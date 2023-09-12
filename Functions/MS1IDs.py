import numpy as np
#Retrive RT as well
def MS1IDs(DataSet):
    IDvec=[]
    c=0
    for SpectralSignals in DataSet:
        MSLevel=SpectralSignals.getMSLevel()
        if MSLevel==1:
            IDvec.append(c)
        c+=1
    IDvec=np.array(IDvec,dtype=int)
    return IDvec
