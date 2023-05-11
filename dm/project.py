import random
from PIL import Image
import streamlit as st

items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)

st.write('IMMAGINE ' + rand_item)
#picture = "images/" + rand_item + '.jpg'
#img = Image.open(picture)
#st.image(img, width=300)
 
user_input = st.text_input("Enter the word")

if user_input:	
  st.write(user_input)

  if user_input.lower() == str(rand_item):
    st.write("You entered the correct word!")
  else:
    st.write("Incorrect word. Please try again or get a hint.")
    st.write("\n")
    st.write("\n")
    st.button("TRY AGAIN")
      #    option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])
      #st.button(label='PLAY AGAIN')
      
      



