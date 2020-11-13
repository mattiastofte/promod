from pylab import *
from scipy import *
from scipy import signal
from scipy.io import wavfile
import sounddevice as sd
import numpy as np
import random
import time

duration = 5.5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = (-1 + random.random()*2)*0.4

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))