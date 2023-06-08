import tkinter as tk
from tkinter import ttk
import explorerhat
import pyttsx3

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



gui = tk.Tk()
gui.geometry('800x400')
gui.title('Unibz Chatbot')
gui.configure(bg='#2c4557')
enter = tk.Entry(gui)
switch_on = ttk.Button(gui, text= 'on', command = red_on)
switch_on.place(x=710,y=10)
switch_off = ttk.Button(gui, text= 'off', command = red_off)
switch_off.place(x=710,y=350)

gui.mainloop()
