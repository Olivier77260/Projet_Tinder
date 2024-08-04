import streamlit as st
from function import df
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.markdown("#### <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

st.subheader("""Paradoxalement le nombre de rendez-vous est inversement proportionnelle au nombre de sortie. On peut supposer"""
             """ que les personnes qui cherchent à faire des rencontres utilisent plutôt des applications dédiées. """)

sortie_rdv = pd.merge(df.go_out.value_counts(), df.date.value_counts(), right_index=True, left_index=True)
sortie_rdv = sortie_rdv.rename(columns={'count_x': 'Sorties', 'count_y': 'Rdv'})
def Frequence2(x):
    if x == 1:
        size = "1_Several times a week"
    elif x == 2:
        size = "2_Twice a week"
    elif x == 3:
        size = "3_Once a week"
    elif x == 4:
        size = "4_Twice a month"
    elif x == 5:
        size = "5_Once a month"
    elif x == 6:
        size = "6_Several times a year"
    else:
        size = "7_Almost never"
    return size
sortie_rdv['index'] = sortie_rdv.index.map(Frequence2)
st.bar_chart(sortie_rdv, x="index", y='Sorties', x_label='', stack='normalize', use_container_width=True, color="#dec1ff", horizontal=True)
st.bar_chart(sortie_rdv, x="index", y='Rdv', x_label='', stack='normalize', use_container_width=True, color= "#00d43c", horizontal=True)

objectifs = df.goal.value_counts()
def Objects(x):
    if x == 1.0:
        size = "Seemed like a fun night out"
    elif x == 2.0:
        size = "To meet new people"
    elif x == 3.0:
        size = "To get a date"
    elif x == 4.0:
        size = "Looking for a serious relationship"
    elif x == 5.0:
        size = "To say I did it"
    else:
        size = "Other"
    return size
objectifs.index = objectifs.index.map(Objects)
labels = objectifs.index
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(objectifs, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


rdv = df.date.value_counts()
def Frequence(x):
    if x == 1.0:
        size = "Several times a week"
    elif x == 2.0:
        size = "Twice a week"
    elif x == 3.0:
        size = "Once a week"
    elif x == 4.0:
        size = "Twice a month"
    elif x == 5.0:
        size = "Once a month"
    elif x == 6.0:
        size = "Several times a year"
    else:
        size = "Almost never"
    return size
rdv.index = rdv.index.map(Frequence)
labels = rdv.index
explode = (0.1, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig2, ax2 = plt.subplots()
ax2.pie(rdv, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=180)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

go_out = df.go_out.value_counts()
go_out.index = go_out.index.map(Frequence)
labels = go_out.index
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig3, ax3 = plt.subplots()
ax3.pie(go_out, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=60)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("L'objetif principal.")
    st.pyplot(fig1)

with col2:
    st.subheader("Fréquence des rendez-vous")
    st.pyplot(fig2)

with col3:
    st.subheader("Fréquence des sorties.")
    st.pyplot(fig3)

size = pd.DataFrame(df['date'] - df['go_out'])
size = size.value_counts().reset_index(name='index')
size = size.rename(columns={'o': 'value', 'index': 'Rdv'})
st.dataframe(size)
st.scatter_chart(df, x='date', y='go_out', use_container_width=True, color="#dec1ff")
# st.bar_chart(df, x="go_out", y='date', stack='normalize', use_container_width=True, color="#dec1ff")
st.line_chart(size, x='Rdv')
