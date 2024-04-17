# audio_recorder.py
import sounddevice as sd
import numpy as np
import wave
import os
def record_audio():
    print("Describe your situation or desires in 20 seconds...")

    # Set the sampling frequency and duration
    fs = 44100  # 44.1 kHz
    duration =  20  # 10 minutes (in seconds)

    # Record audio
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=2, dtype=np.int16)
    sd.wait()

    # Save the recording as a WAV file
    with wave.open("recorded_audio.wav", "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())

    print("Recording saved as 'recorded_audio.wav'.")