class wave():
    """
    This class represents a PWA wave.
    """
    def __init__(self,
                 epsilon=0,
                 complexamplitudes=[],
                 w0=1000.,
                 r0=100.,
                 beta=0,
                 k=0):
        
        #reflectivity
        self.epsilon=epsilon

        #amplitudes for each event
        self.complexamplitudes=complexamplitudes
        
        self.beta=beta
        
        self.k=k

    def toString(self):
        """
        returns a string of all the wave properties delimited by newlines.
        """
        return "\n".join(["epsilon="+str(self.epsilon),"len(complexamplitudes)="+str(len(self.complexamplitudes)),"beta="+str(self.beta),"k="+str(self.k)])