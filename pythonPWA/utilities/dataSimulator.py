from random import random

from pythonPWA.fileHandlers.gampReader import gampReader
from pythonPWA.model.intensity import intensity


class dataSimulator(object):
    """description of class"""
    def __init__(self,
                 mass=1010.,
                 waves=[],
                 resonances=[],
                 normint=None,
                 productionAmplitudes=[],
                 alphaList=[],
                 beamPolarization=.4):
        
        self.mass=mass
        self.waves=waves
        self.resonances=resonances
        self.normint=normint
        self.productionAmplitudes=productionAmplitudes
        self.alphaList=alphaList
        self.beamPolarization=beamPolarization

        self.intensity=intensity(resonances=self.resonances,waves=self.waves,productionAmplitudes=self.productionAmplitudes,normint=self.normint,alphaList=self.alphaList,beamPolarization=self.beamPolarization)

    def execute(self,inputGampFile,outputRawGampFile,outputAccGampFile,inputPfFile):
        #print"beggining simulation"
        igreader=gampReader(gampFile=inputGampFile)
        inputGampEvents=igreader.readGamp()
        #lastPercent=0.
        #calculate intensity
        #print"calculating intensity"
        
        iList=[]
        iMax=0.

        #d=float(len(self.alphaList))

        for event in range(len(self.alphaList)):
        #for event in range(10):
            
            #if (float(event)/d)*100.-lastPercent>1.: 
            #    print"intensity:",(float(event)/d)*100.,"%"
            #    lastPercent=(float(event)/d)*100.
            i=self.intensity.calculate(self.mass,event)
            if i>iMax:
                iMax=i
            iList.append(i)
        #lastPercent=0.
        #calculate wn
        #print"calculating weights"
        wList=[]
        #a=float(len(self.alphaList))
        for weight in range(len(self.alphaList)):
            #if (float(weight)/a)*100. -lastPercent > 1.:
            #    print "weight calc:",(float(weight)/a)*100.,"%"
            #    lastPercent=(float(weight)/a)*100.
            wList.append(iList[weight]/iMax)
        
        #lastPercent=0.
        #b=float(len(wList))
        rawGampEvents=[]
        #if wn>random keep gampEvents[eventNumber]
        for wn in range(len(wList)):
            #if (float(wn)/b)*100. -lastPercent > 1.:
            #    print"random filter:",(float(wn)/b)*100.,"%"
            #    lastPercent=(float(wn)/b)*100.
            
            if wList[wn]>random(): #random()=random float on [0.0, 1.0)
                #print"writing event",wn,"to",outputRawGampFile.name
                inputGampEvents[wn].raw=True
                #inputGampEvents[wn].writeGamp(outputRawGampFile)
                rawGampEvents.append(inputGampEvents[wn])
        
        for rawGamps in rawGampEvents:
            rawGamps.writeGamp(outputRawGampFile)

        #lastPercent=0.
        #c=float(len(inputGampEvents))
        
        #acceptedGampEvents=[]
        
        #passing through acceptance filter
        #print"passing all events through acceptance filter"
        
        #pfList=inputPfFile.readlines()
        #for gEvents in inputGampEvents:
            #index=inputGampEvents.index(gEvents)
            
            #if (float(index)/c)*100. - lastPercent > 1.:
            #    print"acc filter:",(float(index)/c)*100.,"%"
            #    lastPercent=(float(index)/c)*100.
            
            #accFlag=int(pfList[index].strip("\n"))
            
            #print type(accFlag)
            #print gEvents.raw
            
            #if (accFlag==1 and gEvents.raw==True):
                
                #print"writing event",index,"to",outputAccGampFile.name
                
                #gEvents.writeGamp(outputAccGampFile)
                #acceptedGampEvents.append(gEvents)
            #if (accFlag!=1 or gEvents.raw!=True):
                #acceptedGampEvents.append(None)
        outputRawGampFile.close()
        outputAccGampFile.close()
        

        #print"finished"
        #return inputGampEvents,rawGampEvents,acceptedGampEvents
        