import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Home",
    layout="centered"
)


ys = [str(y) for y in range(1800, 2026)]
df = pd.read_csv("datasets/children_per_woman_total_fertility.csv")
long = pd.melt(df, id_vars=['geo', 'name'], var_name='year', value_name='value')
long['geo'] = long['geo'].str.upper()



t1, t2 , t3 = st.tabs(["World Map", "Scatter","Line chart"])
with t1:
    st.header("World Map")
    clor = st.selectbox(
    "Choose Colour Scheme",
    ["Viridis",
"Plasma",
"Inferno",
"Magma",
"Cividis",
"Turbo",
"Aggrnyl",
"Agsunset",
"Bluered"],)
    fig2 = px.choropleth(long, locations="geo", color="value", hover_name="name", animation_frame="year",color_continuous_scale=clor)
    st.plotly_chart(fig2, use_container_width=True)
with t2:
    st.header("Scatter")
    
    fig = px.scatter(long,
    x="value",
    y ="name",
    animation_frame = "year",
    hover_name="name",
    log_x=False,
    size_max=60,)
    st.plotly_chart(fig, theme=None, use_container_width=True)
with t3:
    st.header("Line Chart")
    fig3 = px.line(long, x="year", y="value", color='name')
    st.plotly_chart(fig3, theme=None, use_container_width=True)













