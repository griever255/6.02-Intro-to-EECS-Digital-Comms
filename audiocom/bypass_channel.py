import math
import numpy
import matplotlib.pyplot as p
import graphs
import random

class BypassChannel:
    def __init__(self, noise, lag, h):
        self.noise = noise
        self.lag = lag
        self.h = h
        #DO NOT modify the following lines.
        numpy.random.seed()
        random.seed()

    def xmit_and_recv(self, tx_samples):
        noise_array = numpy.random.normal(0, self.noise**(1/2), tx_samples.shape)
        return tx_samples + noise_array
