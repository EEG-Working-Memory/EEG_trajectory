import h5py
import hdf5storage
import numpy as np

theta = np.zeros((2, 24, 80, 2, 20))
alpha = np.zeros((2, 24, 80, 2, 20))
lowbeta = np.zeros((2, 24, 80, 2, 20))
highbeta = np.zeros((2, 24, 80, 2, 20))
lowgamma = np.zeros((2, 24, 80, 2, 20))
highgamma = np.zeros((2, 24, 80, 2, 20))

for i in range(20):
    f=h5py.File('..\stft_VP{:0>2d}_psd_con1.mat'.format(i+1),'r')
    psd=f['psd']
    for j in range(80):
        for k in range(24):
            psdInTheta=np.reshape(psd[j,:,k,4:8],(128,4))
            eachMax=np.amax(psdInTheta,0)
            eachCh=np.argmax(psdInTheta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            theta[0,k,j,0,i]=bandMax
            theta[1,k,j,0,i]=maxCh
            psdInAlpha=np.reshape(psd[j,:,k,8:13],(128,5))
            eachMax=np.amax(psdInAlpha,0)
            eachCh=np.argmax(psdInAlpha,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            alpha[0,k,j,0,i]=bandMax
            alpha[1,k,j,0,i]=maxCh
            psdInLowbeta=np.reshape(psd[j,:,k,14:21],(128,7))
            eachMax=np.amax(psdInLowbeta,0)
            eachCh=np.argmax(psdInLowbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowbeta[0,k,j,0,i]=bandMax
            lowbeta[1,k,j,0,i]=maxCh
            psdInHighbeta=np.reshape(psd[j,:,k,20:31],(128,11))
            eachMax=np.amax(psdInHighbeta,0)
            eachCh=np.argmax(psdInHighbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highbeta[0,k,j,0,i]=bandMax
            highbeta[1,k,j,0,i]=maxCh
            psdInLowgamma=np.reshape(psd[j,:,k,30:61],(128,31))
            eachMax=np.amax(psdInLowgamma,0)
            eachCh=np.argmax(psdInLowgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowgamma[0,k,j,0,i]=bandMax
            lowgamma[1,k,j,0,i]=maxCh
            psdInHighgamma=np.reshape(psd[j,:,k,60:101],(128,41))
            eachMax=np.amax(psdInHighgamma,0)
            eachCh=np.argmax(psdInHighgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highgamma[0,k,j,0,i]=bandMax
            highgamma[1,k,j,0,i]=maxCh

for i in range(20):
    f=h5py.File('..\stft_VP{:0>2d}_psd_con2.mat'.format(i+1),'r')
    psd=f['psd']
    for j in range(80):
        for k in range(24):
            psdInTheta=np.reshape(psd[j,:,k,4:8],(128,4))
            eachMax=np.amax(psdInTheta,0)
            eachCh=np.argmax(psdInTheta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            theta[0,k,j,1,i]=bandMax
            theta[1,k,j,1,i]=maxCh
            psdInAlpha=np.reshape(psd[j,:,k,8:13],(128,5))
            eachMax=np.amax(psdInAlpha,0)
            eachCh=np.argmax(psdInAlpha,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            alpha[0,k,j,1,i]=bandMax
            alpha[1,k,j,1,i]=maxCh
            psdInLowbeta=np.reshape(psd[j,:,k,14:21],(128,7))
            eachMax=np.amax(psdInLowbeta,0)
            eachCh=np.argmax(psdInLowbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowbeta[0,k,j,1,i]=bandMax
            lowbeta[1,k,j,1,i]=maxCh
            psdInHighbeta=np.reshape(psd[j,:,k,20:31],(128,11))
            eachMax=np.amax(psdInHighbeta,0)
            eachCh=np.argmax(psdInHighbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highbeta[0,k,j,1,i]=bandMax
            highbeta[1,k,j,1,i]=maxCh
            psdInLowgamma=np.reshape(psd[j,:,k,30:61],(128,31))
            eachMax=np.amax(psdInLowgamma,0)
            eachCh=np.argmax(psdInLowgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowgamma[0,k,j,1,i]=bandMax
            lowgamma[1,k,j,1,i]=maxCh
            psdInHighgamma=np.reshape(psd[j,:,k,60:101],(128,41))
            eachMax=np.amax(psdInHighgamma,0)
            eachCh=np.argmax(psdInHighgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highgamma[0,k,j,1,i]=bandMax
            highgamma[1,k,j,1,i]=maxCh
            
hdf5storage.savemat('..\Channels_max_psd.mat', {'theta':theta, 'alpha':alpha, 'lowbeta':lowbeta, 'highbeta':highbeta, 'lowgamma':lowgamma,'highgamma':highgamma})