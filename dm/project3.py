import streamlit as st 
import json, requests
from PIL import Image
import random
     

st.title("WELCOME TO YOUR APHASIA APP!")
st.write("\n")
st.header("What do you see on the picture below?")
st.write("\n")
st.write("\n")


items = ['to_eat', 'to_read', 'tree', 'apple']
if 'item' not in st.session_state:
    st.write('Item not set!')
    rand_item = random.choice(items)
    st.session_state.item = rand_item
    st.write('Item set to ' + rand_item)
else:
    rand_item = st.session_state.item
    st.write('Item still set to' + rand_item)


picture = "images/" + rand_item + '.jpg'
st.write("QUI IMMAGINE DI: " + rand_item)
#img = Image.open(picture)
#st.image(img, width=300)

#if st.button(label='START'):
user_input = st.text_input("Enter the word")
    
if user_input:
    st.write("You entered:",user_input)
    if user_input.lower() == str(rand_item):
        st.write("You entered the correct word!")
    else:
        st.write("Unfortunately ths is incorrect. Please try again or get a hint below.")
        st.write("\n")
        st.write("\n")
        option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])

        if option:
            key_dict = {"It is another word for": "rel_syn", "It sounds like": "sl", "Similar in meaning to": "ml", "It rhymes with": "rel_rhy"}
            key = key_dict[option] if option in key_dict else None

            if key:
                keyword = rand_item
                url = 'https://api.datamuse.com/words?' + key + "=" + keyword
                response = requests.get(url)
                dataFromDatamuse = json.loads(response.text)
                st.write(dataFromDatamuse[0]["word"])
            
                st.write("\n")
                st.write("Still no idea? Choose another hint!")
                st.write("\n")
                user_input2 = st.text_input("Or try again now and enter the word")
                if user_input2:
                    st.write("You entered:",user_input2)
                    if user_input2.lower() == str(rand_item):
                        st.write("Super! Now you entered the correct word!")
                    else:
                        st.write("Incorrect again. The word starts with", rand_item[0])
                        user_input3 = st.text_input("Last chance, enter the word")
                        if user_input3:
                          st.write("You entered:",user_input3)
                          if user_input3.lower() == str(rand_item):
                                        st.write("Super! Now you entered the correct word!")
                          else:
                            st.write("Incorrect again. The word was: ", rand_item) 
                        
                        
                        
else:
    #st.write("Please enter a word.")
    pass

if st.button("Reload app"):
     #for key in st.session_state.keys():
     del st.session_state
     #st.write(st.session_state['item'])

