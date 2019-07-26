%从功率谱密度（psd）中挑选出5个频率段下每个时间段能量最大的通道
theta = zeros(2, 24, 80, 2, 20);
alpha = zeros(2, 24, 80, 2, 20);
lowbeta = zeros(2, 24, 80, 2, 20);
highbeta = zeros(2, 24, 80, 2, 20);
lowgamma = zeros(2, 24, 80, 2, 20);
highgamma = zeros(2, 24, 80, 2, 20);
%condition 1
for i=1:20
    load(['stft_VP', sprintf('%02d', i), '_psd_con1.mat']);
    for j=1:80
        for k=1:24
            psdInTheta = reshape(psd(5:8,k,:,j),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,j,1,i) = bandMax;
            theta(2,k,j,1,i) = maxCh;
            psdInAlpha = reshape(psd(9:13,k,:,j),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,j,1,i) = bandMax;
            alpha(2,k,j,1,i) = maxCh;
            psdInLowbeata = reshape(psd(15:21,k,:,j),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,j,1,i) = bandMax;
            lowbeta(2,k,j,1,i) = maxCh;
            psdInHighbeata = reshape(psd(21:31,k,:,j),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,j,1,i) = bandMax;
            highbeta(2,k,j,1,i) = maxCh;
            psdInLowgamma = reshape(psd(31:61,k,:,j),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,j,1,i) = bandMax;
            lowgamma(2,k,j,1,i) = maxCh;
            psdInHighgamma = reshape(psd(61:101,k,:,j),[41,128]);
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
            psdInTheta = reshape(psd(5:8,k,:,j),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,j,2,i) = bandMax;
            theta(2,k,j,2,i) = maxCh;
            psdInAlpha = reshape(psd(9:13,k,:,j),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,j,2,i) = bandMax;
            alpha(2,k,j,2,i) = maxCh;
            psdInLowbeata = reshape(psd(15:21,k,:,j),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,j,2,i) = bandMax;
            lowbeta(2,k,j,2,i) = maxCh;
            psdInHighbeata = reshape(psd(21:31,k,:,j),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,j,2,i) = bandMax;
            highbeta(2,k,j,2,i) = maxCh;
            psdInLowgamma = reshape(psd(31:61,k,:,j),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,j,2,i) = bandMax;
            lowgamma(2,k,j,2,i) = maxCh;
            psdInHighgamma = reshape(psd(61:101,k,:,j),[41,128]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,j,2,i) = bandMax;
            highgamma(2,k,j,2,i) = maxCh;
        end
    end
end
save('Channels_max_psd.mat','theta','alpha','lowbeta','highbeta','lowgamma','highgamma')