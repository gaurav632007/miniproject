import streamlit as st
import pandas as pd
import plotly.express as px
import os 

st.set_page_config(
    page_title="Home",
    layout="centered"
)

md ='''
# About

## Team Members
'''

st.markdown(md)
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.header("Achintya Mishra")
    st.image("static/a.jpg")

with c2:
    st.header("Gaurav Agrawal")
    st.image("static/gaurav.jpg")

with c3:
    st.header("Dhanvin Ambavkar")
    st.image("static/dhanvin.jpg")

with c3:
    st.header("Ayaan Lone")
    st.image("static/ayaan.jpg")

with c3:
    st.header("Eeshaan Suryawanshi")
    st.image("static/eeshaan.jpg")