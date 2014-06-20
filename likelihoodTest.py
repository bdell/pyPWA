import numpy
import os

from pythonPWA.dataTypes.resonance import resonance
from pythonPWA.fileHandlers.getWavesGen import getwaves
from pythonPWA.model.normInt import normInt
from pythonPWA.model.intensity import intensity
from pythonPWA.fileHandlers.gampReader import gampReader
from pythonPWA.utilities.minuitLikelihood import minuitLikelihood

from iminuit import Minuit

dataDir=os.path.join("/home/salgado/pkk","data","1000pd_MeV")
print"working with dataDir=",dataDir

alphaList=numpy.loadtxt(os.path.join(dataDir,"alphaevents.txt"))
print"loaded alphaFile",os.path.join(dataDir,"alphaevents.txt"),"with",len(alphaList),"events"

maxNumberOfEvents=float(len(alphaList))
    
testMass=1025.
print"using testMass=",testMass

#resonances=[resonance(cR=2.*maxNumberOfEvents/3.,wR=[1.,0.],w0=1320.,r0=107.),resonance(cR=maxNumberOfEvents/3.,wR=[0.,1.],w0=1895.,r0=235.)]
#resonances=[resonance(cR=2.*maxNumberOfEvents/3.,wR=[0.,1.],w0=1320.,r0=107.),resonance(cR=maxNumberOfEvents/3.,wR=[1.,0.],w0=1895.,r0=235.)]

#print"loaded",len(resonances),"resonances"
    
waves=getwaves(dataDir)
print"loaded",len(waves),"waves"

#rInt=normInt(waves=waves,alphaList=alphaList)
normint=numpy.load(os.path.join(dataDir,"mc","normint.npy"))
accNormInt=numpy.load(os.path.join(dataDir,"mc","normint.npy"))


#THESE DIRECTORIES NEED TO BE SET
acceptedPath=os.path.join(dataDir,"mc","alphaevents.txt")
generatedPath=os.path.join(dataDir,"mc","alphaevents.txt")



#minuitLn=minuitLikelihood(resonances=resonances,waves=waves,normint=normint,alphaList=alphaList,acceptedPath=acceptedPath,generatedPath=generatedPath)
minuitLn=minuitLikelihood(waves=waves,normint=normint,alphaList=alphaList,acceptedPath=acceptedPath,generatedPath=generatedPath,accNormInt=accNormInt)

#CHANGE THESE VALUES IN ORDER TO TEST THE RESULTS OF THE CALCNEGLNL FUNCTION
#wave1Re=.1
#wave1Im=.1
#wave2Re=.1
#wave2Im=.1

#print minuitLn.calcneglnL(wave1Re,wave1Im,wave2Re,wave2Im)

#UNCOMMENT THE LINES BELOW TO TEST THE MINUIT MINIMIZATION OF THE CALCNEGLNL FUNCTION
m=Minuit(minuitLn.calcneglnL,wave1Re=0.01,wave2Re=0.01,wave1Im=-0.01,wave2Im=-0.01)#,fix_wave1Im=True,fix_wave2Im=True)
m.set_strategy(1)
m.set_up(0.5)
m.migrad(ncall=1000)
print m.values
#m.draw_profile('wave1Re')
#m.draw_profile('wave2Re')
print"done"