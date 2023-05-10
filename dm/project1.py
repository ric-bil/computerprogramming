import json, requests
from PIL import Image
import random

import streamlit as st
	
	
	items = ['to_eat', 'to_read', 'tree', 'apple']
	rand_item = random.choice(items)
	#pictureX = st.empty()
	
	if st.button(label='START'):
	    picture = "images/" + rand_item + '.jpg'
	    img = Image.open(picture)
	    st.image(img, width=300)
	    
	    user_input = st.text_input("Enter the word")
	    
	    if user_input:
	        st.write(user_input)
	    #if user_input.lower() == str(rand_item):
	       # st.write("You entered the correct word!")
	   # else:
	       # st.write("Incorrect word. Please try again or get a hint.")
	       # st.write("\n")
	       # st.write("\n")
	       # option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])
	
	          #  if option:
	           #      key_dict = {"It is another word for": "rel_syn", "It sounds like": "sl", "Similar in meaning to": "ml", "It rhymes with": "rel_rhy"}
	           #     key = key_dict[option] if option in key_dict else None
	#
	             #   if key:
	              #      keyword = rand_item
	               #     url = 'https://api.datamuse.com/words?' + key + "=" + keyword

	                #    response = requests.get(url)
	                 #   dataFromDatamuse = json.loads(response.text)
	                  #  st.write(dataFromDatamuse[0]["word"])
	    
	                   # st.write("\n")
	                    #st.write("\n")
	                  #  user_input2 = st.text_input("Try again now! Enter the word")
	                    #if user_input2.lower() == str(rand_item):
	                    #    st.write("Super! Now you entered the correct word!")
