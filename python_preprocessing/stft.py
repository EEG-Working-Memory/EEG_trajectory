import h5py
import hdf5storage
import numpy as np
from scipy.signal import spectrogram

for i in range(20):
    f=h5py.File('..\CLAS_VP{:0>2d}_onedata_STBFH_MNT.mat'.format(i+1),'r')
    onedata=f['onedata']
    
    psd=np.zeros((501,24,128,80))
    for j in range(80):
        for k in range(128):
            x=onedata[j,:,k,0]
            f,t,s=spectrogram(x,1000,('hamming'),nperseg=320,noverlap=160,nfft=1000)
            psd[:,:,k,j]=s
    hdf5storage.savemat('..\stft_VP{:0>2d}_psd_con1.mat'.format(i+1), {'psd':psd})
     
    psd=np.zeros((501,24,128,80))
    for j in range(80):
        for k in range(128):
            x=onedata[j,:,k,1]
            f,t,s=spectrogram(x,1000,('hamming'),nperseg=320,noverlap=160,nfft=1000)
            psd[:,:,k,j]=s
    hdf5storage.savemat('..\stft_VP{:0>2d}_psd_con2.mat'.format(i+1), {'psd':psd})