import numpy

def spinDensity(beampolarization,alpha):
    """
    Returns the entire spinDensity matrix for specified beam polarization and angle alpha.
    Note that the spinDensity matrix is a 2x2 matrix indexed by the wave reflectivity (wave.epsilon).
    """
    #TODO: need to make this check the type of alpha, if its type is none then return [[.5,0.],[0.,.5]]
    complexrhomatrix=numpy.empty((2,2),dtype=numpy.complex)
    complexrhomatrix[0,0]=numpy.complex(1.+beampolarization*numpy.cos(2.*alpha),0.)
    complexrhomatrix[0,1]=numpy.complex(0.,beampolarization*numpy.sin(2.*alpha))
    complexrhomatrix[1,0]=numpy.complex(0.,-1.*beampolarization*numpy.sin(2.*alpha))
    complexrhomatrix[1,1]=numpy.complex(1.-beampolarization*numpy.cos(2.*alpha),0.)
    return .5*complexrhomatrix