import numpy as np
from ValleyBordersUpdate import *
def CentroidsValley(spectra,Centroids):
    NCent=len(Centroids)    
    for centroidLoc in np.arange(1,NCent,dtype='int'):
        BorderLight_mz=Centroids[centroidLoc-1,2]
        BorderHeavy_mz=Centroids[centroidLoc,1]   
        Lighter=BorderLight_mz
        Heavier=BorderHeavy_mz
        if Heavier<Lighter:
            Heavier=BorderLight_mz
            Lighter=BorderHeavy_mz            
        ValleyLoc=np.where((spectra[:,0]>Lighter)&(spectra[:,0]<Heavier))[0]  
        ValleyBordersUpdate(ValleyLoc=ValleyLoc,spectra=spectra,Centroids=Centroids,centroidLoc=centroidLoc)    
