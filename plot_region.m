%����ͼ�ϻ������ֺõ�ͨ���������ĵ㣬��ҪEEG_Box���µ�topoplot����
load('Channels_5avg_max_psd.mat')
load('CLAS_VP01_onedata_STBFH_MNT.mat')
figure;
topoplot(avgLocs,EEG.chanlocs,'style','blank');