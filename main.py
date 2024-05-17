import streamlit as st
import pandas as pd 
import json
from pages import *


st.title ( "Une app Multipage ")
st.image('images/sf st.jpeg' , width = 400, use_column_width = False)



PAGES = {
    "Page 1": "bmi",
    "Page 2": "candidate",
    "Page 3": "chatbot"
}


