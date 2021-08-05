import struct
import numpy as np
import pyaudio
import matplotlib.pyplot as plt

#%matplotlib tk

p = pyaudio.PyAudio()

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = int(p.get_device_info_by_index(0)['defaultSampleRate'])


stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

data = stream.read(CHUNK, exception_on_overflow=False)
print(data)

# data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

# fig, ax = plt.subplots()
# ax.plot(data_int, '-')

# plt.show()

# def ProcessAudioData():
#     pass

