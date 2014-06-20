class gampEvent():
    """
    This class represents a single gamp event.  That is to say that
    this class contains a set of particles and a flag to specify if
    this event is accepted into the filtered data set.
    """
    def __init__(self,
                 particles=[],
                 accepted=None,
                 raw=None):
        
        self.particles=particles
        self.raw=raw
        self.accepted=accepted
        
    def writeGamp(self,outputFile):
        outputFile.write(str(len(self.particles))+"\n")
        for particle in self.particles:
            outputFile.write(particle.toString())

    def writeGampIfAccepted(self,outputFile):
        if self.accepted==True:
            self.writeGamp(outputFile)