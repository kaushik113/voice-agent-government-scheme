from stt.whisper_stt import speech_to_text
from tts.gtts_tts import speak

def ask_via_voice(prompt_marathi):
    # SPEAK the prompt (voice-first)
    speak(prompt_marathi)

    # Optional: also print for debugging
    print(prompt_marathi)

    # Listen for user response
    text = speech_to_text()
    return text.strip()
