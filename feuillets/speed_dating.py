import streamlit as st
import matplotlib.pyplot as plt

def quality_o(x):
    if x == 'attr2_1':
        size = "Attractive"
    elif x == 'sinc2_1':
        size = "Sincere"
    elif x == 'intel2_1':
        size = "Intelligent"
    elif x == 'fun2_1':
        size = "Fun"
    elif x == 'amb2_1':
        size = "Ambitious"
    else:
        size = "Has shared interests/hobbies"
    return size

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

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

df2 = df.groupby(['wave', 'dec_o', 'exphappy', 'gender', 'age', 'goal', 'attr2_1','shar2_1','sinc2_1','intel2_1','fun2_1','amb2_1'], dropna=False)['iid'].value_counts().reset_index()
df3 = df.groupby(['dec_o', 'exphappy', 'gender', 'age', 'goal', 'pf_o_amb', 'pf_o_att', 'pf_o_fun', 'pf_o_int', 'pf_o_sha', 'pf_o_sin'], dropna=False)['iid'].value_counts().reset_index()

st.markdown("## <font color='tomato'><ins>**SPEED DATING**</ins></font>", unsafe_allow_html=True)

st.subheader("Le speed dating est un rendez-vous d'une durée d'environ 4 mn avec le partenaire selectionné.")

list_age = df2['age'].value_counts()
list_age = list_age.index.sort_values(ascending=True)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Qualités recherchées***]", "##### :blue[***2. qualités attribuées par hommes***]", "##### :blue[***3. qualités attribuées par les femmes***]"])
# slider de selection de l'age
age = st.select_slider("Selectionner l'age", options=list_age, key="attribution_bad", value=25)

