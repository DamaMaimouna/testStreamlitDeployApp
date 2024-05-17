import streamlit as st 
import pandas as pd

@st.cache_data  
def load_json(path):
    df = pd.read_json(path)
    return df

