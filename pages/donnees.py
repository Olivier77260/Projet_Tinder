import streamlit as st
import pandas as pd

df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")

st.dataframe(df)