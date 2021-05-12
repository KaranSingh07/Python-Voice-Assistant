from gtts import gTTS   # Google Text To Speech (gTTS) Library
import playsound


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


print("Speaking...")
speak("Hello Karan")
