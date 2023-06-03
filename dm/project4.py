import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
  items = ['to_eat', 'to_read', 'tree', 'apple']    
  if 'item' not in st.session_state:
    rand_item = random.choice(items)
    st.session_state.item = rand_item
  else:
    rand_item = st.session_state.item
    # Replace the placeholder with some text:
  with placeholder:
    st.title("WELCOME TO YOUR APHASIA APP!")
    st.write("\n")
    st.header("What do you see on the picture below?")
    st.write("\n")
    st.write("\n")
    user_input = st.text_input("Enter the word")
  picture = "images/" + rand_item + '.jpg'
  st.write("IMAGE OF: " + rand_item)
  #img = Image.open(picture)
  #st.image(img, width=300)

    
    
    
elif st.session_state.page == 1:
    # Replace the text with a chart:
    placeholder.line_chart({"data": [1, 5, 2, 6]})

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
