import numpy
import os
from pythonPWA.model.spinDensity import spinDensity

class normInt():
    """
    Represents a normalization integral.  To compute the value of the normalization integral
    call normInt.execute().  To save the normalization integral to a directory call normInt.save()
    """
    def __init__(self,
                 waves=[],
                 alphaList=[],
                 beamPolarization=0.4):
        
        self.waves=waves
        self.alphaList=alphaList
        self.beamPolarization=beamPolarization
        
        self.ret=numpy.ndarray((2,2,len(waves),len(waves)),dtype=numpy.complex)
        self.ret[:,:,:,:]=numpy.complex(0.,0.)
    
    def execute(self):
        """
        Returns the normalization integral for the waves, alphas, and beam polarization.
        Note that the normalization integral is stored as a numpy ndarray with 4 dimensions.
        The indexing of the normalization integral is [wave1.epsilon,wave2.epsilon,waves.index(wave1),waves.index(wave2)].
        This means that the first 2 dimensions (wave1.epsilon,wave2.epsilon) have length of 2.  The last 2 dimensions
        (waves.index(wave1),waves.index(waves2)) have length equal to the number of waves to be represented in this normalization
        integral.
        """
        evnumber=0
        for alpha in self.alphaList:
            spindensity=spinDensity(self.beamPolarization,alpha)
            for wave1 in self.waves:
                for wave2 in self.waves:
                    temp=wave1.complexamplitudes[evnumber]*numpy.conj(wave2.complexamplitudes[evnumber])*spindensity[wave1.epsilon,wave2.epsilon]
                    self.ret[wave1.epsilon,wave2.epsilon,self.waves.index(wave1),self.waves.index(wave2)]+=temp
            evnumber+=1    

        return self.ret*(1./float(evnumber))

    def save(self,directory):
        """
        Saves the current value of the normalization integral.  Note that if this is called before
        normInt.execute() it will save an ndarray of complex 0's to the specified file.
        """
        numpy.save(os.path.join(directory,"normint.npy"),self.ret)
