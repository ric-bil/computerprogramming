#! python3
import json, requests 
import streamlit as st

#add your own APIkey
option = st.selectbox('Please, select an option', ('Synonyms', 'Antonyms', 'Sounds like', 'Means like')) 
keyword = st.text_input('Insert a keyword')

if option:
    if option=='Synonyms':
        choosen_option='rel_syn'
    elif option=='Antonyms':
        choosen_option='rel_ant'
    elif option=='Sounds like':
        choosen_option='sl'
    elif option=='Means like':
        choosen_option='ml'
    else:
        choosen_option = None

if (choosen_option and keyword):
    url= 'https://api.datamuse.com/words?' + choosen_option + '=' + keyword

    # Download the JSON data from Datamuse's API.
    response = requests.get(url)  

    #Load JSON data into a Python variable.
    responseData = json.loads(response.text)
    # Uncomment to see the raw JSON text:
    st.write("Responses: " + responseData[0]['word'] + ", ", responseData[1]['word'] + ", ", responseData[2]['word'] + ", ", responseData[3]['word'])

