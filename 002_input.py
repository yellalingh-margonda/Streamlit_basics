import streamlit as st

st.title("My App")
st.header("Section")
st.text("Simple text")
st.write({"a": 1})
#
# st.something widgets store the value internally (in Streamlit’s session state)
# 👉 Your variable just reads that stored value on every rerun

# Every click / change:
#
# Streamlit reruns your script top → bottom
# Widget asks: “what value should I show?”
# Streamlit replies from its stored state
# Your variable receives that value for this run only

name = st.text_input("Enter name")
age = st.slider("Age", 0, 100)
clicked = st.button("Submit")

if clicked:
    st.write(name, age)