#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st
import base64

translator = Translator()
lang_code = st.text_input("Please, type a 2-letter language code, for the destination language")
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
  translate = translator.translate(uploaded_file.getvalue().decode("utf-8"), dest=lang_code) 
  tts1=gTTS(text=translate.text, lang=lang_code)
  tts1.save('file.mp3')

  audio_file = open("file.mp3", "rb")
  
  

  mymidia_placeholder = st.empty()

  mymidia_str = "data:audio/ogg;base64,%s"%(base64.b64encode(audio_file).decode())
  mymidia_html = """
                <audio autoplay class="stAudio">
                <source src="%s" type="audio/ogg">
                Your browser does not support the audio element.
                </audio>
            """%mymidia_str

  mymidia_placeholder.empty()
  time.sleep(1)
  mymidia_placeholder.markdown(mymidia_html, unsafe_allow_html=True)
