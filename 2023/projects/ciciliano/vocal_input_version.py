import speech_recognition as sr
import pyttsx3
import pyaudio
import tkinter as tk

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            text = text.lower()
        except sr.UnknownValueError:
            text = 'Something went wrong, sorry :('
        except sr.RequestError:
            text = 'Something went wrong, sorry :('
    return text
