import streamlit as st
import matplotlib.pyplot as plt
from function import df
import seaborn as sns

st.markdown("#### <font color='tomato'><ins>**ATTENTES DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

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

list_search = df.loc[:, 'attr1_1' : 'shar1_1'].sum().sort_values()
def quality(x):
    if x == 'attr1_1':
        size = "Attractive"
    elif x == 'sinc1_1':
        size = "Sincere"
    elif x == 'intel1_1':
        size = "Intelligent"
    elif x == 'fun1_1':
        size = "Fun"
    elif x == 'amb1_1':
        size = "Ambitious"
    else:
        size = "Has shared interests/hobbies"
    return size
list_search.index = list_search.index.map(quality)

colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig2, ax2 = plt.subplots()
ax2.pie(list_search, explode=explode, labels=list_search.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.divider()
col1, col2 = st.columns(2, gap='medium')
with col1:
    st.subheader("Attentes des participants.")
    st.pyplot(fig1)

with col2:
    st.subheader("Qualités recherchées dans le sexe opposé.")
    st.pyplot(fig2)

st.divider()

male0 = df[(df.gender == 1) & (df.match == 0) & (df.dec_o == 0)]
malepf = male0.loc[:, 'pf_o_att' : 'pf_o_sha'].sum().sort_values()
def quality_pf_o(x):
    if x == 'pf_o_att':
        size = "Attractive"
    elif x == 'pf_o_sin':
        size = "Sincere"
    elif x == 'pf_o_int':
        size = "Intelligent"
    elif x == 'pf_o_fun':
        size = "Fun"
    elif x == 'pf_o_amb':
        size = "Ambitious"
    else:
        size = "Has shared interests/hobbies"
    return size
malepf.index = malepf.index.map(quality_pf_o)
colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig3, ax3 = plt.subplots()
ax3.pie(malepf, explode=explode, labels=malepf.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


female0 = df[(df.gender == 0) & (df.match == 0) & (df.dec_o == 0)]
femalepf = female0.loc[:, 'pf_o_att' : 'pf_o_sha'].sum().sort_values()
femalepf.index = femalepf.index.map(quality_pf_o)
colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig4, ax4 = plt.subplots()
ax4.pie(femalepf, explode=explode, labels=femalepf.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


col3, col4 = st.columns(2, gap='medium')
with col3:
    st.subheader("Préférences déclarées au premier rendez-vous envers les hommes.")
    st.pyplot(fig3)

with col4:
    st.subheader("Préférences déclarées au premier rendez-vous envers les femmes.")
    st.pyplot(fig4)