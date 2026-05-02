import streamlit as st

st.title("Auto Tabs Example")

tab_names = ["Home", "Profile", "Settings", "Analytics"]

tabs = st.tabs(tab_names)

for tab, name in zip(tabs, tab_names):
    with tab:
        st.write(f"This is the {name} tab")