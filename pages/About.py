import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="About",
    layout="centered"
)

md ='''
# About

## Team Members
- Achintya Mishra
- Gaurav Agrawal
- Dhanvin Ambavkar
- Ayaan Lone 
- Eeshaan Suryawanshi

'''

st.markdown(md)
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Achintya Mishra")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Gaurav Agrawal ")
    st.image("static/p.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
