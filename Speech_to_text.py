import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import Text_to_speech


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: ", Text_to_speech.speak("Error Generated"))

    return said


get_audio()