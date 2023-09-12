def ValleyBordersUpdate(ValleyLoc,spectra,Centroids,centroidLoc):
    if len(ValleyLoc)>0:
        Valley=spectra[ValleyLoc,:]
        MinInt=np.min(Valley[:,1])
        MinValleyLoc=np.where(Valley[:,1]==MinInt)[0]
        LocBorderLight_mz=MinValleyLoc[0]
        LocBorderHeavy_mz=MinValleyLoc[-1]
        BorderLight_mz=Valley[LocBorderLight_mz,0]
        BorderHeavy_mz=Valley[LocBorderHeavy_mz,0]
        Centroids[centroidLoc-1,2]=BorderLight_mz
        Centroids[centroidLoc,1]=BorderHeavy_mz   
