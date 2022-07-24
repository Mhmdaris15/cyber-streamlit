import streamlit as st
import streamlit.components.v1 as stc
import PIL

logo = PIL.Image.open("img/test-account-48.png")
st.set_page_config(page_title="Profile Page | Cybersecurity", page_icon=logo)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
with open('index.html') as g:
    st.markdown(f'<text>{g.read()}</text>', unsafe_allow_html=True)

st.sidebar.markdown("Profile Page❄️")