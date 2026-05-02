import streamlit as st

charts = ["Bar", "Line", "Pie"]

# User controls how many components appear
#
# ✔ multiple selections allowed
# ✔ UI scales up/down
# ✔ repeated structure is generated
#
# Think:
#
# “Build your own dashboard”

choice = st.multiselect("Select charts", charts)

for c in choice:
    st.write(f"Rendering {c} chart")