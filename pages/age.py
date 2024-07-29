import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from function import load_data

# @st.cache_data
# def load_data(file):
#     df = pd.read_csv(file, encoding="cp1252")
#     return df

df = load_data("Speed_Dating_Data.csv")

age_gender = df.groupby('age')['gender'].value_counts().reset_index()
age_gender['gender'] = age_gender['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
# sns.catplot(x="age", y="count", kind="bar", hue="gender", data=age_gender, aspect=2.5)

# st.bar_chart(age_gender, x="age", y="count", color="gender", horizontal=False)

st.bar_chart(age_gender, x="age", y="count", color="gender", stack=False, use_container_width=True)