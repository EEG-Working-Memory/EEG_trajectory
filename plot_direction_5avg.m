%���������5��ͨ��ƽ��������ݣ�����һ��������ĳ��Ƶ�ʶε�����Trial�������켣���켣�����߳��ֵ��Ⱥ�˳����ɫ��ǳ����
load('Channels_5avg_max_psd.mat');
c=2;    %ָ��condition
task=23;    %ָ������
for k=1:5   %ָ���������߷�Χ
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
                %ѡ��Ҫʹ�õ�Ƶ�ʶ�
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