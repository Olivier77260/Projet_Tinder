import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from function import df

age_gender = df.groupby('age')['gender'].value_counts().reset_index()
age_gender['gender'] = age_gender['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
# sns.catplot(x="age", y="count", kind="bar", hue="gender", data=age_gender, aspect=2.5)

# st.bar_chart(age_gender, x="age", y="count", color="gender", horizontal=False)

st.bar_chart(age_gender, x="age", y="count", color="gender", stack=False, use_container_width=True)