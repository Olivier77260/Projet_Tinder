import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**SPEED DATING**</ins></font>", unsafe_allow_html=True)

st.subheader("Le speed dating est un rendez-vous d'une durée d'environ 4 mn avec le partenaire selectionné.")


tab1, tab2 = st.tabs(["##### :blue[***1. Envers les hommes***]", "##### :blue[***2. Envers les femmes***]"])
# préferences male
preference_male1 = df[(df.gender == 1) & (df.match == 0) & (df.dec_o == 0)]
preference_male = preference_male1.loc[:, 'pf_o_att' : 'pf_o_sha'].sum().sort_values()
preference_male.index = preference_male.index.map(quality_pf_o)
colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)
fig3, ax3 = plt.subplots()
ax3.pie(preference_male, explode=explode, labels=preference_male.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax3.axis('equal')

# préferences female
preference_female1 = df[(df.gender == 0) & (df.match == 0) & (df.dec_o == 0)]
preference_female = preference_female1.loc[:, 'pf_o_att' : 'pf_o_sha'].sum().sort_values()
preference_female.index = preference_female.index.map(quality_pf_o)
colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)
fig4, ax4 = plt.subplots()
ax4.pie(preference_female, explode=explode, labels=preference_female.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax4.axis('equal')

# evaluations male
male_evaluation0 = preference_male1.loc[:, 'attr_o' : 'shar_o'].sum().sort_values()
male_evaluation0.index = male_evaluation0.index.map(quality_o)
colors = sns.color_palette("bright")
explode = (0, 0.1, 0, 0, 0, 0)
fig5, ax5 = plt.subplots()
ax5.pie(male_evaluation0, explode=explode, labels=male_evaluation0.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax5.axis('equal')

# évaluations female
female_evaluation0 = preference_female1.loc[:, 'attr_o' : 'shar_o'].sum().sort_values()
female_evaluation0.index = female_evaluation0.index.map(quality_o)
explode = (0, 0.1, 0, 0, 0, 0)
fig6, ax6 = plt.subplots()
ax6.pie(female_evaluation0, explode=explode, labels=female_evaluation0.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax6.axis('equal')

#affichage preferences
with tab1:
    col3, col4 = st.columns(2, gap='medium')
    with col3:
        st.divider()
        st.subheader("Préférences déclarées au speed dating envers les hommes.")
        st.pyplot(fig3)
        st.metric(value=preference_male1['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col4:
        st.divider()
        st.subheader("Suite au premier rendez-vous l'attractivité envers les hommes n'y est pas.")
        st.pyplot(fig5)
        st.metric(value=preference_female1['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")

# affichage évaluations
with tab2:
    col5, col6 = st.columns(2, gap='medium')
    with col5:
        st.divider()
        st.subheader("Préférences déclarées au premier rendez-vous envers les femmes.")
        st.pyplot(fig4)
        st.metric(value=preference_male1['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.") 

    with col6:
        st.divider()
        st.subheader("Suite au premier rendez-vous l'attractivité envers les femmes n'y est pas.")
        st.pyplot(fig6)
        st.metric(value=preference_female1['pf_o_att'].isnull().sum(), label="Nombre de valeurs manquantes.")