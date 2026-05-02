import streamlit as st

st.title("My App")
st.header("Section")
st.text("Simple text")
st.write({"a": 1})

name = st.text_input("Enter name")
age = st.slider("Age", 0, 100)
clicked = st.button("Submit")

if clicked:
    st.write(name, age)

# Core rule in Streamlit layout
#
# 👉 Everything goes in the main page by default
# 👉 Only st.sidebar explicitly sends content to the sidebar

# means:
#
# “Create two columns inside the MAIN area”
#
# NOT sidebar.
c1, c2 = st.columns(2)

with c1:
    st.write("Left")

with c2:
    st.write("Right")
st.sidebar.write("Sidebar content")