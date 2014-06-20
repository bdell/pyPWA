from pythonPWA.utilities.chunks import chunks
from pythonPWA.utilities.likelihood import likelihood
import numpy
from math import log

import numpy
from math import log 
from pythonPWA.model.complexV import complexV
from pythonPWA.model.spinDensity import spinDensity
from pythonPWA.model.intensity import intensity
from random import random

import os

class minuitLikelihood(object):
    """description of class"""
    def __init__(self,
 #                resonances=[],
                 waves=[],
                 productionAmplitudes=[],
                 normint=None,
                 alphaList=[],
                 beamPolarization=.4,
                 mass=1010.,
                 eventNumber=7540,
                 acceptedPath=os.getcwd(),
                 generatedPath=os.getcwd(),
                 accAlphaList=[],
                 accNormInt=None,
                 rawAlphaList=[],
                 rawNormInt=None
                 ):
        
#        self.resonances=resonances
        self.waves=waves
        self.productionAmplitudes=productionAmplitudes
        self.normint=normint
        self.alphaList=alphaList
        self.beamPolarization=beamPolarization
        self.mass=mass
        self.eventNumber=len(self.alphaList)
        self.acceptedPath=acceptedPath
        self.generatedPath=generatedPath
        self.debugPrinting=0
        self.iList=[]
        self.accAlphaList=accAlphaList
        self.accNormInt=accNormInt
        self.rawAlphaList=rawAlphaList
        self.rawNormInt=rawNormInt
        

    def calclogI(self):
        ret=numpy.complex(0.,0.)
        for n in range(0,len(self.alphaList)-1,1):    
            argret=numpy.complex(0.,0.)            
            for wave1 in self.waves:
                for wave2 in self.waves:
                    if len(self.productionAmplitudes)!=0:
                                #logarithmic domain error
                        arg = self.productionAmplitudes[self.waves.index(wave1)]*numpy.conjugate(self.productionAmplitudes[self.waves.index(wave2)])*wave1.complexamplitudes[n]*numpy.conjugate(wave2.complexamplitudes[n])*spinDensity(self.beamPolarization,self.alphaList[n])[wave1.epsilon,wave2.epsilon]
                        argret+=arg
            if self.debugPrinting==1:                        
                print"loop#",n,"="*10
                print"argval:",arg
                print"argtype:",type(arg)
                print"productionAmps1:",self.productionAmplitudes[self.waves.index(wave1)]
                print"productionAmps2*:",numpy.conjugate(self.productionAmplitudes[self.waves.index(wave2)])
                print"spinDensityValue:",spinDensity(self.beamPolarization,self.alphaList[n])[wave1.epsilon,wave2.epsilon]
                print"A1:",wave1.complexamplitudes[n]                        
                print"A2*:",numpy.conjugate(wave2.complexamplitudes[n])
            if argret > 0.:                        
                ret+=log(argret)
            
            self.iList.append(argret)                           
        return ret

    def countAlphas(self,path):
        Alpha = open(path,'r')
        AlphaList = Alpha.readlines()
        
        return len(AlphaList)                        
    
    #This calculates Eta x                         
    def etaX(self):
        etax=(self.countAlphas(self.acceptedPath)/self.countAlphas(self.generatedPath))
 #       print "etax:",etax        
        return etax 


    #This calculates only the sums in the right term
    def calcSigmaN(self):
        reN=numpy.complex(0,0)
        for wave1 in self.waves:
            for wave2 in self.waves:
                if len(self.productionAmplitudes)!=0:
                    #print"for wave index:",self.waves.index(wave1),"\nV=",self.productionAmplitudes[self.waves.index(wave1)]
                    reN+=self.productionAmplitudes[self.waves.index(wave1)]*numpy.conjugate(self.productionAmplitudes[self.waves.index(wave2)])*self.accNormInt[wave1.epsilon,wave2.epsilon,self.waves.index(wave1),self.waves.index(wave2)]
        return reN                   
    
    #This multiplies Eta and the sums to make the entire N/right term                        
    def calcN(self):
        return self.etaX() * self.calcSigmaN()
            
    #This adds the left and right terms to make the log likelihood.         
    def calcneglnL(self,wave1Re,wave1Im,wave2Re,wave2Im):
        #this needs to be generalizable to n number of waves, not just 2
        self.productionAmplitudes=[numpy.complex(wave1Re,wave1Im),numpy.complex(wave2Re,wave2Im)]
        LLog =  -(self.calclogI()) + self.calcN()      
        print LLog        
        return LLog