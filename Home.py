import streamlit as st



st.set_page_config(
    page_title="Home",
    layout="centered"
)

# making style classes
st.markdown(
    """
    <style>
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
-  Gapminder Foundation. Gapminder Data Documentation and Datasets.
Available at: https://www.gapminder.org/data
(Used for population, GDP, life expectancy, fertility rate, CO₂ emissions, and other global indicators.)
- Streamlit Documentation. Streamlit — The fastest way to build data apps.
Available at: https://docs.streamlit.io
(Used to create the interactive web application/dashboard.)
- Pandas Documentation.
Available at: https://pandas.pydata.org/docs
(Used for data loading, cleaning, manipulation, and merging.)
- Plotly Documentation.
Available at: https://plotly.com/python
(Used to create world maps, bar charts, line graphs, scatter plots, and animated visualizations.)
- Python Official Documentation.
Available at: https://docs.python.org
(General programming reference.)
  Streamlit Community Cloud.
Available at: https://streamlit.io/cloud
(Used for hosting and deploying the project dashboard online.)
- Kurzgesagt  In a Nutshell. Educational Videos on Global Change and Data Trends.
YouTube Channel: https://www.youtube.com/@kurzgesagt
(Used for conceptual inspiration and understanding global trends.)
 
'''
htu = '''# How to Use  
1. Just choose the dataset you want from the sidebar.
2. Choose the data representation format.
3. Slide the year graph to get a year wise picture. 
4. Some graphs have an animated vresion of them try it.
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
VIDEO_URL = "https://youtu.be/S7TUe5w6RHo?si=8yBb5SGrhdUXkO7M"
st.video(VIDEO_URL)
st.markdown('<div>credits: kurzgesagt- In a Nutshell </div> <a href="https://www.youtube.com/@kurzgesagt">youtube channel</a>', unsafe_allow_html=True)
st.markdown(ref)
