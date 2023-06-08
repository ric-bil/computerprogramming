import tkinter as tk
import explorerhat
import pyttsx3
import speech_recognition as sr

def red_on():
        engine = pyttsx3.init()
        explorerhat.light.red.on()
        engine.say('command executed: door open')
        engine.runAndWait()

def red_off():
        engine = pyttsx3.init()
        explorerhat.light.red.off()
        engine.say('command executed: door closed')
        engine.runAndWait()

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rec.listen(source,phrase_time_limit=5)
        try:
            text = rec.recognize_google(audio,language='en-US')
            text = text.lower()
        except sr.UnknownValueError:
            text = 'something went wrong, try again'
        except sr.RequestError:
            text = 'something went wrong, try again'
    if 'closed' in text:
        red_off
    elif 'open' in text:
        red_on
    else:
        pass

gui = tk.Tk()
gui.geometry('800x400')
gui.title('Unibz Chatbot')
gui.configure(bg='blue')
enter = tk.Entry(gui)
switch_on = tk.Button(gui, text= 'Mic', command = listen)
switch_on.place(x=380,y=300)


gui.mainloop()
