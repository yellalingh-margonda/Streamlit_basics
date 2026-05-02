import streamlit as st

st.title("My App")
st.header("Section")
st.text("Simple text")
st.write({"a": 1})

# Across button clicks (NO refresh)
#
# 👉 This works because:
#
# Streamlit reruns the script
# BUT st.session_state is preserved in the browser session
# So count keeps increasing

# Browser creates a new session
# Streamlit loses previous session memory
# st.session_state resets
#
# So:
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)
