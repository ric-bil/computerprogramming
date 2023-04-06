#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st


translator = Translator()
word = st.input("Please, insert a word/sentence\t")
lang_code = st.input("Please, type a 2-letter language code, for the destination language ")
translate = translator.translate(word, dest=lang_code) 
tts1=gTTS(text=translate.text, lang=lang_code)
tts1.save('file.mp3')

audio_file = open("file.mp3", "rb")
st.audio(data=audio_file, format="audio/mp3", start_time=0)
