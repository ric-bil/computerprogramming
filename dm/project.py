import random
from PIL import Image
import streamlit as st

# The items list
items = ['to_eat', 'to_read', 'tree', 'apple']

# Looks if the item was already choosen
if 'item' not in st.session_state:
  rand_item = random.choice(items)
  st.session_state.item = rand_item
  st.write("SCELGO: " + rand_item)
# Otherwise set a random item    
else:
  rand_item = st.session_state.item
  st.write("HO: " + rand_item)
  
if 'playing' not in st.session_state:
  st.session_state.playing = True

if st.button("START"):
  st.write('IMAGE ' + rand_item)
  #picture = "images/" + rand_item + '.jpg'
  #img = Image.open(picture)
  #st.image(img, width=300)
 
  user_input = st.text_input("Enter the word")

  if user_input:
    st.write(user_input)

    #if user_input.lower() == str(rand_item):
    #  st.write("You entered the correct word!")
    #  del st.session_state['item']
    #else:
    #  st.write("Incorrect word. Please try again or get a hint.")
    #  st.write("\n")
    #  st.write("\n")
    
      



