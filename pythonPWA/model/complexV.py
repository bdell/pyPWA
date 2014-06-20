import numpy
from pythonPWA.model.magV import magV
from pythonPWA.model.getPhi import getPhi

def complexV(resonance,wave,waves,normint,mass):
    """
    Returns the complex value of the production amplitude for a resonance, wave in the set of waves, normalization integral, and mass.
    """
    return numpy.complex(magV(mass,resonance,wave,waves,normint)*numpy.cos(getPhi(mass,resonance)+resonance.phase),magV(mass,resonance,wave,waves,normint)*numpy.sin(getPhi(mass,resonance)+resonance.phase))
    #return numpy.complex(magV(mass,resonance,wave,waves,normint)*(resonance.w0**2-mass**2)/(resonance.w0**2),magV(mass,resonance,wave,waves,normint)*(resonance.w0*resonance.r0)/(resonance.w0**2))