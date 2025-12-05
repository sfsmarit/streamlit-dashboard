import streamlit as st


lang = st.sidebar.radio("Language", ["JP", "EN"])


pages = [
    st.Page("contents/home.py", title="Home", icon=":material/home:"),
    st.Page(f"contents/develop_{lang.lower()}.py", title="Develop", icon=":material/build:"),
]

st.navigation(pages).run()
