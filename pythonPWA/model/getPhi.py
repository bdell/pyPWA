import numpy

def getPhi(mass,resonance):
    """
    Returns the value of Phi used in complex production amplitude calculation, and thus
    number of events (nTrue.nTrue()), for a specified mass and resonance.
    """
    return numpy.arctan((resonance.r0*resonance.w0)/(mass**2-resonance.w0**2)) #need to make this arccotan? invert args