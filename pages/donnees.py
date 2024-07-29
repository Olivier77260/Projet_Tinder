import streamlit as st
import pandas as pd
from function import load_data

# df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
df = load_data("Speed_Dating_Data.csv")

st.dataframe(df.head())
infor = df.info()
st.dataframe(infor)

st.dataframe(df.describe())

df_num = df.select_dtypes(exclude="object")
st.dataframe(df_num.columns)

df_catagories = df.select_dtypes(include="object")
st.dataframe(df_catagories.columns)