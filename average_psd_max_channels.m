%计算每个记忆任务下所有trials的功率谱密度（psd）平均值，然后选出5个频率段上平均能量最大的通道
theta = zeros(2, 24, 4, 20);
alpha = zeros(2, 24, 4, 20);
lowbeta = zeros(2, 24, 4, 20);
highbeta = zeros(2, 24, 4, 20);
lowgamma = zeros(2, 24, 4, 20);
highgamma = zeros(2, 24, 4, 20);
for i=1:20
    load(['stft_VP', sprintf('%02d', i), '_psd_con1.mat']);
    load(['CLAS_VP', sprintf('%02d', i), '_onedata_STBFH_MNT.mat']);
    new_1=[];
    new_2=[];
    for j=1:80
       if(allgoodevents(1,j)==1)
           if(allevents(1,j)==13)
               new_1=[new_1,j];
           end
           else
               new_2=[new_2,j];
       end
    end
    new_psd_1=zeros(501,24,128,size(new_1,2));
    new_psd_2=zeros(501,24,128,size(new_2,2));
    for j=1:size(new_1,2)
        new_psd_1(:,:,:,j)=psd(:,:,:,new_1(j));
    end
    for j=1:size(new_2,2)
        new_psd_2(:,:,:,j)=psd(:,:,:,new_2(j));
    end
    mean_psd_1=mean(new_psd_1,4);   %Face
    mean_psd_2=mean(new_psd_2,4);   %House
        for k=1:24
            psdInTheta = reshape(mean_psd_1(5:8,k,:),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,1,i) = bandMax;
            theta(2,k,1,i) = maxCh;
            psdInAlpha = reshape(mean_psd_1(9:13,k,:),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,1,i) = bandMax;
            alpha(2,k,1,i) = maxCh;
            psdInLowbeata = reshape(mean_psd_1(15:21,k,:),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,1,i) = bandMax;
            lowbeta(2,k,1,i) = maxCh;
            psdInHighbeata = reshape(mean_psd_1(21:31,k,:),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,1,i) = bandMax;
            highbeta(2,k,1,i) = maxCh;
            psdInLowgamma = reshape(mean_psd_1(31:61,k,:),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,1,i) = bandMax;
            lowgamma(2,k,1,i) = maxCh;
            psdInHighgamma = reshape(mean_psd_1(61:101,k,:),[41,128]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,1,i) = bandMax;
            highgamma(2,k,1,i) = maxCh;
        end
        for k=1:24
            psdInTheta = reshape(mean_psd_2(5:8,k,:),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,2,i) = bandMax;
            theta(2,k,2,i) = maxCh;
            psdInAlpha = reshape(mean_psd_2(9:13,k,:),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,2,i) = bandMax;
            alpha(2,k,2,i) = maxCh;
            psdInLowbeata = reshape(mean_psd_2(15:21,k,:),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,2,i) = bandMax;
            lowbeta(2,k,2,i) = maxCh;
            psdInHighbeata = reshape(mean_psd_2(21:31,k,:),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,2,i) = bandMax;
            highbeta(2,k,2,i) = maxCh;
            psdInLowgamma = reshape(mean_psd_2(31:61,k,:),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,2,i) = bandMax;
            lowgamma(2,k,2,i) = maxCh;
            psdInHighgamma = reshape(mean_psd_2(61:101,k,:),[41,128]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,2,i) = bandMax;
            highgamma(2,k,2,i) = maxCh;
        end
end
for i=1:20
    load(['stft_VP', sprintf('%02d', i), '_psd_con2.mat']);
    load(['CLAS_VP', sprintf('%02d', i), '_onedata_STBFH_MNT.mat']);
    new_1=[];
    new_2=[];
    for j=1:80
       if(allgoodevents(2,j)==1)
           if(allevents(2,j)==13)
               new_1=[new_1,j];
           end
           else
               new_2=[new_2,j];
       end
    end
    new_psd_1=zeros(501,24,128,size(new_1,2));
    new_psd_2=zeros(501,24,128,size(new_2,2));
    for j=1:size(new_1,2)
        new_psd_1(:,:,:,j)=psd(:,:,:,new_1(j));
    end
    for j=1:size(new_2,2)
        new_psd_2(:,:,:,j)=psd(:,:,:,new_2(j));
    end
    mean_psd_1=mean(new_psd_1,4);   %digit
    mean_psd_2=mean(new_psd_2,4);   %letter
        for k=1:24
            psdInTheta = reshape(mean_psd_1(5:8,k,:),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,3,i) = bandMax;
            theta(2,k,3,i) = maxCh;
            psdInAlpha = reshape(mean_psd_1(9:13,k,:),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,3,i) = bandMax;
            alpha(2,k,3,i) = maxCh;
            psdInLowbeata = reshape(mean_psd_1(15:21,k,:),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,3,i) = bandMax;
            lowbeta(2,k,3,i) = maxCh;
            psdInHighbeata = reshape(mean_psd_1(21:31,k,:),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,3,i) = bandMax;
            highbeta(2,k,3,i) = maxCh;
            psdInLowgamma = reshape(mean_psd_1(31:61,k,:),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,3,i) = bandMax;
            lowgamma(2,k,3,i) = maxCh;
            psdInHighgamma = reshape(mean_psd_1(61:101,k,:),[41,128]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,3,i) = bandMax;
            highgamma(2,k,3,i) = maxCh;
        end
        for k=1:24
            psdInTheta = reshape(mean_psd_2(5:8,k,:),[4,128]);
            [eachMax,eachCh] = max(psdInTheta,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            theta(1,k,4,i) = bandMax;
            theta(2,k,4,i) = maxCh;
            psdInAlpha = reshape(mean_psd_2(9:13,k,:),[5,128]);
            [eachMax,eachCh] = max(psdInAlpha,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            alpha(1,k,4,i) = bandMax;
            alpha(2,k,4,i) = maxCh;
            psdInLowbeata = reshape(mean_psd_2(15:21,k,:),[7,128]);
            [eachMax,eachCh] = max(psdInLowbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowbeta(1,k,4,i) = bandMax;
            lowbeta(2,k,4,i) = maxCh;
            psdInHighbeata = reshape(mean_psd_2(21:31,k,:),[11,128]);
            [eachMax,eachCh] = max(psdInHighbeata,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highbeta(1,k,4,i) = bandMax;
            highbeta(2,k,4,i) = maxCh;
            psdInLowgamma = reshape(mean_psd_2(31:61,k,:),[31,128]);
            [eachMax,eachCh] = max(psdInLowgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            lowgamma(1,k,4,i) = bandMax;
            lowgamma(2,k,4,i) = maxCh;
            psdInHighgamma = reshape(mean_psd_2(61:101,k,:),[41,128]);
            [eachMax,eachCh] = max(psdInHighgamma,[],2);
            [bandMax,index] = max(eachMax);
            maxCh = eachCh(index);
            highgamma(1,k,4,i) = bandMax;
            highgamma(2,k,4,i) = maxCh;
        end
end
save('Channels_mean_max_psd.mat','theta','alpha','lowbeta','highbeta','lowgamma','highgamma')