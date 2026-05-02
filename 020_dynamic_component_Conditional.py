import streamlit as st

# Condition → change UI
# Meaning:
#
# User chooses ONE path
#
# ✔ Only one UI branch is active
# ✔ UI switches like a “mode change”
# ✔ Mutually exclusive options
#
# Think:
#
# “Pick one screen”
option = st.selectbox("Choose type", ["Text", "Number"])

if option == "Text":
    st.text_input("Enter text")

elif option == "Number":
    st.number_input("Enter number")

