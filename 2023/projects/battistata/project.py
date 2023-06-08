from random import choice
import json,requests
import streamlit as st
from googletrans import Translator

st.title('Fun with adjectives')

if 'counter1' not in st.session_state or 'counter2' not in st.session_state :
 st.session_state.counter1 = 3
 st.session_state.counter2 = 3
if st.session_state.counter1 < 1 or st.session_state.counter2 < 1:
 st.title('Game Over!')
 st.stop()
 
words = ['forte','alto','giovane', 'nuovo', 'aperto','grande', 'caldo', 
         'amichevole', 'lungo', 'bagnato', 'pesante', 'pieno',  
        'ordinato', 'silenzioso', 'dolce', 'facile','veloce']

if 'choice' not in st.session_state:
 st.session_state.choice = choice(words)
translator = Translator(service_urls=['translate.googleapis.com'])
trans = translator.translate(st.session_state.choice,src='it', dest= 'en')
if 'word_trans' not in st.session_state:
 st.session_state.word_trans = trans.text
#st.write(st.session_state.word_trans)
 

 
st.write(st.session_state.choice)

word_input = st.text_input('inserisci la tua traduzione: ','')
st.write('Tentativi: ', st.session_state.counter1)

  
if word_input:
 if st.session_state.word_trans != word_input:
  st.session_state.counter1 -=1
  st.write('Sbagliato!')
 elif st.session_state.word_trans == word_input:
  st.write('Esatto! Ora passiamo agli antonimi!')
  url= 'https://api.datamuse.com/words?rel_ant=' + st.session_state.word_trans + ''
  response = requests.get(url)
  datamuse = json.loads(response.text)
  if 'antonym' not in st.session_state:
   st.session_state.antonym = datamuse[0]['word']
  #st.write(st.session_state.antonym)
  word_ant=st.text_input('scrivi qui l\' antonimo: ','')
  st.write('Tentativi: ', st.session_state.counter2)
  if word_ant:
   if word_ant != st.session_state.antonym:
    st.session_state.counter2 -=1
    st.write('Sbagliato!')
   elif word_ant == st.session_state.antonym:
    win = True
    st.write('Esatto! Premi Ctrl + R per continuare a giocare!')
