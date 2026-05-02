import streamlit as st

def card(title, value):
    with st.container():
        st.subheader(title)
        st.write(value)

data = {
    "Revenue": "$10K",
    "Users": "500",
    "Growth": "12%"
}

for k, v in data.items():
    card(k, v)