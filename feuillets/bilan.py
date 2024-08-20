import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fonctions import nb_participant
from annotated_text import annotated_text
from fonctions import list_age, quality_o_7

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**BILAN DU SPEED DATING**</ins></font>", unsafe_allow_html=True)   

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Suivant l'âge***]", "##### :blue[***2. Suivant la race***]", "##### :blue[***2. Qualités recherchées***]"])

@st.cache_data
def load_data_rdv(df):
    df3 = df.groupby(['age', 'gender'])['match'].sum().reset_index()    
    return df3

df3 = load_data_rdv(df)


with tab1:
    st.subheader("Nombre de match obtenu en fonction de l'âge.")    
    df3['gender'] = df3['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')    
    st.bar_chart(df3, x="age", y="match", color='gender', stack=False, use_container_width=True)
    annotated_text(
    "Male : ",
    ("", "blue", "#4169e1"),
    " Female : ",
    ("", "rose", "#ff00ff"),)
    expander2 = st.expander("Valeurs manquantes :")
    expander2.metric(value=df['match'][df.gender == 1].isnull().sum(), label="Pour les hommes.")
    expander2.metric(value=df['match'][df.gender == 0].isnull().sum(), label="Pour les femmes.")
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        Nb_total_rencontre = len(df)
        st.metric(value=Nb_total_rencontre, label="Nombre total de rencontres lors du speed dating")


    with col2:
        rdv = df3[df3.gender == '#ff00ff'].sum()
        result = rdv.match
        st.metric(value=result, label="Nombre total de match obtenu")
        expander = st.expander("considérations :")
        expander.write("Il faut que les 2 participants aient décidé de se revoir pour comptabiliser un match.")
        if 'nb_rdv' not in st.session_state:
            st.session_state.nb_rdv = result

    with col3:
        pourcentage = np.round(result * 100 / Nb_total_rencontre, 2)
        st.metric(value=pourcentage, label="soit en pourcentage")

    with col4:
        participant = nb_participant(df)
        pourcentage2 = np.round(result / participant, 2)
        st.metric(value=pourcentage2, label="Nombre de match par participant")

with tab2:
    st.subheader("Nombre de match obtenu pour les personnes de même race.")  
    df2 = df.groupby(['age', 'match'])['samerace'].value_counts().reset_index()
    df2 = df2[df2.match == 1]
    df2['samerace'] = df2['samerace'].apply(lambda x: '#FFFFFF' if x == 0 else '#E5F90B')
    st.bar_chart(df2, x="age", y="count", color='samerace', stack=False, use_container_width=True)
    annotated_text(
        "Race différente : ",
        ("", "white", "#FFFFFF"),
        " race identique : ",
        ("", "yellow", "#E5F90B"),)
    expander3 = st.expander("Valeurs manquantes :")
    expander3.metric(value=df['samerace'].isnull().sum(), label="Pour les hommes.")
    expander3.metric(value=df['samerace'].isnull().sum(), label="Pour les femmes.")
# affichage qualités
with tab3:    
    st.subheader("Suite au speed dating, il a été demandé de repenser leurs décisions.")
    age = st.select_slider("Selectionner l'age", options=list_age(df), key="attribution_bad", value=25)
    st.write("L'age selectionné est ", age, "ans")
    list_search = df.groupby(['gender', (df.age == age), (df.match == 1)], dropna=True).aggregate({'attr7_2':'mean','shar7_2':'mean','sinc7_2':'mean','intel7_2':'mean','fun7_2':'mean','amb7_2':'mean'}).reset_index()
    list_search = list_search[list_search.age == True]
    list_search = list_search[list_search.match == True]
    col1, col2 = st.columns(2, gap='medium')
    with col1:
        # Qualités recherchées par les femmes
        if 0 not in list_search.values:
            st.subheader("Pas de données féminines pour "+str(age)+ " ans")
        else:
            list_search_female = list_search[list_search['gender'] == 0].reset_index()
            list_search_female = list_search_female.drop('gender', axis=1)
            list_search_female = list_search_female.drop('age', axis=1)
            list_search_female = list_search_female.drop('match', axis=1)
            list_search_female = list_search_female.drop('index', axis=1)  
            list_search_female.dropna(inplace=True)                   
            if list_search_female.empty:
                st.subheader("Pas de données féminines pour "+str(age)+ " ans")
            else:            
                list_search_female.sort_values(ascending=True, by=0, axis=1, inplace=True)            
                list_search_female_label = list_search_female.columns.map(quality_o_7)        
                list_search_female = list_search_female.squeeze()
                explode = list()
                for i in range(len(list_search_female)-1):
                    explode.append(0)
                explode.append(0.1)
                fig3, ax3 = plt.subplots()
                st.subheader("Envers les hommes")
                ax3.pie(list_search_female, explode=explode, labels=list_search_female_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
                ax3.axis('equal')
                st.pyplot(fig3)
                expander2 = st.expander("Valeurs manquantes :")
                expander2.metric(value=df['attr7_2'][df.gender == 0][df.match == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col2:
        # Qualités recherchées par les hommes
        if 1 not in list_search.values:
            st.subheader("Pas de données masculines pour "+str(age)+ " ans")
        else:
            list_search_male = list_search[list_search['gender'] == 1].reset_index()
            list_search_male = list_search_male.drop('gender', axis=1)
            list_search_male = list_search_male.drop('age', axis=1)
            list_search_male = list_search_male.drop('match', axis=1)
            list_search_male = list_search_male.drop('index', axis=1)
            list_search_male.dropna(inplace=True)                      
            if list_search_male.empty: 
                st.subheader("Pas de données masculine pour "+str(age)+ " ans")
            else:            
                list_search_male.sort_values(ascending=True, by=0, axis=1, inplace=True) 
                list_search_male_label = list_search_male.columns.map(quality_o_7)
                list_search_male = list_search_male.squeeze()        
                explode = list()
                for i in range(len(list_search_male)-1):
                    explode.append(0)
                explode.append(0.1)
                fig4, ax4 = plt.subplots()
                st.subheader("Envers les femmes")            
                ax4.pie(list_search_male, explode=explode, labels=list_search_male_label, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
                ax4.axis('equal')
                st.pyplot(fig4)
                expander2 = st.expander("Valeurs manquantes :")
                expander2.metric(value=df['attr7_2'][df.gender == 1][df.match == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

txt = st.text_area(
    "#### **Interprétation :**",
    "Le nombre de match obtenu suite au speed dating est très faible. "
    "Nous avons en moyenne un peu plus d'un match par personne, malgré une bonne correspondance dans les qualités recherchées. "
    "L'importance de la race dans une relation se retrouve bien ici dans les matchs obtenus, nous n'avons pas de retour concernant la religion. "
    "La réévaluation de l'importance des qualités recherchées montre un changement de tendance vers l'attractivité. ",)

