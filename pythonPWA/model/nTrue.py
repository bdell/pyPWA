import numpy
from pythonPWA.model.complexV import complexV

def nTrue(resonances,waves,mass,normint):
    """
    Returns the number of events for all resonances and waves for the specified mass and normalization integral.
    """
    ret=0.
    for resonance1 in resonances:
        for resonance2 in resonances:
            for wave1 in waves:
                for wave2 in waves:
                    v1=complexV(resonance1,wave1,waves,normint,mass)
                    v2=numpy.conjugate(complexV(resonance2,wave2,waves,normint,mass))
                    psi=normint[wave1.epsilon,wave2.epsilon,waves.index(wave1),waves.index(wave2)]
                    term=v1*v2*psi
                    ret+=term
    return ret.real

def nTrueForWave(resonances,waves,wave,mass,normint):
    """
    Returns the number of events for all resonances, for a specified wave out of the set of all waves, for the specified mass,
    and for the nomalization integral.
    """
    ret=0.
    for resonance1 in resonances:
        for resonance2 in resonances:
            v1=complexV(resonance1,wave,waves,normint,mass)
            v2=numpy.conjugate(complexV(resonance2,wave,waves,normint,mass))
            psi=normint[wave.epsilon,wave.epsilon,waves.index(wave),waves.index(wave)]
            term=v1*v2*psi
            ret+=term
    return ret.real
    
    
def nTrueForFixedV1V2(vList,waves,normint):
    """
    calculates the number of events for fitted v1 and v2 values.
    """
    ret=0.
    for wave1 in waves:
        for wave2 in waves:
            psi=normint[wave1.epsilon,wave2.epsilon,waves.index(wave1),waves.index(wave2)]
            ret+=vList[waves.index(wave1)]*numpy.conjugate(vList[waves.index(wave2)])*psi
    return ret.real
    
def nTrueForFixedV1V2AndWave(v,waves,wave,normint):
    """
    calculates the number of events for fitted v1 and v2 values for a specific
    wave.
    """
    return v*numpy.conjugate(v)*normint[wave.epsilon,wave.epsilon,waves.index(wave),waves.index(wave)]
    