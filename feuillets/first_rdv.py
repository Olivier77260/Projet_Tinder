import streamlit as st
import numpy as np
from fonctions import nb_participant

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**PREMIERS RENDEZ-VOUS**</ins></font>", unsafe_allow_html=True)

@st.cache_data
def load_data_rdv(df):
    df3 = df.groupby(['age', 'gender', 'iid'])['match'].sum().reset_index()    
    return df3

df3 = load_data_rdv(df)
rdv = df3[df3.gender == 0 ].sum()
result = rdv.match
st.subheader("Suite au speed dating, personnes qui ont obtenues un premier rendez-vous.")
df3['gender'] = df3['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
st.bar_chart(df3, x="age", y="match", color='gender', stack=False, use_container_width=True)



col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    Nb_total_rencontre = len(df)
    st.metric(value=Nb_total_rencontre, label="Nombre total de rencontres lors du speed dating")


with col2:
    st.metric(value=result, label="Nombre total de rendez-vous obtenu")

with col3:
    pourcentage = np.round(result * 100 / Nb_total_rencontre, 2)
    st.metric(value=pourcentage, label="soit en pourcentage")

with col4:
    participant = nb_participant(df)
    pourcentage = np.round(result / participant, 2)
    st.metric(value=pourcentage, label="Nombre de rendez-vous obtenu par participant")

txt = st.text_area(
    "#### **Interprétation :**",
    "Le nombre de rendez-vous obtenu suite au speed dating est très faible. "
    "Nous avons en moyenne un peu plus d'un rendez-vous par personne, malgré une bonne correspondance dans les qualités recherchées. ",)
st.divider()
expander = st.expander("considérations :")
expander.write("Pour obtenir un rendez-vous, il faut que les 2 participants aient décidé de se revoir.")

expander2 = st.expander("Valeurs manquantes :")
expander2.metric(value=df3['match'][df3.gender == 1].isnull().sum(), label="Pour les hommes.")
expander2.metric(value=df3['match'][df3.gender == 0].isnull().sum(), label="Pour les femmes.")