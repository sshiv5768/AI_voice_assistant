import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    # Using google text to speech module for accepting text and converting into speech
    tts = gTTS(text=text, lang="en")
    # Converting text into mp3 format
    filename = "voice.mp3"
    tts.save(filename)
    # Using playsound module for playing sound
    playsound.playsound(filename)


speak("Hello World!")
