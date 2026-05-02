import streamlit as st

st.title("Main Page")

with st.sidebar:
    st.header("Sidebar")

    # columns inside sidebar
    c1, c2 = st.columns(2)

    with c1:
        st.button("Left")

    with c2:
        st.button("Right")