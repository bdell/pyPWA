import threading

class dataSimulatorThread(threading.Thread):
    """A Single Thread used to allow for parallel processing of mass bins."""
    def __init__(self,
                 mass=1010.,
                 waves=[],
                 resonances=[],
                 normint=None,
                 productionAmplitudes=[],
                 alphaList=[],
                 beamPolarization=.4,
                 inputGampEvents=[],
                 pfList=[]):
        
        self.mass=mass
        self.waves=waves
        self.resonances=resonances
        self.normint=normint
        self.productionAmplitudes=productionAmplitudes
        self.alphaList=alphaList
        self.beamPolarization=beamPolarization

        self.intensity=intensity(resonances=self.resonances,waves=self.waves,productionAmplitudes=self.productionAmplitudes,normint=self.normint,alphaList=self.alphaList,beamPolarization=self.beamPolarization)

        self.inputGampEvents=inputGampEvents
        self.pfList=pfList

        self.iList=[]
        self.wList=[]
        self.rawGampEvents=[]
        self.acceptedGampEvents=[]
        

    def run(self,inputGampEvents,pfList):
        """
        formerly execute
        """

        #calculating intensity and storing maximum.
        iMax=0.
        for event in range(len(self.alphaList)):
            i=self.intensity.calculate(self.mass,event)
            if i>iMax:
                iMax=i
            self.iList.append(i)

        #calculating weights
        for weight in range(len(self.alphaList)):
            self.wList.append(iList[weight]/iMax)
        
        #if wn>random keep gampEvents[eventNumber]
        for wn in range(len(self.wList)):
            r=random()
            if self.wList[wn]>r:
                inputGampEvents[wn].raw=True
                self.rawGampEvents.append(inputGampEvents[wn])
        
        #for all input gamp events, if the matching entry in the pflist and the gamp event is in the "raw" list, then we add it to the accepted list.
        for gEvents in inputGampEvents:
            index=inputGampEvents.index(gEvents)
            accFlag=int(pfList[index].strip("\n"))
            if (accFlag==1 and gEvents.raw==True):
                self.acceptedGampEvents.append(gEvents)