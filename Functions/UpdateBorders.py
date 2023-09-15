import numpy as np
from FeaturesStats import *
def UpdateBorders(Centroids,allFeatures,SafetyFactor=4): #This one should also check if the borders should be updated
    NCent=len(Centroids)
    for Cfeat in np.arange(NCent,dtype='int'):
        featureID=int(Centroids[Cfeat,3])
        Signals=allFeatures[featureID]
        if len(Signals[:,0])>3:
            featuresStats=FeaturesStats(Signals=Signals)
            mz=featuresStats[0]
            mz_std=featuresStats[1]
            SumInt=featuresStats[2]
            Centroids[Cfeat,[0,1,2,4]]=[mz,mz-SafetyFactor*mz_std,mz+SafetyFactor*mz_std,SumInt]
