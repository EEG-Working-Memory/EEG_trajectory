%�������ֵ�ԭʼʱ������

%ָ���������ߺ�����
person=1;   
con=1;
load(['stft_VP', sprintf('%02d', person), '_psd_con',sprintf('%d',con),'.mat']);
sum=40;
figure
hold on

for i=1:50  %ָ����ͼ���ݵ㷶Χ
    plot((reshape(onedata(1,i,:,11),1,4000)+sum)/80,'k')
    xlabel('time(ms)')
    ylabel('Channel')
    sum = sum+80;
end