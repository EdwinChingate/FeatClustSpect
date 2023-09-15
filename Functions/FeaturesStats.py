import numpy as np
def FeaturesStats(Signals):
    SumIntens=sum(Signals[:,1])
    RelativeInt=Signals[:,1]/SumIntens
    AverageMZ=sum(Signals[:,0]*RelativeInt)
    l=len(Signals[:,1])    
    VarianMZ=sum(RelativeInt*(Signals[:,0]-AverageMZ)**2)*l/(l-1)  
    StdMZ=np.sqrt(VarianMZ)
    featuresStats=[AverageMZ,StdMZ,SumIntens]    
    return featuresStats
