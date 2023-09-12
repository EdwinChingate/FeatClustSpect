import numpy as np
def FeaturesData(Centroids,spectra,allFeatures):
    NCent=len(Centroids)    
    for centroidLoc in np.arange(NCent,dtype='int'):    
        PeaksLoc=np.where((spectra[:,0]>Centroids[centroidLoc,1])&(spectra[:,0]<Centroids[centroidLoc,2]))[0]
        Peaks=spectra[PeaksLoc,:]
        featureID=int(Centroids[centroidLoc,3])
        if len(allFeatures[featureID])==0:
            allFeatures[featureID]=Peaks
        else:
            allFeatures[featureID]=np.append(allFeatures[featuresID],Peaks,axis=0)
