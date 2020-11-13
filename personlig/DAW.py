from pylab import *
from scipy import *
from scipy import signal
from scipy.io import wavfile
from playsound import playsound

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

# layers
midi = []
for i in range(1,total_samples):
    if i > 20000:
        midi.append((128,20))
layer_1 = [(0,midi)]

# x linspace for graphs

x = np.linspace(0,length, samplerate*length)

audio = np.linspace(0,0, samplerate*length)

square_wave = square(440,np.linspace(0,0.2,int(samplerate*0.2)),1000,0.1)
layer_1 = array([])

for i in range(1,total_samples):


layer_1.resize(audio.shape)
audio = audio + layer_1


plot(x,audio)
xlim((0,0.01))
show()

wavfile.write('ouptput.wav', samplerate, audio)


# tenkte å lage ett mini musikk program 
# men det ble for vanskelig :(
# nå driver jeg bare å fucker rundt og 
# lager lydbølger med square waves (fourier series)