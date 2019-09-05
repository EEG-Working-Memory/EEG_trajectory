#将20个被测试者划分成测试集和训练集，使用直方图统计训练集的能量轨迹中各区域连线出现次数，选出有效连线
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

REPEAT_TIME=100     #分类时交叉验证的次数
REPEAT_TIME_person=10
Threshold=2         #直方图有效连线判断的阈值
Threshold_all=160

band='lowgamma'
con=2

counts=np.zeros((26,26))
train_hists=[]
train_label=[]
test_hists=[]
test_label=[]

def read_data_hist_count(band='alpha',con=1,person=1):
	#从训练集数据中统计两种任务出现次数，用于挑选有效连线
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
    
    #进行直方图统计，两种任务计数分别为1和-1表示区别
    hists = []
    bandPsdMax = bandsMax[band]
    avgLocs = bandsMax['avgLocs']
    chanlocs = events['EEG']['chanlocs']
    hist1 = np.zeros((26, 26))
    for i in eventsConx:
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(23):
            if(allevents[i][con-1]==13):
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
            else:
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
    
    #挑选有效的连线                
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
    newHists = []
    for hist in hists:
        newHist=[]
        for index in goodIndex:
            counts[index[0]][index[1]]+=hist[index[0]][index[1]]

    #sio.savemat('../%s_con%d_person%d_hist.mat' %(band, con, person), {'hist':newHists, 'label':labels, 'index':goodIndex})
    return newHists

def read_data_hist_train(band='alpha',con=1,person=1,goodIndex=[]):
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
                train_label.append(0)
            else:
                train_label.append(1)
    
    #进行直方图统计，两种任务计数分别为1和-1表示区别
    hists = []
    bandPsdMax = bandsMax[band]
    avgLocs = bandsMax['avgLocs']
    chanlocs = events['EEG']['chanlocs']
    hist1 = np.zeros((26, 26))
    for i in eventsConx:
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(23):
            if(allevents[i][con-1]==13):
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
            else:
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
    
    #统计出现次数
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
        train_hists.append(newHist)
        
def read_data_hist_test(band='alpha',con=1,person=1,goodIndex=[]):
	#从数据中选择特征连线，统计形成计数训练用或测试用直方图
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
                test_label.append(0)
            else:
                test_label.append(1)
    
    #进行直方图统计，两种任务计数分别为1和-1表示区别
    hists = []
    bandPsdMax = bandsMax[band]
    avgLocs = bandsMax['avgLocs']
    chanlocs = events['EEG']['chanlocs']
    hist1 = np.zeros((26, 26))
    for i in eventsConx:
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(23):
            if(allevents[i][con-1]==13):
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]+=1
            else:
                hist1[int(currentTrial[j][1]-1)][int(currentTrial[j+1][1]-1)]-=1
    
    #统计出现次数
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
        test_hists.append(newHist)
    
def vecClusterAnalysis():
    clf = SVC(kernel='linear')      #使用SVM算法进行分类，下面是可以替代采用的分类算法
    #clf = tree.DecisionTreeClassifier()
    #clf=KNeighborsClassifier(n_neighbors=3)
    #clf=AdaBoostClassifier(n_estimators=100)
    #clf=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0)
    clf.fit(train_hists, train_label)
    acc = clf.score(test_hists,test_label)
    print acc
    

if __name__ == '__main__':
    for i in range(REPEAT_TIME_person):
		#划分测试集与训练集
        input_size=20
        testnum = int(input_size * 0.2)
        test_slice = random.sample(range(0, input_size), testnum)
        train_slice = list(set(range(20))-set(test_slice))
        for j in train_slice:
            read_data_hist_count(band, con, j+1)   #从训练集数据的最大通道和能量信息中统计两种任务出现次数
													#前两个参数为指定的频率段和condition
        
		#选取特征
		good_index=[]
        for k in range(26):
            for l in range(26):
                if counts[k][l] >= Threshold_all:
                    good_index.append([k,l])
        for j in train_slice:
            read_data_hist_train(band, con, j+1, good_index)	#从训练集数据中选择特征连线，统计形成计数训练用直方图
        for j in test_slice:
            read_data_hist_test(band, con, j+1, good_index)		#从测试集数据中选择特征连线，统计形成计数测试用直方图
        vecClusterAnalysis()
        
		#全局变量初始化
		train_hists=[]
        train_label=[]
        test_hists=[]
        test_label=[]
        counts=np.zeros((26,26))
    #sio.savemat('../counts.mat' , {'counts':counts})