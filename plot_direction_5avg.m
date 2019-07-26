%针对区域下5个通道平均后的数据，画出一个任务下某个频率段的所有Trial的能量轨迹，轨迹按照线出现的先后顺序颜色由浅变深
load('Channels_5avg_max_psd.mat');
c=2;    %指定condition
task=23;    %指定任务
for k=1:5   %指定被测试者范围
	figure
	count=1;
	load(['CLAS_VP', sprintf('%02d', k), '_onedata_STBFH_MNT.mat']);
	for t=1:80
		if(allgoodevents(c,t)==1 && allevents(c,t)==task)
			subplot(8,5,count)
			hold on
			x=zeros(1,24);
			y=zeros(1,24);
			for j=1:24
                %选择要使用的频率段
				x(j)=EEG.chanlocs(avgLocs(lowbeta(2,j,t,c,k))).X;
				y(j)=EEG.chanlocs(avgLocs(lowbeta(2,j,t,c,k))).Y;
			end
			plot(x(1),y(1),'o')
			for j=1:23
				plot(x(j:j+1),y(j:j+1),'color',[0 1-j/23 0],'LineWidth',1)
			end
			plot(x(24),y(24),'^')
			xlim([-1 1])
			ylim([-1 1])
			hold off
			count = count+1;
		end
	end
end