# affichage qualités
with tab1:
    st.subheader("Qualités recherchées chez le sexe opposé lors de ce rendez-vous.")
    # qualité noteé dans les waves de 1 à 5 et de 10 à 21, les waves 6 à 9 sont non conformes à la notation demandée.
    st.write("L'age selectionné est ", age, "ans")
    wave1a5_10a21 = df2[(df2['wave'] <= 5) | (df2['wave'] >=10)]
    wave1a5_10a21 = wave1a5_10a21.fillna(0)
    list_search = wave1a5_10a21.groupby(['gender', (wave1a5_10a21.age == age)]).aggregate({'attr2_1':'mean','shar2_1':'mean','sinc2_1':'mean','intel2_1':'mean','fun2_1':'mean','amb2_1':'mean'}).reset_index()
    list_search = list_search[list_search.age == True]    
    col1, col2 = st.columns(2, gap='medium')
    with col1:
        # Qualités recherchées par les femmes        
        list_search_female = list_search[list_search['gender'] == 0].reset_index()
        list_search_female = list_search_female.drop('gender', axis=1)
        list_search_female = list_search_female.drop('age', axis=1)        
        list_search_female = list_search_female.drop('index', axis=1)
        if list_search_female.empty:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            list_search_female.sort_values(ascending=True, by=0, axis=1, inplace=True)    
            list_search_female_label = list_search_female.columns.map(quality_o)        
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
            st.metric(value=df2['attr2_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col2:
        # Qualités recherchées par les hommes
        list_search_male = list_search[list_search['gender'] == 1].reset_index()
        list_search_male = list_search_male.drop('gender', axis=1)
        list_search_male = list_search_male.drop('age', axis=1)
        if list_search_male.empty: 
            st.subheader("Pas de données masculine pour "+str(age)+ " ans")
        else:
            list_search_male.sort_values(ascending=True, by=0, axis=1, inplace=True) 
            list_search_male_label = list_search_male.columns.map(quality_o)        
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
            st.metric(value=df2['attr2_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

preference_positive = df3[(df3.dec_o == 1)]
preference_positive = preference_positive.fillna(0)
research_good = preference_positive.groupby(['gender', (preference_positive.age == age)]).aggregate({'pf_o_att':'mean','pf_o_sin':'mean','pf_o_int':'mean','pf_o_fun':'mean','pf_o_amb':'mean','pf_o_sha':'mean'}).reset_index()
research_good = research_good[research_good.age == True] 

preference_negative = df3[(df3.dec_o == 0)]
preference_negative = preference_negative.fillna(0)
research_bad = preference_negative.groupby(['gender', (preference_negative.age == age)]).aggregate({'pf_o_att':'mean','pf_o_sin':'mean','pf_o_int':'mean','pf_o_fun':'mean','pf_o_amb':'mean','pf_o_sha':'mean'}).reset_index()
research_bad = research_bad[research_bad.age == True]

#affichage qualités des hommes
with tab2:
    st.subheader("Attribution des qualités par les hommes suite au speed dating.")
    # qualités attibuées sans suite de rdv
    st.write("L'age selectionné est ", age, "ans")
    col3, col4 = st.columns(2, gap='medium')
    with col3:
         # Attribution des qualités par les hommes         
        list_search_bad_male = research_bad[research_bad['gender'] == 1].reset_index()    
        list_search_bad_male = list_search_bad_male.drop('gender', axis=1)
        list_search_bad_male = list_search_bad_male.drop('age', axis=1)            
        list_search_bad_male = list_search_bad_male.drop('index', axis=1)        
        if list_search_bad_male.empty:
            st.subheader("Pas de données masculine pour "+str(age)+ " ans")
        else:
            list_search_bad_male.sort_values(ascending=True, by=0, axis=1, inplace=True)     
            list_search_bad_male_label = list_search_bad_male.columns.map(quality_pf_o)             
            list_search_bad_male = list_search_bad_male.squeeze()
            explode = list()            
            for i in range(len(list_search_bad_male)-1):
                explode.append(0)
            explode.append(0.1)         
            fig1, ax1 = plt.subplots()
            st.subheader("Envers les femmes sans suite de rendez-vous")
            ax1.pie(list_search_bad_male, explode=explode, labels=list_search_bad_male_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax1.axis('equal')
            st.pyplot(fig1)
            st.metric(value=df3['pf_o_att'][df3.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    # qualités attibuées avec rdv
    with col4:
         # Attribution des qualités par les hommes         
        list_search_good_male = research_good[research_good['gender'] == 1].reset_index()    
        list_search_good_male = list_search_good_male.drop('gender', axis=1)
        list_search_good_male = list_search_good_male.drop('age', axis=1)            
        list_search_good_male = list_search_good_male.drop('index', axis=1)        
        if list_search_good_male.empty:
            st.subheader("Pas de données masculine pour "+str(age)+ " ans")
        else:
            list_search_good_male.sort_values(ascending=True, by=0, axis=1, inplace=True)     
            list_search_good_male_label = list_search_good_male.columns.map(quality_pf_o) 
            
            list_search_good_male = list_search_good_male.squeeze()
            explode = list()            
            for i in range(len(list_search_good_male)-1):
                explode.append(0)
            explode.append(0.1)
            fig5, ax5 = plt.subplots()
            st.subheader("Envers les femmes avec rendez-vous")
            ax5.pie(list_search_good_male, explode=explode, labels=list_search_good_male_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax5.axis('equal')
            st.pyplot(fig5)
            st.metric(value=df3['pf_o_att'][df3.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

#affichage qualités des femmes
with tab3:
    st.subheader("Attribution des qualités par les femmes suite au speed dating.")
    st.write("L'age selectionné est ", age, "ans")
    col3, col4 = st.columns(2, gap='medium')
    with col3:
        # Attribution des qualités par les femmes sans rendez-vous
        list_search_female = research_bad[research_bad['gender'] == 0].reset_index()
        list_search_female = list_search_female.drop('gender', axis=1)
        list_search_female = list_search_female.drop('age', axis=1)        
        list_search_female = list_search_female.drop('index', axis=1)
        if list_search_female.empty:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            list_search_female.sort_values(ascending=True, by=0, axis=1, inplace=True)     
            list_search_female_label = list_search_female.columns.map(quality_pf_o)        
            list_search_female = list_search_female.squeeze()
            explode = list()            
            for i in range(len(list_search_female)-1):
                explode.append(0)
            explode.append(0.1)
            fig6, ax6 = plt.subplots()
            st.subheader("Envers les hommes sans suite de rendez-vous")
            ax6.pie(list_search_female, explode=explode, labels=list_search_female_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax6.axis('equal')
            st.pyplot(fig6)
            st.metric(value=df3['pf_o_att'][df3.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col4:
            # Attribution des qualités par les femmes avec rendez-vous
            list_search_female_good = research_good[research_good['gender'] == 0].reset_index()
            list_search_female_good = list_search_female_good.drop('gender', axis=1)
            list_search_female_good = list_search_female_good.drop('age', axis=1)        
            list_search_female_good = list_search_female_good.drop('index', axis=1)
            if list_search_female_good.empty:
                st.subheader("Pas de données féminine pour "+str(age)+ " ans")
            else:
                list_search_female_good.sort_values(ascending=True, by=0, axis=1, inplace=True)     
                list_search_female_good_label = list_search_female_good.columns.map(quality_pf_o)        
                list_search_female_good = list_search_female_good.squeeze()
                explode = list()                
                for i in range(len(list_search_female_good)-1):
                    explode.append(0)
                explode.append(0.1)          
                fig2, ax2 = plt.subplots()
                st.subheader("Envers les hommes avec rendez-vous")
                ax2.pie(list_search_female_good, explode=explode, labels=list_search_female_good_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
                ax2.axis('equal')
                st.pyplot(fig2)
                st.metric(value=df3['pf_o_att'][df3.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")