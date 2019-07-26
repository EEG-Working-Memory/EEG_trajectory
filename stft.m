%对原始时序数据进行短时距傅里叶变换
for i=1:20
    load(['CLAS_VP', sprintf('%02d', i), '_onedata_STBFH_MNT.mat'], 'onedata');
    psd = zeros(501,24,128,80);
    
    %condition 1
    for j = 1:80
        for k = 1:128
            x = reshape(onedata(1,k,:,j),[1,4000]); 
            [s,f,t, ps] = spectrogram(x,320, [], 1000, 1e3);
            psd(:,:,k,j) = ps;
        end
    end
    save(['stft_VP', sprintf('%02d', i), '_psd_con1.mat'], 'psd')
    
    %condition 2
    psd = zeros(501,24 ,128,80);
    for j = 1:80
        for k = 1:128
            x = reshape(onedata(2,k,:,j),[1,4000]); 
            [s,f,t, ps] = spectrogram(x,320, [], 1000, 1e3);
            psd(:,:,k,j) = ps;
       end
    end
    save(['stft_VP', sprintf('%02d', i), '_psd_con2.mat'], 'psd')
end