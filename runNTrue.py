import numpy
import os

from pythonPWA.dataTypes.resonance import resonance
from pythonPWA.fileHandlers.getWavesGen import getwaves
from pythonPWA.model.normInt import normInt
from pythonPWA.model.intensity import intensity
from pythonPWA.fileHandlers.gampReader import gampReader
from pythonPWA.utilities.dataSimulator import dataSimulator
from pythonPWA.model.nTrue import nTrueForFixedV1V2 as ntrue
from pythonPWA.model.nTrue import nTrueForFixedV1V2AndWave as ntrueforwave

dataDir=os.path.join("/","home","salgado","pkk","data","1000pd_MeV")
print"working with dataDir=",dataDir
    
waves=getwaves(dataDir)
print"loaded",len(waves),"waves"

accNormInt=numpy.load(os.path.join(dataDir,"mc","normint.npy"))

v1=numpy.complex(-0.1759968798932109,-0.06703609562678432)

v2=numpy.complex(0.056361107762924675,-0.1377034355817562)

print"nTrue:", ntrue([v1,v2],waves,accNormInt)

vList=[v1,v2]

nTrueList=[]

for wave in waves:
    print"for wave",waves.index(wave),"ntrue=",ntrueforwave(vList[waves.index(wave)],waves,wave,accNormInt)
    nTrueList.append(ntrueforwave(vList[waves.index(wave)],waves,wave,accNormInt))
    
print"wave0/wave1=",nTrueList[0]/nTrueList[1]