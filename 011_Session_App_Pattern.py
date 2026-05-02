import streamlit as st


st.title("Simple List App")
# Instead of random variables, structure like:
# if we don't do this st.session_state.my_items = [] instead of if check and
# initilize then on every run it will create an empty list

if "my_items" not in st.session_state:
    st.session_state.my_items = []

item = st.text_input("Enter item")

if st.button("Add"):
    st.session_state.my_items.append(item)

st.write(st.session_state.my_items)
