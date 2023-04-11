#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st
import time

translator = Translator()
lang_code = st.text_input("Please, type a 2-letter language code, for the destination language")
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
  translate = translator.translate(uploaded_file.getvalue().decode("utf-8"), dest=lang_code) 
  tts1=gTTS(text=translate.text, lang=lang_code)
  tts1.save('file.mp3')

  audio_file = open("file.mp3", "rb")
  
  


  html_string = """
            <audio controls autoplay>
              <source src="./file.mp3" type="audio/mp3">
            </audio>
            """

  sound = st.empty()
  sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
  time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
  #sound.empty()  # optionally delete the element afterwards
