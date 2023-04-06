#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st

translator = Translator()
lang_code = st.text_input("Please, type a 2-letter language code, for the destination language")
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
  translate = translator.translate(uploaded_file, dest=lang_code) 
  tts1=gTTS(text=translate.text, lang=lang_code)
  tts1.save('file.mp3')

  audio_file = open("file.mp3", "rb")
  st.audio(data=audio_file, format="audio/mp3", start_time=0)
  
  st.download_button(label="Download", data=audio_file, file_name='file.mp3',mime='audio/mp3')
