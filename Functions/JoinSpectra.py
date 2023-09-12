import numpy as np
def JoinSpectra(IDvec,DataSet,FirstID,LastID,minInt=2e5):
    ShortIDlistLoc=np.where((IDvec>=FirstID)&(IDvec<=LastID))[0]
    firstSpectrum=True
    for ids in ShortIDlistLoc:
        ID=int(IDvec[ids])
        spectrum0=np.array(DataSet[ID].get_peaks()).T
        RT=DataSet[ID].getRT()
        spectrumLoc=np.where(spectrum0[:,1]>minInt)[0]
        spectrumWoRT=spectrum0[spectrumLoc,:]
        spectrum=np.c_[spectrumWoRT,RT*np.ones(len(spectrumWoRT))]
        if firstSpectrum:
            Spectrum=spectrum
            firstSpectrum=False
        else:
            Spectrum=np.r_[Spectrum,spectrum]
    return Spectrum
