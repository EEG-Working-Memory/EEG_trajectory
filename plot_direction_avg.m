%针对对每个被测试者平均后的功率谱密度信息，画出一个任务下所有被测试者的能量轨迹，轨迹按照线出现的先后顺序颜色由浅变深
load('Channels_mean_max_psd.mat');
for i=1:4   %选择任务范围
    figure
    count=1;
    for k=1:20
        subplot(4,5,count)
        hold on
        load(['CLAS_VP', sprintf('%02d', k), '_onedata_STBFH_MNT.mat']);
        x=zeros(1,24);
        y=zeros(1,24);
        for j=1:24
            %选择使用的频率段
            x(j)=EEG.chanlocs(alpha(2,j,i,k)).X;
            y(j)=EEG.chanlocs(alpha(2,j,i,k)).Y;
        end
        plot(x(1),y(1),'o')
        for j=1:23
            plot(x(j:j+1),y(j:j+1),'color',[0 1-j/23 0],'LineWidth',1)
        end
        plot(x(24),y(24),'^')
        xlim([-1 1])
        ylim([-1 1])
        xlabel('Channel location axis X')
        ylabel('Channel location axis Y')
        hold off
        count=count+1;
    end
end