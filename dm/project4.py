import streamlit as st
import random

if "page" not in st.session_state:
  st.session_state.page = 0
if "user_input" not in st.session_state:
  st.session_state.user_input = None
if "rand_item" not in st.session_state:
  st.session_state.rand_item = None
def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
  items = ['to_eat', 'to_read', 'tree', 'apple']    
  if 'item' not in st.session_state:
    st.session_state.rand_item = random.choice(items)
    st.session_state.item = st.session_state.rand_item
  else:
    rand_item = st.session_state.item
    # Replace the placeholder with some text:
  with placeholder:
    st.title("WELCOME TO YOUR APHASIA APP!")
    st.write("\n")
    st.header("What do you see on the picture below?")
    st.write("\n")
    st.write("\n")
    st.session_state.user_input = st.text_input("Enter the word")
  picture = "images/" + st.session_state.rand_item + '.jpg'
  st.write("IMAGE OF: " + st.session_state.rand_item)
  #img = Image.open(picture)
  #st.image(img, width=300)

elif st.session_state.page == 1:
  if st.session_state.user_input:
    if st.session_state.user_input.lower() == str(st.session_state.rand_item):
      placeholder.write("You entered the correct word!")
    else:
      with placeholder:
        st.write("Unfortunately ths is incorrect. Please try again or get a hint below.")
        st.write("\n")
        st.write("\n")
        option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])

elif st.session_state.page == 2:
# Replace the chart with several elements:
    with placeholder.container():
        st.write("This is one element")
        st.write("This is another")
        st.metric("Page:", value=st.session_state.page)

elif st.session_state.page == 3:
    placeholder.markdown(r"$f(x) = \exp{\left(x^🐈\right)}$")

else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)
