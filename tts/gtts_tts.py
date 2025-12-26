from gtts import gTTS
import sounddevice as sd
import soundfile as sf


def speak(text, lang="mr"):
    """
    Generates TTS and plays it internally (NO VLC).
    """
    filename = "tts.wav"

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    data, fs = sf.read(filename, dtype="float32")
    sd.play(data, fs)
    sd.wait()
