import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("#### <font color='tomato'><ins>**PREMIERS RENDEZ-VOUS**</ins></font>", unsafe_allow_html=True)

st.subheader("""Paradoxalement, ce n'est pas parce que l'on sort beaucoup que l'on fait plus de rencontre."""
             """ D'où le succés de l'utilisation des applications dédiées. """)

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



male_evaluation0 = male0.loc[:, 'attr_o' : 'shar_o'].sum().sort_values()
def quality_o(x):
    if x == 'attr_o':
        size = "Attractive"
    elif x == 'sinc_o':
        size = "Sincere"
    elif x == 'intel_o':
        size = "Intelligent"
    elif x == 'fun_o':
        size = "Fun"
    elif x == 'amb_o':
        size = "Ambitious"
    else:
        size = "Has shared interests/hobbies"
    return size
male_evaluation0.index = male_evaluation0.index.map(quality_o)

colors = sns.color_palette("bright")
explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig5, ax5 = plt.subplots()
ax5.pie(male_evaluation0, explode=explode, labels=male_evaluation0.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


female_evaluation0 = female0.loc[:, 'attr_o' : 'shar_o'].sum().sort_values()
female_evaluation0.index = female_evaluation0.index.map(quality_o)

explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig6, ax6 = plt.subplots()
ax6.pie(female_evaluation0, explode=explode, labels=female_evaluation0.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax6.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

col3, col4 = st.columns(2, gap='medium')
with col3:
    st.subheader("Préférences déclarées au premier rendez-vous envers les hommes.")
    st.pyplot(fig3)
    st.metric(value=male0['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")

with col4:
    st.subheader("Suite au premier rendez-vous l'attractivité envers les hommes n'y est pas.")
    st.pyplot(fig5)
    st.metric(value=female0['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")

st.divider()

col5, col6 = st.columns(2, gap='medium')
with col5:
    st.subheader("Préférences déclarées au premier rendez-vous envers les femmes.")
    st.pyplot(fig4)
    st.metric(value=male0['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.") 

with col6:
    st.subheader("Suite au premier rendez-vous l'attractivité envers les femmes n'y est pas.")
    st.pyplot(fig6)
    st.metric(value=female0['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")

st.balloons()