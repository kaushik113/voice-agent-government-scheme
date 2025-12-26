import numpy as np
import sounddevice as sd

def play_beep(duration=0.25, freq=1000, fs=16000):
    """
    Plays a short beep sound before recording.
    """
    t = np.linspace(0, duration, int(fs * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)
    sd.play(tone, fs)
    sd.wait()
