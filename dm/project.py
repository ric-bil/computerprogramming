import random
import streamlit as st

items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)
st.write(rand_item)

if st.button(label='START'):
  picture = "images/" + rand_item + '.jpg'
  img = Image.open(picture)
  st.image(img, width=300)
