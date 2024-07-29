import streamlit as st
import pandas as pd
from function import load_data
from function import df

st.dataframe(df.head(), hide_index=True)
infor = df.info()
st.dataframe(infor)

st.dataframe(df.describe())

df_num = df.select_dtypes(exclude="object")
st.dataframe(df_num.columns)

df_catagories = df.select_dtypes(include="object")
st.dataframe(df_catagories.columns)