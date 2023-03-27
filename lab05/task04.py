#! python3
import json, requests 
from googletrans import Translator
import streamlit as st

option = st.selectbox('Please, select an destionation language', ('it', 'de', 'en', 'fr')) 
keyword = st.text_input('Insert a word or a sentence')


if (option and keyword):
    translate = translator.translate(word, dest=language) 
    print(translate)
