import scipy.io.wavfile as wavfile
import wave
import numpy as np
import struct
import math

wav = wave.open("in10.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
content = wav.readframes(nframes)

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

samples = np.fromstring(content, dtype=types[sampwidth])

data = samples[0::nchannels]


dest = wave.open("out2.wav", mode="wb")
dest.setparams(wav.getparams())


newdata = samples[::-1]
print(newdata)

newframes = struct.pack('<' + str(len(newdata)) + 'h', *newdata)
# записываем содержимое в преобразованный файл.
dest.writeframes(newframes)
wav.close()
dest.close()