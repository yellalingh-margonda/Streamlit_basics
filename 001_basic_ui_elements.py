# Streamlit reruns your script top → bottom on every interaction
#
# This one concept explains:
#
# why variables reset
# why session_state exists
# why UI feels “reactive”

import streamlit as st

st.title("My App")
st.header("Section")
st.text("Simple text")
st.write({"a": 1})