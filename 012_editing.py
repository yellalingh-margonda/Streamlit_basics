import streamlit as st

# 🧠 Key insight
#
# 👉 Step 2 = “change state”
# 👉 Step 3 = “react to state”
# Step 1: initialize state
if "editing_id" not in st.session_state:
    st.session_state.editing_id = None

st.title("Edit Example")

st.write("Current editing_id:", st.session_state.editing_id)

# Step 2: button logic
if st.button("Edit Item 1"):
    st.session_state.editing_id = 1
    st.rerun()

# Step 3: conditional UI based on state
if st.session_state.editing_id == 1:
    st.success("You are editing item 1")
    new_value = st.text_input("Edit value")

    if st.button("Save"):
        st.success(f"Saved: {new_value}")
        st.session_state.editing_id = None
        st.rerun()