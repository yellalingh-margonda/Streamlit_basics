import streamlit as st

st.title("Form Example")

with st.form("my_form"):
    name = st.text_input("Name")
    age = st.slider("Age", 0, 100)

    submitted = st.form_submit_button("Submit")

# This runs ONLY when submit is clicked
if submitted:
    st.write("Submitted Name:", name)
    st.write("Submitted Age:", age)