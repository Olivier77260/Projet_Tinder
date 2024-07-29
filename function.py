import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file):
    df = pd.read_csv(file, encoding="cp1252")
    return df

df = load_data("Speed_Dating_Data.csv")