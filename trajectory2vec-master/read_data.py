import cPickle
import h5py
import numpy as np

#将最大通道和能量信息读取成轨迹信息，参数为指定的频率段、condition和被测试人
def read_data(band='alpha',con=1,person=1):
    bandsMax = h5py.File('../Channels_max_psd.mat', 'r')
    eventsConx = []
    labels = []
    events = h5py.File('../CLAS_VP{:0>2d}_onedata_STBFH_MNT.mat'.format(person),'r')
    allevents = events['allevents']
    allgoodevents = events['allgoodevents']
    
    #生成标签信息
    for i in range(80):
        if(allgoodevents[i][con-1] == 1):
            eventsConx.append(i)
            if(allevents[i][con-1] == 13):
                labels.append(0)
            else:
                labels.append(1)
    
    #生成轨迹信息           
    data = []
    bandPsdMax = bandsMax[band]
    chanlocs = events['EEG']['chanlocs']
    for i in eventsConx:
        currentTrial = bandPsdMax[person-1][con-1][i]
        t = 0
        currentTrac = []
        for j in range(24):
            #保存的轨迹点信息为时间、能量值、通道X轴坐标、通道Y轴坐标
            currentTrac.append([t, currentTrial[j][0], events[chanlocs['X'][currentTrial[j][1]-1][0]][0][0],events[chanlocs['Y'][currentTrial[j][1]-1][0]][0][0]])
            t+=160
        data.append(currentTrac)
    cPickle.dump(data,open('./band_data/trajectories','w'))
    cPickle.dump(labels,open('./band_data/labels','w'))
    return data

if __name__ == '__main__':
    read_data()