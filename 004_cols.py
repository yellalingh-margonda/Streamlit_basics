import streamlit as st

# Page title
st.title("Dashboard")

# CASE 1: Create ONE shared 2-column layout for the whole page
cols = st.columns(2)

# List of items to display as UI blocks
items = ["A", "B", "C"]

# Distribute items across the SAME two columns
# i % 2 alternates between column 0 and column 1
for i, item in enumerate(items):
    with cols[i % 2]:
        st.write(f"Box {item}")


# CASE 2: Create NEW columns for every single item (different behavior)

for item in items:
    # Each loop creates a fresh 2-column row
    cols = st.columns(2)

    # Put content only in first column of each new row
    with cols[0]:
        st.write(f"Box {item}")