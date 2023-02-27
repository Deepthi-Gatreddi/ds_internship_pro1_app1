import streamlit as st
from matplotlib import image
import pandas as pd
import os

st.title("Dashboard - Fruits Image")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "fruits.jpg")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Select the Fruit:")
power = st.selectbox("To See the Image",{"Apple","Orange","Lemon","Mandarin"})
    
if power == 'Apple':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "apple.jpg")
    img1 = image.imread(IMAGE_PATH1)
    st.image(img1)
if power == 'Orange':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "orange.jpg")
    img1 = image.imread(IMAGE_PATH1)
    st.image(img1)
if power == 'Lemon':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "lemon.jpg")
    img1 = image.imread(IMAGE_PATH1)
    st.image(img1)
if power == 'Mandarin':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "mandarin.jpg")
    img1 = image.imread(IMAGE_PATH1)
    st.image(img1)








