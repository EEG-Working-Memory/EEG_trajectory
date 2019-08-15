import cPickle
import h5py
import numpy as np

#将按一个被测试者的不同Trial平均后最大通道和能量信息读取成轨迹信息，参数为指定的频率段、condition和被测试人
def read_data_chan(band='alpha',con=1):
    bandsMax = h5py.File('../Channels_mean_max_psd.mat', 'r')
    labels_chan = []
	
	#生成轨迹和标签信息  
    data = []
    bandPsdMax = bandsMax[band]
    for person in range(1,21):
        events = h5py.File('../CLAS_VP{:0>2d}_onedata_STBFH_MNT.mat'.format(person),'r')
        chanlocs = events['EEG']['chanlocs']
        t=0
        currentTrac = []
        currentTrial = bandPsdMax[person-1][(con-1)*2]
        for j in range(24):
			#保存的轨迹点信息为时间、能量值、通道X轴坐标、通道Y轴坐标
            currentTrac.append([t,currentTrial[j][0],events[chanlocs['X'][currentTrial[j][1]-1][0]][0][0],events[chanlocs['Y'][currentTrial[j][1]-1][0]][0][0]])
            t+=160
        data.append(currentTrac)
        labels_chan.append(0)
        t=0
        currentTrac = []
        currentTrial = bandPsdMax[person-1][(con-1)*2+1]
        for j in range(24):
			#保存的轨迹点信息为时间、能量值、通道X轴坐标、通道Y轴坐标
            currentTrac.append([t,currentTrial[j][0],events[chanlocs['X'][currentTrial[j][1]-1][0]][0][0],events[chanlocs['Y'][currentTrial[j][1]-1][0]][0][0]])
            t+=160
        data.append(currentTrac)
        labels_chan.append(1)
    #print np.shape(data)
    cPickle.dump(data,open('./band_data/trajectories','w'))
    cPickle.dump(labels_chan,open('./band_data/labels_chan','w'))
    return data
        
if __name__ == '__main__':
    read_data_chan()
