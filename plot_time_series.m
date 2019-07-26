%画出部分的原始时序数据

%指定被测试者和任务
person=1;   
con=1;
load(['stft_VP', sprintf('%02d', person), '_psd_con',sprintf('%d',con),'.mat']);
sum=40;
figure
hold on

for i=1:50  %指定画图数据点范围
    plot((reshape(onedata(1,i,:,11),1,4000)+sum)/80,'k')
    xlabel('time(ms)')
    ylabel('Channel')
    sum = sum+80;
end