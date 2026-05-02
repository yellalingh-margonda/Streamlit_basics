import streamlit as st

# 🧠 What happens
# Inside container:
# grouped together visually
# treated as one block of UI
# Outside container:
# separate section
# [ Container ]
#   Text
#   Button
#   Slider
#
# [ Outside content ]
st.title("Container Example")

with st.container():
    st.write("This is inside a container")
    st.button("Button 1")
    st.slider("Slider", 0, 100)

st.write("This is outside the container")