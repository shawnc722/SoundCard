import sc
import time

with sc.get_microphone(sc.default_speaker().name).recorder(samplerate=48000) as mic:
    while True:
        data = mic.record(numframes=48000)
