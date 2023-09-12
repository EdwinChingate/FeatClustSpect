import numpy as np
#FractionCut=0.1353352832366127=np.exp(-4/2) The relative intensity after 2 standard deviation, if the signal behave normal
#I can also estimate STDGuess with other altorithm
def SpectraCentroids(spectra,SafetyFactor=4,STDGuess=5e-5):
    Centroids=[]
    featureID=0
    while True:        
        MaxInt=np.max(spectra[:,1])
        if MaxInt==0:       
            break
        Loc=np.where(spectra[:,1]==MaxInt)[0][0]
        mz=spectra[Loc,0]
        LightBorder_mz=mz-SafetyFactor*STDGuess
        HeavyBorder_mz=mz+SafetyFactor*STDGuess
        PeakLoc=np.where((spectra[:,0]>LightBorder_mz)&(spectra[:,0]<HeavyBorder_mz))[0]
        spectra[PeakLoc,1]=0  
        centroid=[mz,LightBorder_mz,HeavyBorder_mz,featureID,0,1]
        featureID+=1
        Centroids.append(centroid)
    NPCentroids=np.array(Centroids)
    CentroidsLoc=np.argsort(NPCentroids[:,0])
    return NPCentroids[CentroidsLoc,:]
