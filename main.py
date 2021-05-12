from gtts import gTTS   # Google Text To Speech (gTTS) Library
import playsound


def speak(text):
    tts = gTTS(text=text, lang="en")    # Converted the text to speech
    filename = "voice.mp3"              # Just a filename, could be anything
    tts.save(filename)                  # Saving that converted speech
    playsound.playsound(filename)       # Playing with playsound (it just plays an audio file)


print("Speaking....")
speak("Hello Karan")
