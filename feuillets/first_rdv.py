import streamlit as st
import pandas as pd
import numpy as np

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**PREMIERS RENDEZ-VOUS**</ins></font>", unsafe_allow_html=True)

df3 = df.groupby(['age', 'gender'])['match'].sum().reset_index()
df3['gender'] = df3['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
st.bar_chart(df3, x="age", y="match", color='gender', stack=False, use_container_width=True)

# @st.cache_data
# def load_data_df3(df):
#     df3 = df.groupby(['age', 'gender', 'match'])['iid'].value_counts().reset_index()
#     return df3


# df3 = load_data_df3(df)
# # somme des match
# df4 = df3.groupby(['age', 'gender', 'iid'])['count'].sum().reset_index()
# # somme des oui
# df5 = df3[df3.dec ==1]
# df6 = pd.merge(df5, df4, how='left', on=["age", "gender", 'iid'], suffixes=('_yes', '_match'))
# def moy(row):
#     a = (100 * row['count_yes']) / row['count_match']
#     return np.round(a, decimals=2)
# df6['moy'] = df6.apply(lambda x : moy(x), axis=1)
# result_female = np.round(df6['moy'][df6.gender == 0].mean(), decimals=2)
# result_male = np.round(df6['moy'][df6.gender == 1].mean(), decimals=2)
# #affichage des pourcentage
# col1, col2 = st.columns(2, gap='large')
# with col1:
#     st.metric(value=result_female, label="pourcentage de rendez-vous obtenue pour les femmes")
# with col2:
#     st.metric(value=result_male, label="pourcentage de rendez-vous obtenue pour les hommes")
# graph

# tableau = df6.groupby(['gender', 'age'])['moy'].mean().reset_index()


# df3 = df.groupby(['age', 'gender', 'iid'])['match'].value_counts().reset_index()
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

expander = st.expander("A noter")
expander.write('''
    Le nombre de rendez-vous correspond à la somme des matchs égals à 1 divisé par 2. 
    Le nombre de rendez-vous obtenu suite au speed dating est trés faible malgré une correspondance dans les qualités recherchées.
''')