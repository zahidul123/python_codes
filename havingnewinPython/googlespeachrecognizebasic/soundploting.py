import matplotlib.pyplot as plt
import wave
import numpy as np
import sys

data=wave.open("F:\havingnewinPython\googlespeachrecognizebasic\chunk1.wav","r")
signal=data.readframes(-2)
signal=np.fromstring(signal,"Int16")
plt.plot(signal)
plt.title("wave are ploting")
plt.show()


#Split the data into channels
channels = [[] for channel in range(data.getnchannels())]

for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)
#Get time from indices
fs = data.getframerate()
Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

plt.title('Signal Wave...')
for channel in channels:
    plt.plot(Time,channel)
plt.show()


channels=np.array(channels)

channels=[abs(i) for i in channels if(abs(i)>1000).any()]
print(channels)
plt.title("afterspliting")
plt.plot(channels)
plt.show()