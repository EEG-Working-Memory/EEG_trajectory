#将每个被测试者的数据划分成测试集和训练集，使用直方图统计训练集的能量轨迹中各区域连线出现次数，选出有效连线
#再统计测试集有效连线的出现次数进行分类
import random
import cPickle
import h5py
import numpy as np
import scipy.io as sio

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

REPEAT_TIME=10     #分类时交叉验证的次数
Threshold=4        #直方图有效连线判断的阈值

counts=np.zeros((26,26))
train_hists=[]
train_label=[]
test_hists=[]
test_label=[]
   
def read_random_data(band='alpha',con=1,person=1):
	#将每个被测试者的数据划分成测试集和训练集，使用直方图统计训练集和测试集的能量轨迹中各区域连线出现次数
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
    #划分测试集与训练集  
    input_size = len(labels)
    testnum = int(input_size * 0.2)
    test_slice = random.sample(range(0, input_size), testnum)
    test_labels=np.array(labels)[test_slice]
    train_labels=list(np.delete(labels, test_slice, axis=0))
    for i in test_labels:
        test_label.append(i)
    for i in train_labels:
        train_label.append(i)
        
    #进行直方图统计，两种任务计数分别为1和-1表示区别
    hists = []
    bandPsdMax = bandsMax[band]
    avgLocs = bandsMax['avgLocs']
    chanlocs = events['EEG']['chanlocs']
    hist1 = np.zeros((26, 26))
    count=0
    for i in eventsConx:
        if count not in test_slice:
            currentTrial = bandPsdMax[person-1][con-1][i]
            t = 0
            currentTrac = []
            for j in range(23):
                if(allevents[i][con-1]==13):
                    hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
                else:
                    hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
        count+=1
    
    #挑选有效连线并统计出现次数         
    goodIndex = []
    for indexes in range(26):
        for index in range(26):
            if hist1[indexes][index] >= Threshold or hist1[indexes][index] <= -Threshold:
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
    count=0
    for hist in hists:
        newHist=[]
        if count in test_slice:
            for index in goodIndex:
                newHist.append(hist[index[0]][index[1]])
            test_hists.append(newHist)
        else:
            for index in goodIndex:
                newHist.append(hist[index[0]][index[1]])
            train_hists.append(newHist)
        count+=1
        
    cPickle.dump(labels,open('./band_data/labels','w'))
    #sio.savemat('../%s_con%d_person%d_hist.mat' %(band, con, person), {'hist':newHists, 'label':labels, 'index':goodIndex})

def vecClusterAnalysis():
    clf = SVC(kernel='linear')      #使用SVM算法进行分类，下面是可以替代采用的分类算法
    #clf = tree.DecisionTreeClassifier()
    #clf=KNeighborsClassifier(n_neighbors=3)
    #clf=AdaBoostClassifier(n_estimators=100)
    #clf=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0)
    clf.fit(train_hists, train_label)
    acc = clf.score(test_hists,test_label)
    return acc

if __name__ == '__main__':
    for i in range(20):
        total=0
        for j in range(REPEAT_TIME):
            read_random_data('highgamma', 2, i+1)   #将每个被测试者的数据划分成测试集和训练集
													#使用直方图统计训练集和测试集的能量轨迹中各区域连线出现次数
            acc=vecClusterAnalysis()
            total+=acc
			
			#全局变量初始化
            train_hists=[]
            train_label=[]
            test_hists=[]
            test_label=[]
			
        print(total / REPEAT_TIME)