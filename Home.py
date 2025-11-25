import streamlit as st
import pandas as pd
#import plotly.express as px


st.set_page_config(
    page_title="Home",
    layout="centered"
)

# making style classes
st.markdown(
    """
    <style>
    .main {
        background: #ffffff;
        color: #ffffff;
    }
    .block-title {
        border-radius: 12px;
        font-size: 36px;
        font-weight: 700;
    }
    .earth {
        font-size: 91px;
        align: center
    }
    </style>
    """,
    unsafe_allow_html=True
)
ref = '''# References and Credits  
- 
-  
-  
'''
htu = '''# How to Use  
1. just choose the data you want from the sidebar 
2. choose the data representation format
3. slide the year graph to get a year wise picture 
4. some graphs have an animated vresion of them try it
5. Enjoy !   
   
----


'''
st.markdown('<center class ="earth">🌍</center>', unsafe_allow_html=True)
st.markdown('<center class="block-title">How the World Changes Over The Years </center>', unsafe_allow_html=True)
st.write(
    "<center>Visualise Real Global data on Physcial, Environmental, Economic, Social, Cultural and other types of changes throughout the world </center>",unsafe_allow_html=True
)
st.markdown('<div> </div>', unsafe_allow_html=True)
st.markdown('<div> </div>', unsafe_allow_html=True)
st.markdown('<div>  </div>', unsafe_allow_html=True)
st.markdown(htu)
VIDEO_URL = "https://youtu.be/S7TUe5w6RHo"
st.video(VIDEO_URL)
st.markdown('<div>credits: kurzgesagt- In a Nutshell</div> <a href="https://www.youtube.com/@kurzgesagt">youtube channel</a>', unsafe_allow_html=True)
st.markdown(ref)
