import random

def randm(low,high):
    """
    Returns a random value, used in generatePureWave.
    """
    return ((high-low)*random.random()+low)