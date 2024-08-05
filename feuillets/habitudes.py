import streamlit as st
from function import df
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.markdown("#### <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

st.subheader("""Paradoxalement, ce n'est pas parce que l'on sort beaucoup que l'on fait plus de rencontre."""
             """ D'où le succés de l'utilisation des applications dédiées. """)
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
sortie_rdv = pd.merge(df.go_out.value_counts(), df.date.value_counts(), right_index=True, left_index=True)
sortie_rdv = sortie_rdv.rename(columns={'count_x': 'Sorties', 'count_y': 'Rdv'})
sortie_rdv['index'] = sortie_rdv.index.map(Frequence2)

st.divider()
col2, col3 = st.columns(2, gap='large')
with col2:
    st.subheader("Fréquence des sorties.")
    st.bar_chart(sortie_rdv, x="index", y='Sorties', x_label='Fréquence des sorties', stack=False, use_container_width=True, color="#dec1ff", horizontal=True)

with col3:
    st.subheader("Fréquence des rendez-vous.")
    st.bar_chart(sortie_rdv, x="index", y='Rdv', x_label='Fréquence des rendes-vous', stack=False, use_container_width=True, color= "#00d43c", horizontal=True)

ethnic = df['imprace'].value_counts().reset_index(name='somme')
ethnic['iid'] = ethnic['imprace']
religious = df['imprelig'].value_counts().reset_index(name='total')
religious['iid'] = religious['imprelig']
dataset = religious.merge(ethnic, on='iid')
dataset = dataset.sort_values('iid')
plt.plot(
    'iid', 'total', data=dataset,
    marker='o', # marker type
    markerfacecolor='blue', # color of marker
    markersize=4, # size of marker
    color='blue', # color of line
    linewidth=2, # change width of line
    label="religion" # label for legend
)

plt.plot(
    'iid', 'somme', data=dataset,
    marker='+', # no marker
    color='green', # color of line
    linewidth=2, # change width of line
    linestyle='dashed', # change type of line
    label="race" # label for legend
)

# show legend
plt.legend()

# fig, ax = plt.subplots()
# ax.scatter(x, y)
# # other plotting actions...
st.pyplot()

st.line_chart(
    dataset,
    x="iid",
    y=["total", "somme"],
    color=["#FF0000", "#0000FF"],  # Optional
)