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
c1, c2, c3, c4, c5 , c6 = st.columns(6)

with c1:
    st.text("Achintya Mishra")
    st.image("static/a.jpg")

with c2:
    st.text("Gaurav Agrawal")
    st.image("static/gaurav.jpg")

with c3:
    st.text("Dhanvin Ambavkar")
    st.image("static/dhanvin.jpg")

with c4:
    st.text("Ayaan Lone")
    st.image("static/ayaan.jpg")

with c5:
    st.text("Eeshaan Suryawanshi")
    st.image("static/eeshaan.jpg")
with c6:
    st.text("Arnav Kohli")
    st.image("static/arnav.jpg")