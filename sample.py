"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
This is the callback (non-blocking) version.
"""
import pyaudio
import time
import numpy as np

WIDTH = 2
CHANNELS = 2
RATE = 44100
CHUNK = 2 ** 10
p = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    return in_data, pyaudio.paContinue


stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)
stream.start_stream()
print("start")
while stream.is_active():
    print("running...")
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    print(int(np.average(np.abs(data))))
    time.sleep(0.1)
stream.stop_stream()
stream.close()
p.terminate()
