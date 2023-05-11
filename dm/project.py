import random
from PIL import Image
import streamlit as st

items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)

st.button(label='START')
st.write(rand_item)
  #picture = "images/" + rand_item + '.jpg'
  #img = Image.open(picture)
  #st.image(img, width=300)
  
user_input = st.text_input("Enter the word")

if user_input:
  st.write(user_input)
  st.button(label='PLAY AGAIN')
