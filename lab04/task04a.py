#! python3
import json, requests 
import streamlit as st

options = {
    'rel_syn':'Synonyms',
    'rel_ant':'Antynoms',
    'sl':'Sounds like',
    'ml':'Means like'
}

option = st.selectbox('Please, select an option', options.values()) 
keyword = st.text_input('Insert a keyword')

if option:
  key = [k for k, v in options.items() if v == option]
  choosen_option = key[0]

if (choosen_option and keyword):
    url= 'https://api.datamuse.com/words?' + choosen_option + '=' + keyword

    # Download the JSON data from Datamuse's API.
    response = requests.get(url)  

    #Load JSON data into a Python variable.
    responseData = json.loads(response.text)
    # Uncomment to see the raw JSON text:
    st.write(responseData)
