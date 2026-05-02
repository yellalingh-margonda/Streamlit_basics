import streamlit as st

st.title("Expander UI Example")

with st.expander("Click to open advanced settings"):
    st.write("You can put any UI inside expander")

    name = st.text_input("Enter your name")
    age = st.slider("Select age", 0, 100)

    if st.button("Submit inside expander"):
        st.success(f"Hello {name}, age {age}")