%用subplot画出直方图挑选出来的每个被测试者的有效连线
load('Channels_5avg_max_psd.mat')
load('CLAS_VP01_onedata_STBFH_MNT.mat')
figure;
band="theta";   %指定频率段
con=1;          %指定任务
for person=1:20
    load([sprintf('%s',band),'_con',sprintf('%d',con),'_person',sprintf('%d',person),'.mat'])
    subplot(5,4,person)
    hold on;
    indexSize=size(index);
    for i=1:indexSize(1)
        plot([EEG.chanlocs(avgLocs(index(i,1)+1)).X EEG.chanlocs(avgLocs(index(i,2)+1)).X],[EEG.chanlocs(avgLocs(index(i,1)+1)).Y EEG.chanlocs(avgLocs(index(i,2)+1)).Y],'color',[0 0.5 0],'LineWidth',1)
    end
    xlim([-1 1])
    ylim([-1 1])
    hold off
end