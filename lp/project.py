import streamlit as st 
import stanza
from googletrans import Translator

translator = Translator()
if 'clicked' not in st.session_state:
  st.session_state['clicked'] = '0'
else:
  clicked = st.session_state.clicked
  st.write(clicked)

st.title('Translator- Text Analyser')
st.header('Welcome to the slowest and still malfunctioning text analyser ever!')
st.write('''This app allows you to translate and then analyse a text in any language, 
as long as Stanza and Google Translate support it. To use it, just type a text in any language of your
choice. It will be automatically recognized. Then, choose a language. You can write the
name of the language in English or just type the two code-letter (e.g. for Spanish, you 
can either type "Spanish" or "es"). You will have a translation and then you can
walk through the sentences of the translated text. When clicking on a sentence,
you will have clickable single tokens. When clicking them, you will get the lemma and the part
of speech of the desired word.''')

input_text = st.text_area('Please, insert text here')
dest_lang = st.text_input('Enter a language here')

if (input_text and dest_lang):
  try:
    output_text = translator.translate(input_text, dest=dest_lang)
    st.write(output_text.text)
    translated_text = (output_text.text)
  except ValueError:
    st.info (f"{dest_lang} is not a valid language!")
    text = False
    dest_lang = False
else:
  st.info ("Oops! Something is missing!")

text = False
if (input_text and dest_lang):
  try:
    stanza.download(dest_lang)
    lan_nlp = stanza.Pipeline(f"{dest_lang}", processors = "tokenize, mwt" )
    text = lan_nlp(translated_text)
  except stanza.pipeline.core.UnsupportedProcessorError:
    st.info ("Sorry, this language is not supported.")
    text = False
  
duplicate_avoider = 0
if text != False:
  for i, sent in enumerate(text.sentences):
    sentence_text = sent.text
    st.write(clicked)
    if st.button(f"Sentence {i+1}: {sentence_text}", key=i):
      clicked = i
      st.session_state['clicked'] = clicked
    if clicked:
      st.write(f"Sentence {i+1}:")
      for word in sent.words:
        if word.pos == 'PUNCT':
          continue
        duplicate_avoider += 1
        st.button(word.text, key = duplicate_avoider)
    else:
      pass

  #st.info(f"Lemma: {word.lemma}; Part of Speech: {word.pos}")
