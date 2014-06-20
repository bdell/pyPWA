import numpy

def readBamp(filename):
    """
    This is a general bamp reading function.  returns list of numpy.complexes
    representing the complex amplitudes of the wave represented by the file.
    """
    temp1=numpy.fromfile(file=filename,dtype=numpy.dtype('f8'))
    temp2=temp1.reshape((2,-1),order='F')
    temp3=[]
    for lineNumber in range(temp2.shape[1]):
        temp3.append(numpy.complex(temp2[0,lineNumber],temp2[1,lineNumber]))
    return temp3