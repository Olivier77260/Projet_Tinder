import streamlit as st
from function import df
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.markdown("#### <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

st.subheader("L'objetif principal.")
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
st.pyplot(fig1)

st.divider()
st.subheader("Fréquence des rendez-vous")
rdv = df.date.value_counts()

def Frequence(x):
    if x == 1.0:
        size = "Several times a week"
    elif x == 2.0:
        size = "Twice a week"
    elif x == 3.0:
        size = "Once a week"
    elif x == 4.0:
        size = "Twice a mont"
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
fig1, ax1 = plt.subplots()
ax1.pie(rdv, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st.divider()
st.subheader("Fréquence des sorties.")
go_out = df.go_out.value_counts()

go_out.index = go_out.index.map(Frequence)
labels = go_out.index
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(go_out, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=60)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st.divider()
st.subheader("Paradoxalement le nombre de rendez-vous et inversement proportionnelle au nombre de sortie.")
sortie_rdv = pd.merge(df.go_out.value_counts(), df.date.value_counts(), right_index=True, left_index=True)
sortie_rdv = sortie_rdv.rename(columns={'count_x': 'Sorties', 'count_y': 'Rdv'})
chart_data = pd.DataFrame(sortie_rdv, columns=['Rdv', 'Sorties'])

st.line_chart(chart_data, color=["#FF0000", "#0000FF"])