%在脑图上画出划分好的通道区域中心点，需要EEG_Box包下的topoplot函数
load('Channels_5avg_max_psd.mat')
load('CLAS_VP01_onedata_STBFH_MNT.mat')
figure;
topoplot(avgLocs,EEG.chanlocs,'style','blank');