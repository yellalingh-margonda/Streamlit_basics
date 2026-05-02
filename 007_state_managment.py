import streamlit as st

# 🧠 What you will observe
# 🔴 Normal variable
# Always shows 1 (or 0 before click)
# Never accumulates
# Resets every rerun
# 🟢 session_state
# 1 → 2 → 3 → 4…
# Keeps growing
# Survives reruns (same session)

st.title("Session State vs Normal Variable")

# -----------------------------
# CASE 1: NORMAL VARIABLE
# -----------------------------
st.subheader("Without session_state")

count_normal = 0  # resets every rerun

if st.button("Increment Normal"):
    count_normal += 1

st.write("Normal count:", count_normal)


# -----------------------------
# CASE 2: SESSION STATE
# -----------------------------
st.subheader("With session_state")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment Session State"):
    st.session_state.count += 1

st.write("Session count:", st.session_state.count)