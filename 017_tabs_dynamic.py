import streamlit as st

st.title("Dynamic Tabs with Conditional Widgets")

# -----------------------------
# 1. Define tabs + what each tab should show
# -----------------------------
tab_config = {
    "Home": "home",
    "Profile": "profile",
    "Settings": "settings"
}

# -----------------------------
# 2. Create tabs dynamically
# -----------------------------
tabs = st.tabs(list(tab_config.keys()))

# -----------------------------
# 3. Render content conditionally
# -----------------------------
for tab, tab_name in zip(tabs, tab_config.values()):
    with tab:

        if tab_name == "home":
            st.write("🏠 This is Home tab")
            st.button("Home button")

        elif tab_name == "profile":
            st.write("👤 This is Profile tab")
            name = st.text_input("Enter name")

        elif tab_name == "settings":
            st.write("⚙️ This is Settings tab")
            volume = st.slider("Volume", 0, 100)