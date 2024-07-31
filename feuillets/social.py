import streamlit as st
import numpy as np
import pandas as pd

st.markdown("#### <font color='tomato'><ins>**PROFIL SOCIAL**</ins></font>", unsafe_allow_html=True)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

import streamlit as st

import matplotlib.pyplot as plt



# Pie chart, where the slices will be ordered and plotted counter-clockwise:

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)