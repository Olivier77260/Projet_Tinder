import streamlit as st
import numpy as np

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**PREMIERS RENDEZ-VOUS**</ins></font>", unsafe_allow_html=True)

df3 = df.groupby(['age', 'gender'], dropna=False)['match'].sum().reset_index()
df3['gender'] = df3['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
st.bar_chart(df3, x="age", y="match", color='gender', stack=False, use_container_width=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    Nb_total_rencontre = len(df)
    st.metric(value=Nb_total_rencontre, label="Nombre total de rencontres lors du speed dating")


with col2:
    somme_rdv = df3[df3.gender == "#ff00ff"].sum()
    somme_rdv = somme_rdv.iloc[2]
    st.metric(value=somme_rdv, label="Nombre total de rendez-vous obtenu")

with col3:
    pourcentage = np.round(somme_rdv * 100 / Nb_total_rencontre, 2)
    st.metric(value=pourcentage, label="soit en pourcentage")

expander = st.expander("Considèrations :")
expander.write('Le nombre de rendez-vous obtenu suite au speed dating est trés faible malgré une correspondance dans les qualités recherchées.')

expander2 = st.expander("Valeurs manquantes :")
expander2.metric(value=df3['match'][df3.gender == 1].isnull().sum(), label="Pour les hommes.")
expander2.metric(value=df3['match'][df3.gender == 0].isnull().sum(), label="Pour les femmes.")