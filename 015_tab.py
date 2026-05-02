import streamlit as st

st.title("Tabs Example")

tab1, tab2, tab3 = st.tabs(["Home", "Profile", "Settings"])

with tab1:
    st.write("🏠 This is Home tab")
    st.button("Home button")

with tab2:
    st.write("👤 This is Profile tab")
    name = st.text_input("Enter name")

with tab3:
    st.write("⚙️ This is Settings tab")
    st.slider("Volume", 0, 100)