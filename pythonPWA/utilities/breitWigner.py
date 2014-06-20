import numpy

def breitWigner(mass,resMass,gamma):
    """
    Returns numpy.complex data type representing the Briet Wigner function for a given
    mass, resonance mass, and resonance width.  Note that here, it assumes a fixed
    resonance width.
    """
    dr=mass-resMass
    denom=dr*dr+gamma*gamma/4.
    return numpy.complex(dr*gamma/(2.*denom),gamma*gamma/(denom*4.))