#demodulate workfile: 6.02 PS 4,5,6
import numpy
import sendrecv
import math

def avgfilter(samples_in, window):
    x = numpy.empty_like(samples_in, dtype=float)
    for i in range(len(x)):
        if i + window > len(x):
            x[i] = float(sum(samples_in[i:]))/len(samples_in[i:])
        else:
            x[i] = float(sum(samples_in[i:i+window]))/window
    return x


def lpfilter(samples_in, omega_cut):
    raise NotImplementedError("lpfilter")

def envelope_demodulator(samples, sample_rate, carrier_freq, spb):
    raise NotImplementedError("envelope_demodulator")

def avg_demodulator(samples, sample_rate, carrier_freq, spb):
    window = (sample_rate/carrier_freq)/2
    abs_samples = [abs(i) for i in samples]
    return avgfilter(abs_samples, window)
    

def quad_demodulator(samples, sample_rate, carrier_freq, spb, channel_gap = 500):
    raise NotImplementedError("avg_demodulator")

