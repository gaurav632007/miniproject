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
c1, c2, c3, c4, c5 , c6 = st.columns(6)

with c1:
    st.text("Achintya Mishra")
    st.image("static/a.jpg",width = "stretch")

with c2:
    st.text("Arnav Kohli")
    st.image("static/arnav.jpg",width= "stretch")

with c3:
    st.text("Dhanvin Ambavkar")
    st.image("static/dhanvin.jpg", width = "stretch")

with c4:
    st.text("Ayaan Lone")
    st.image("static/ayaan.jpg", width = "stretch")

with c5:
    st.text("Eeshaan Suryawanshi")
    st.image("static/eeshaan.jpg", width = "stretch")
with c6:
    st.text("Gaurav Agrawal")
    st.image("static/gaurav.jpg", width = "stretch")

