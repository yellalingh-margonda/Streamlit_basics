import streamlit as st

st.title("Expander Example")

st.write("This is always visible")

with st.expander("Click to see more details"):
    st.write("Here is hidden content 👀")
    st.write("You can put any UI inside expander")
    st.button("Hidden button")