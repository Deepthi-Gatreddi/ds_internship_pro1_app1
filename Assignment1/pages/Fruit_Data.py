import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "fruits1.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Fruits.csv")

st.title("Dashboard - Fruits Data")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Some Fruits Data")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.header("Select the Fruit:")

fruit = st.selectbox(" ", df['fruit_name'].unique())

col, col1 = st.columns(2)

fig1 = px.histogram(df[df['fruit_name'] == fruit], x="fruit_subtype")
col.plotly_chart(fig1, use_container_width=True)

fig2 = px.box(df[df['fruit_name'] == fruit], y="mass")
col1.plotly_chart(fig2, use_container_width=True)