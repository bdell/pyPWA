import re
import itertools as it
import os

from pythonPWA.dataTypes.wave import wave
from pythonPWA.fileHandlers.bampReader import readBamp

def getwaves(totalpath):
    """
    This function finds and reads in all bamp files in the provided directory an
d returns
    a list of all waves of type pwawave.wave after populating the needed data me
mbers of
    each member.
    """
    wavelist=[]
    #filtering for bamp file types and populating bamplist
    regexp=re.compile(".*(.bamp).*")
    for files in os.listdir(totalpath):
        if regexp.search(files):
            #setting the beta value for the wave
            idex=files.find(".bamp")
            
            #setting the waves epsilon value
            for b in range(len(files)):
                if files[-int(b)] == '-':
                    epsilon=0 
                    break
                if files[-int(b)] == '+':
                    epsilon=1 
                    break
            wavelist.append(wave(epsilon=epsilon,complexamplitudes=readBamp(os.path.join(totalpath,files))))
    return wavelist

