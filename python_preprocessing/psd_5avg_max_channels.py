import h5py
import hdf5storage
import numpy as np

p=[[99,66,42,41,3],[34,1,67,33,97],[98,2,65,35],[108,71,107,7,46],[70,36,6,40],[101,37,8,100,4],[38,68,103,102,5],[39,69,105,104,106],[12,73,109,72,47],[75,43,13,74,9],[77,10,14,76,78],[79,11,15,44,80],[82,51,23,17,83],[52,110,84,18,111],[112,48,53,19,113],[114,49,54,20,115],[16,45,116,50,81],[24,85,119,56,57],[25,87,120,86,58],[26,89,122,88,59],[90,55,91,21,22],[118,60,28,117,92],[93,62,29,61,30],[63,121,31,94,64],[123,27,32,95,124],[127,126,96,125,128]]
theta = np.zeros((2, 24, 80, 2, 20))
alpha = np.zeros((2, 24, 80, 2, 20))
lowbeta = np.zeros((2, 24, 80, 2, 20))
highbeta = np.zeros((2, 24, 80, 2, 20))
lowgamma = np.zeros((2, 24, 80, 2, 20))
highgamma = np.zeros((2, 24, 80, 2, 20))
avgLocs=np.zeros(26)
for i in range(26):
    avgLocs[i]=p[i][0]

for i in range(20):
    f=h5py.File('..\stft_VP{:0>2d}_psd_con1.mat'.format(i+1),'r')
    psd=np.array(f['psd'])
    for j in range(80):
        for k in range(24):
            avgPsd=np.zeros((26,101))
            for l in range(26):
                avgPsd[l,:]=np.mean(np.reshape(psd[j,np.array(p[l])-1,k,0:101],(-1,101)),0)
            
            psdInTheta=np.reshape(avgPsd[:,4:8],(26,4))
            eachMax=np.amax(psdInTheta,0)
            eachCh=np.argmax(psdInTheta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            theta[0,k,j,0,i]=bandMax
            theta[1,k,j,0,i]=maxCh
            psdInAlpha=np.reshape(avgPsd[:,8:13],(26,5))
            eachMax=np.amax(psdInAlpha,0)
            eachCh=np.argmax(psdInAlpha,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            alpha[0,k,j,0,i]=bandMax
            alpha[1,k,j,0,i]=maxCh
            psdInLowbeta=np.reshape(avgPsd[:,14:21],(26,7))
            eachMax=np.amax(psdInLowbeta,0)
            eachCh=np.argmax(psdInLowbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowbeta[0,k,j,0,i]=bandMax
            lowbeta[1,k,j,0,i]=maxCh
            psdInHighbeta=np.reshape(avgPsd[:,20:31],(26,11))
            eachMax=np.amax(psdInHighbeta,0)
            eachCh=np.argmax(psdInHighbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highbeta[0,k,j,0,i]=bandMax
            highbeta[1,k,j,0,i]=maxCh
            psdInLowgamma=np.reshape(avgPsd[:,30:61],(26,31))
            eachMax=np.amax(psdInLowgamma,0)
            eachCh=np.argmax(psdInLowgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowgamma[0,k,j,0,i]=bandMax
            lowgamma[1,k,j,0,i]=maxCh
            psdInHighgamma=np.reshape(avgPsd[:,60:101],(26,41))
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
            avgPsd=np.zeros((26,101))
            for l in range(26):
                avgPsd[l,:]=np.mean(np.reshape(psd[j,np.array(p[l])-1,k,0:101],(-1,101)),0)
                
            psdInTheta=np.reshape(avgPsd[:,4:8],(26,4))
            eachMax=np.amax(psdInTheta,0)
            eachCh=np.argmax(psdInTheta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            theta[0,k,j,1,i]=bandMax
            theta[1,k,j,1,i]=maxCh
            psdInAlpha=np.reshape(avgPsd[:,8:13],(26,5))
            eachMax=np.amax(psdInAlpha,0)
            eachCh=np.argmax(psdInAlpha,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            alpha[0,k,j,1,i]=bandMax
            alpha[1,k,j,1,i]=maxCh
            psdInLowbeta=np.reshape(avgPsd[:,14:21],(26,7))
            eachMax=np.amax(psdInLowbeta,0)
            eachCh=np.argmax(psdInLowbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowbeta[0,k,j,1,i]=bandMax
            lowbeta[1,k,j,1,i]=maxCh
            psdInHighbeta=np.reshape(avgPsd[:,20:31],(26,11))
            eachMax=np.amax(psdInHighbeta,0)
            eachCh=np.argmax(psdInHighbeta,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highbeta[0,k,j,1,i]=bandMax
            highbeta[1,k,j,1,i]=maxCh
            psdInLowgamma=np.reshape(avgPsd[:,30:61],(26,31))
            eachMax=np.amax(psdInLowgamma,0)
            eachCh=np.argmax(psdInLowgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            lowgamma[0,k,j,1,i]=bandMax
            lowgamma[1,k,j,1,i]=maxCh
            psdInHighgamma=np.reshape(avgPsd[:,60:101],(26,41))
            eachMax=np.amax(psdInHighgamma,0)
            eachCh=np.argmax(psdInHighgamma,0)
            bandMax=np.amax(eachMax)
            index=np.argmax(eachMax)
            maxCh=eachCh[index]
            highgamma[0,k,j,1,i]=bandMax
            highgamma[1,k,j,1,i]=maxCh
            
hdf5storage.savemat('..\Channels_5avg_max_psd.mat', {'theta':theta, 'alpha':alpha, 'lowbeta':lowbeta, 'highbeta':highbeta, 'lowgamma':lowgamma,'highgamma':highgamma})
