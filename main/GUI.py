import struct
import numpy as np
import pyaudio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

CHUNK = 1024 * 4

def ProcessAudioData():
    p = pyaudio.PyAudio()

    stream = p.open(
        rate=44100,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )

    fig,ax = plt.subplots()
    x = np.arange(0,2*CHUNK,2)
    line, = ax.plot(x, np.random.rand(CHUNK),'r')
    ax.set_ylim(-60000,60000)
    ax.ser_xlim = (0,CHUNK)
    fig.show()

    while True:
        data = stream.read(CHUNK)
        dataInt = struct.unpack(str(CHUNK) + 'h', data)
        line.set_ydata(dataInt)
        fig.canvas.draw()
        fig.canvas.flush_events()


ProcessAudioData()