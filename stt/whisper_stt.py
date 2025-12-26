import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import winsound
import time
import os

model = whisper.load_model("base")

def beep():
    winsound.Beep(1200, 200)

def record_audio(duration=3, fs=16000):
    beep()
    time.sleep(0.2)
    print("🎤 Listening...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp.name, fs, recording)

    return temp.name


# ✅ THIS FUNCTION MUST EXIST
def speech_to_text():
    audio_path = record_audio()

    try:
        result = model.transcribe(
            audio_path,
            language="en",
            fp16=False,
            condition_on_previous_text=False,
            temperature=0.0,
            no_speech_threshold=0.6
        )

        text = result.get("text", "").strip()
        print("📝 Transcribed:", text)
        return text

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)
