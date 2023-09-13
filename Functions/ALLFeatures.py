import numpy as np
def ALLFeatures(Centroids,allFeatures=[]):
    NCent=len(Centroids)
    NFeat=len(allFeatures)
    for feat in np.arange(NFeat,NCent):
        allFeatures.append([])
    return allFeatures 
