import streamlit as st
from contents import develop_jp, develop_en

if st.session_state["language"] == "JP":
    develop_jp.render()
else:
    develop_en.render()
