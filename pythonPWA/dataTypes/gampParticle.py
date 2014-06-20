class gampParticle():
    """
    This class represents a particle described in a single line of a 
    .gamp file.
    """
    def __init__(self,
                 particleID=None,
                 particleCharge=None,
                 particleXMomentum=None,
                 particleYMomentum=None,
                 particleZMomentum=None,
                 particleE=None):

        self.particleID=particleID
        self.particleCharge=particleCharge
        self.particleXMomentum=particleXMomentum
        self.particleYMomentum=particleYMomentum
        self.particleZMomentum=particleZMomentum
        self.particleE=particleE
    
    def toString(self):
        """
        Returns a string of the particle data members delimited by newlines.
        """
        return " ".join([str(self.particleID),str(self.particleCharge),str(self.particleXMomentum),str(self.particleYMomentum),str(self.particleZMomentum),str(self.particleE)])