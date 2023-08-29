import numpy as np
#FractionCut=0.1353352832366127=np.exp(-4/2) The relative intensity after 2 standard deviation, if the signal behave normal
def SpectraCentroids(spectra,MinIntKernel=3e5,SafetyFactor=4,FractionCut=0.1353):
    MaxInt=1.5*MinIntKernel
    Centroids=[]
    while MaxInt>MinIntKernel:
        MaxInt=np.max(spectra[:,1])
        Loc=np.where(spectra[:,1]==MaxInt)[0][0]
        mz=spectra[Loc,0]
        CutInt=MaxInt*FractionCut
        LocCut=np.where((spectra[:,1]<CutInt)&(spectra[:,0]>mz))[0][0] #This would be the mz 2 standard deviations at the right of the maximum
        mz2Sig=spectra[LocCut,0]
        Int2Sig=spectra[LocCut,1]
        DataFractionCut=MaxInt/Int2Sig
        SigmaDist=np.sqrt(2*np.log(DataFractionCut))
        Deltamz=mz2Sig-mz
        Sigma=Deltamz/SigmaDist
        Light_mz=mz-SafetyFactor*Sigma
        Heavy_mz=mz+SafetyFactor*Sigma
        PeakLoc=np.where((spectra[:,0]>Light_mz)&(spectra[:,0]<Heavy_mz))[0]
        spectra[PeakLoc,1]=0  
        centroid=[Light_mz,Heavy_mz]
        Centroids.append(centroid)
    return np.array(Centroids)
