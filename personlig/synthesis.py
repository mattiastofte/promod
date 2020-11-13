from pylab import *
from scipy import *
from scipy import signal
from scipy.io import wavfile
from playsound import playsound

from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

def square(frequency,x,n,amplitude):
    factor_sum = 0
    for i in range(1,n+1):
        print(i)
        factor_sum += (np.sin(2*np.pi*(((2*(i)))-1)*frequency*x))/((2*(i))-1)
    y = amplitude*(np.pi/4)*factor_sum
    return y

# variablees
samplerate = 44100
length = 1
total_samples = samplerate*length
amplitude = 0.05

# x linspace for graphs
x = np.linspace(0,length, total_samples)
carrier = np.sin(2 * np.pi * 440 * 2 * x)
frequency_modulation = (((np.sin(2 * np.pi * 4 *x))*10)+np.sin(2 * np.pi * 2 *x))+440
frequency_modulation_2 = (signal.sawtooth(2 * np.pi * 2 * x)*20)+440
square = (signal.square(2 * np.pi * frequency_modulation * x)+np.sin(2 * np.pi * frequency_modulation * 2 * x)+np.sin(2 * np.pi * frequency_modulation_2))*amplitude
audio = (1 + (carrier))*square


plot(x,audio)
plot(x,frequency_modulation)
plot(x,square)
plot(x,carrier)
xlim((0,0.01))
show()
audio = np.append(audio,np.zeros(44100))

delay = 500 # In miliseconds
delaySamples = delay*samplerate
decay = 0.5

from librosa import load
audio, sr = load(infile, sr=None)
audio = fx(audio)

wavfile.write('ouptput.wav', 44100, audio)


# tenkte å lage ett mini musikk program 
# men det ble for vanskelig :(
# nå driver jeg bare å fucker rundt og 
# lager lydbølger med square waves (fourier series)