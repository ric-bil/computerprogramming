#! python3
import json, requests 
from googletrans import Translator
import streamlit as st

language = st.selectbox('Please, select an destionation language', ('it', 'de', 'en', 'fr')) 
keyword = st.text_input('Insert a word or a sentence')


if (language and keyword):
    translate = translator.translate(word, dest=language) 
    print(translate)
