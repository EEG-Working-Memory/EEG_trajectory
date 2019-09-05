#将能量轨迹分为两段，然后对每一段使用直方图统计能量轨迹中各区域连线出现次数，选出有效的连线作为特征进行分类训练
import random
import cPickle
import h5py
import numpy as np

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

REPEAT_TIME=100     #分类时交叉验证的次数
Threshold=2         #直方图有效连线判断的阈值

def read_data_hist(band='alpha',con=1,person=1):
    bandsMax = h5py.File('../Channels_5avg_max_psd.mat', 'r')
    eventsConx = []
    labels = []
    events = h5py.File('../CLAS_VP{:0>2d}_onedata_STBFH_MNT.mat'.format(person),'r')
    allevents = events['allevents']
    allgoodevents = events['allgoodevents']
    
    #生成标签数据
    for i in range(80):
        if(allgoodevents[i][con-1] == 1):
            eventsConx.append(i)
            if(allevents[i][con-1] == 13):
                labels.append(0)
            else:
                labels.append(1)
    
    #分两段进行直方图统计，两种任务计数分别为1和-1表示区别
    hists = []
    bandPsdMax = bandsMax[band]
    avgLocs = bandsMax['avgLocs']
    chanlocs = events['EEG']['chanlocs']
    hist1 = np.zeros((26, 26))
    hist2 = np.zeros((26, 26))
    for i in eventsConx:
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(16):
            if(allevents[i][con-1]==13):
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
            else:
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
        for j in range(16,23):
            if(allevents[i][con-1]==13):
                hist2[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
            else:
                hist2[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
    
    #挑选有效的连线
    goodIndex = []
    for indexes in range(26):
        for index in range(26):
            if hist1[indexes][index] >= Threshold or hist1[indexes][index] <= -Threshold:
                goodIndex.append([indexes,index])
            if hist2[indexes][index] >= Threshold or hist1[indexes][index] <= -Threshold:
                goodIndex.append([indexes,index])
    hists = []
    for i in eventsConx:
        hist = np.zeros((26, 26))
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(23):
            hist[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
        hists.append(hist)
    newHists = []
    for hist in hists:
        newHist=[]
        for index in goodIndex:
            newHist.append(hist[index[0]][index[1]])
        newHists.append(newHist)
        
    cPickle.dump(labels,open('./band_data/labels','w'))
    return newHists

def vecClusterAnalysis(hists):
    input_size = len(hists)
    labels = np.array(cPickle.load(open('./band_data/labels')))
    data=np.reshape(hists,(input_size,-1))
    
    total=0
    for i in range(REPEAT_TIME):
        testnum = int(input_size * 0.2)
        test_slice = random.sample(range(0, input_size), testnum)
        test = data[test_slice,:]
        test_label = labels[test_slice]
        train = np.delete(data, test_slice, axis=0)
        train_label = np.delete(labels, test_slice, axis=0)
    
        clf = SVC(kernel='linear')      #使用SVM算法进行分类，下面是可以替代采用的分类算法
        #clf = tree.DecisionTreeClassifier()
        #clf=KNeighborsClassifier(n_neighbors=3)
        #clf=AdaBoostClassifier(n_estimators=100)
        #clf=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0)
        clf.fit(train, train_label)
        acc = clf.score(test,test_label)
        total+=acc
    print(total / REPEAT_TIME)

if __name__ == '__main__':
    for i in range(20):
        hists=read_data_hist('alpha', 1, i+1)   #将最大通道和能量信息读取成轨迹信息，前两个参数为指定的频率段和condition
        vecClusterAnalysis(hists)
