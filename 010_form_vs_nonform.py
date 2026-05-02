import streamlit as st

st.title("Form vs No Form")

# -----------------------------
# CASE 1: WITHOUT FORM (live updates)

# WITHOUT form
# Widgets update immediately
# Streamlit reruns the script on every interaction
# Variables get the latest widget value on every rerun
# -----------------------------
st.subheader("Without st.form()")

name_live = st.text_input("Name (live)")
age_live = st.slider("Age (live)", 0, 100)

st.write("Live Name:", name_live)
st.write("Live Age:", age_live)


st.divider()

# -----------------------------
# CASE 2: WITH FORM (submit-based)
# Inputs are still stored internally while typing
# BUT script does NOT rerun
# Only when you click submit:
# Streamlit triggers rerun
# values are then read into variables
# -----------------------------
st.subheader("With st.form()")

with st.form("my_form"):
    name_form = st.text_input("Name (form)")
    age_form = st.slider("Age (form)", 0, 100)

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Submitted Name:", name_form)
    st.write("Submitted Age:", age_form)