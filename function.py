import streamlit as st
import pandas as pd



@st.cache_data
def load_data_True():
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    df = df.dropna(subset=['from', 'race'])
    return df
def load_data_False():
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    return df

dfTrue = load_data_True()
dfFalse = load_data_False()