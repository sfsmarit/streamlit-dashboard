import streamlit as st

pages = [
    st.Page("contents/home.py", title="Home", icon=":material/home:"),
    st.Page("contents/develop.py", title="Develop", icon=":material/construction:"),
]

st.navigation(pages).run()
