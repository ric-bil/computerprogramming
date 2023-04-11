#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st
import time
import base64

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


translator = Translator()
lang_code = st.text_input("Please, type a 2-letter language code, for the destination language")
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
  translate = translator.translate(uploaded_file.getvalue().decode("utf-8"), dest=lang_code) 
  tts1=gTTS(text=translate.text, lang=lang_code)
  tts1.save('file.mp3')

  autoplay_audio("file.mp3")
