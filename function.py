import streamlit as st
import pandas as pd

if 'del_from' not in st.session_state:
    st.session_state.del_from = False

@st.cache_data
def load_data(del_from):
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    if del_from:
        df = df.dropna(subset=['from', 'race'])
    return df
if st.session_state.del_from:
    load_data.clear()

df = load_data(st.session_state.del_from)