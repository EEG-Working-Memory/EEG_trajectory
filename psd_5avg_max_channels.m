%对功率谱密度（psd）按照5个通道一组的区域进行平均，之后选取出5个频率段上的能量最大区域

%每个区域中的通道列表
p={[99,66,42,41,3],[34,1,67,33,97],[98,2,65,35],[108,71,107,7,46],[70,36,6,40],[101,37,8,100,4],[38,68,103,102,5],[39,69,105,104,106],[12,73,109,72,47],[75,43,13,74,9],[77,10,14,76,78],[79,11,15,44,80],[82,51,23,17,83],[52,110,84,18,111],[112,48,53,19,113],[114,49,54,20,115],[16,45,116,50,81],[24,85,119,56,57],[25,87,120,86,58],[26,89,122,88,59],[90,55,91,21,22],[118,60,28,117,92],[93,62,29,61,30],[63,121,31,94,64],[123,27,32,95,124],[127,126,96,125,128]};
theta = zeros(2, 24, 80, 2, 20);
alpha = zeros(2, 24, 80, 2, 20);
lowbeta = zeros(2, 24, 80, 2, 20);
highbeta = zeros(2, 24, 80, 2, 20);
lowgamma = zeros(2, 24, 80, 2, 20);
highgamma = zeros(2, 24, 80, 2, 20);

%保存区域中心点
avgLocs=zeros(1,26);	
for i=1:26
    avgLocs(i)=p{i}(1);
end

%condition 1
for i=1:20
    load(['stft_VP', sprintf('%02d', i), '_psd_con1.mat']);
    for j=1:80
        for k=1:24
            avgPsd=zeros(101,26);
            for l=1:26
                avgPsd(:,l)=mean(reshape(psd(1:101,k,p{l},j),101,[]),2);
            end
            psdInTheta = reshape(avgPsd(5:8,:),[4,26]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,j,1,i) = bandMax;
            theta(2,k,j,1,i) = maxCh;
            psdInAlpha = reshape(avgPsd(9:13,:),[5,26]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,j,1,i) = bandMax;
            alpha(2,k,j,1,i) = maxCh;
            psdInLowbeata = reshape(avgPsd(15:21,:),[7,26]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,j,1,i) = bandMax;
            lowbeta(2,k,j,1,i) = maxCh;
            psdInHighbeata = reshape(avgPsd(21:31,:),[11,26]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,j,1,i) = bandMax;
            highbeta(2,k,j,1,i) = maxCh;
            psdInLowgamma = reshape(avgPsd(31:61,:),[31,26]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,j,1,i) = bandMax;
            lowgamma(2,k,j,1,i) = maxCh;
            psdInHighgamma = reshape(avgPsd(61:101,:),[41,26]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,j,1,i) = bandMax;
            highgamma(2,k,j,1,i) = maxCh;
        end
    end
end

%condition 2
for i=1:20
    load(['stft_VP', sprintf('%02d', i), '_psd_con2.mat']);
    for j=1:80
        for k=1:24
            avgPsd=zeros(101,26);
            for l=1:26
                avgPsd(:,l)=mean(reshape(psd(1:101,k,p{l},j),101,[]),2);
            end
            psdInTheta = reshape(avgPsd(5:8,:),[4,26]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,j,2,i) = bandMax;
            theta(2,k,j,2,i) = maxCh;
            psdInAlpha = reshape(avgPsd(9:13,:),[5,26]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,j,2,i) = bandMax;
            alpha(2,k,j,2,i) = maxCh;
            psdInLowbeata = reshape(avgPsd(15:21,:),[7,26]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,j,2,i) = bandMax;
            lowbeta(2,k,j,2,i) = maxCh;
            psdInHighbeata = reshape(avgPsd(21:31,:),[11,26]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,j,2,i) = bandMax;
            highbeta(2,k,j,2,i) = maxCh;
            psdInLowgamma = reshape(avgPsd(31:61,:),[31,26]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,j,2,i) = bandMax;
            lowgamma(2,k,j,2,i) = maxCh;
            psdInHighgamma = reshape(avgPsd(61:101,:),[41,26]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,j,2,i) = bandMax;
            highgamma(2,k,j,2,i) = maxCh;
        end
    end
end
save('Channels_5avg_max_psd.mat','theta','alpha','lowbeta','highbeta','lowgamma','highgamma','avgLocs')