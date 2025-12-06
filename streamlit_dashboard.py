import streamlit as st


st.set_page_config(page_title="Streamlit Dashboard", page_icon=":signal_strength:", layout="wide")

st.sidebar.radio("Language", ["JP", "EN"], key="language")

pages = [
    st.Page("contents/home.py", title="Home", icon=":material/home:"),
    st.Page(f"contents/develop.py", title="Develop", icon=":material/build:"),
]
st.navigation(pages).run()
