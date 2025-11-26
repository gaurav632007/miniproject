import streamlit as st


st.set_page_config(
    page_title="About",
    layout="centered"
)

md ='''
# About

## Team Members
'''

st.markdown(md)
c1, c2, c3, c4, c5 , c6 = st.columns(6,vertical_alignment= "top")

with c1:
    st.markdown("###### Achintya Mishra")
    st.image("static/a.jpg",width = "stretch")

with c2:
    st.markdown("###### Arnav Kohli")
    st.image("static/arnav.jpg",width= "stretch")

with c3:
    st.markdown("###### Dhanvin Ambavkar")
    st.image("static/dhanvin.jpg", width = "stretch")

with c4:
    st.markdown("###### Ayaan Lone")
    st.image("static/ayaan.jpg", width = "stretch")

with c5:
    st.markdown("###### Eeshaan Suryawanshi")
    st.image("static/eeshaan.jpg", width = "stretch")
with c6:
    st.markdown("###### Gaurav Agrawal")
    st.image("static/gaurav.jpg", width = "stretch")

