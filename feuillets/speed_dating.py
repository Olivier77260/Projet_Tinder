import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

df2 = df.groupby(['exphappy', 'gender', 'age', 'goal', 'attr2_1','shar2_1','sinc2_1','intel2_1','fun2_1','amb2_1'])['iid'].value_counts().reset_index()

st.markdown("## <font color='tomato'><ins>**SPEED DATING**</ins></font>", unsafe_allow_html=True)

st.subheader("Le speed dating est un rendez-vous d'une durée d'environ 4 mn avec le partenaire selectionné.")

list_age = df2['age'].value_counts()
list_age = list_age.index.sort_values(ascending=True)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Qualités recherchées***]", "##### :blue[***2. qualités attribuées sans suite de rdv***]", "##### :blue[***3. qualités attribuées avec demande de rendez-vous***]"])

with tab1:
    st.subheader("Qualités recherchées chez le sexe opposé lors de ce rendez-vous.")
    st.divider()
    # listing des ages
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="qualite_rdv",
    value=25,
    )
    # qualité noteé dans les waves de 1 à 5 et de 10 à 21, les waves 6 à 9 sont non conformes à la notation demandée.
    st.write("L'age selectionné est ", age, "ans")
    wave1a5_10a21 = df[(df['wave'] <= 5) | (df['wave'] >=10)]
    wave1a5_10a21 = wave1a5_10a21.fillna(0)
    research = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['fun2_1'].mean().reset_index(name='fun2_1').sort_values(ascending=True, by='iid')
    amb2_1 = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['amb2_1'].mean().reset_index(name='amb2_1').sort_values(ascending=True, by='iid')
    research.insert(loc=len(research.columns), column='amb2_1', value=amb2_1['amb2_1'])
    shar2_1 = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['shar2_1'].mean().reset_index(name='shar2_1').sort_values(ascending=True, by='iid')
    research.insert(loc=len(research.columns), column='shar2_1', value=shar2_1['shar2_1'])
    sinc2_1 = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['sinc2_1'].mean().reset_index(name='sinc2_1').sort_values(ascending=True, by='iid')
    research.insert(loc=len(research.columns), column='sinc2_1', value=sinc2_1['sinc2_1'])
    intel2_1 = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['intel2_1'].mean().reset_index(name='intel2_1').sort_values(ascending=True, by='iid')
    research.insert(loc=len(research.columns), column='intel2_1', value=intel2_1['intel2_1'])
    attr2_1 = wave1a5_10a21.groupby(['wave', 'age', 'iid', 'gender'])['attr2_1'].mean().reset_index(name='attr2_1').sort_values(ascending=True, by='iid')
    research.insert(loc=len(research.columns), column='attr2_1', value=attr2_1['attr2_1'])
    list_search = research.groupby(['gender', (research.age == age)]).aggregate({'attr2_1':'mean','shar2_1':'mean','sinc2_1':'mean','intel2_1':'mean','fun2_1':'mean','amb2_1':'mean'}).reset_index()
    list_search = list_search[list_search.age == True]
    # affichage qualités
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

#affichage preferences
with tab2:
    st.subheader("Attribution des qualités sans suite de rendez-vous.")
    st.divider()
    # listing des ages
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="attribution_bad",
    value=25,
    )
    # qualités attibuées sans suite de rdv
    st.write("L'age selectionné est ", age, "ans")
    preference = df[(df.dec_o == 0)]
    preference = preference.fillna(0)
    research_bad = preference.groupby(['age', 'iid', 'gender'])['pf_o_att'].mean().reset_index(name='pf_o_att').sort_values(ascending=True, by='iid')
    pf_o_sin = preference.groupby(['age', 'iid', 'gender'])['pf_o_sin'].mean().reset_index(name='pf_o_sin').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_sin', value=pf_o_sin['pf_o_sin'])
    pf_o_int = preference.groupby(['age', 'iid', 'gender'])['pf_o_int'].mean().reset_index(name='pf_o_int').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_int', value=pf_o_int['pf_o_int'])
    pf_o_fun = preference.groupby(['age', 'iid', 'gender'])['pf_o_fun'].mean().reset_index(name='pf_o_fun').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_fun', value=pf_o_fun['pf_o_fun'])
    pf_o_amb = preference.groupby(['age', 'iid', 'gender'])['pf_o_amb'].mean().reset_index(name='pf_o_amb').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_amb', value=pf_o_amb['pf_o_amb'])
    pf_o_sha = preference.groupby(['age', 'iid', 'gender'])['pf_o_sha'].mean().reset_index(name='pf_o_sha').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_sha', value=pf_o_sha['pf_o_sha'])
    research_bad = research_bad.groupby(['gender', (research_bad.age == age)]).aggregate({'pf_o_att':'mean','pf_o_sin':'mean','pf_o_int':'mean','pf_o_fun':'mean','pf_o_amb':'mean','pf_o_sha':'mean'}).reset_index()
    research_bad = research_bad[research_bad.age == True] 

    col3, col4 = st.columns(2, gap='medium')
    with col3:
         # Attribution des qualités par les hommes         
        list_search_bad_male = research_bad[research_bad['gender'] == 1].reset_index()    
        list_search_bad_male = list_search_bad_male.drop('gender', axis=1)
        list_search_bad_male = list_search_bad_male.drop('age', axis=1)            
        list_search_bad_male = list_search_bad_male.drop('index', axis=1)        
        if list_search_female.empty:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            list_search_bad_male.sort_values(ascending=True, by=0, axis=1, inplace=True)     
            list_search_bad_male_label = list_search_bad_male.columns.map(quality_pf_o)             
            list_search_bad_male = list_search_bad_male.squeeze()
            explode = list()
            explode.append(0.1)
            for i in range(len(list_search_bad_male)-1):
                explode.append(0)            
            fig1, ax1 = plt.subplots()
            st.subheader("Envers les femmes")
            ax1.pie(list_search_bad_male, explode=explode, labels=list_search_bad_male_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax1.axis('equal')
            st.pyplot(fig1)

    with col4:
        # Attribution des qualités par les femmes
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
            explode.append(0.1)
            for i in range(len(list_search_female)-1):
                explode.append(0)            
            fig2, ax2 = plt.subplots()
            st.subheader("Envers les hommes")
            ax2.pie(list_search_female, explode=explode, labels=list_search_female_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax2.axis('equal')
            st.pyplot(fig2)

with tab3:
    st.subheader("Attribution des qualités avec demande de rendez-vous.")
    st.divider()
    # listing des ages
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="attribution_good",
    value=25,
    )
    # qualités attibuées avec demande de rdv
    st.write("L'age selectionné est ", age, "ans")
    preference = df[(df.dec_o == 1)]
    preference = preference.fillna(0)
    research_bad = preference.groupby(['age', 'iid', 'gender'])['pf_o_att'].mean().reset_index(name='pf_o_att').sort_values(ascending=True, by='iid')
    pf_o_sin = preference.groupby(['age', 'iid', 'gender'])['pf_o_sin'].mean().reset_index(name='pf_o_sin').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_sin', value=pf_o_sin['pf_o_sin'])
    pf_o_int = preference.groupby(['age', 'iid', 'gender'])['pf_o_int'].mean().reset_index(name='pf_o_int').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_int', value=pf_o_int['pf_o_int'])
    pf_o_fun = preference.groupby(['age', 'iid', 'gender'])['pf_o_fun'].mean().reset_index(name='pf_o_fun').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_fun', value=pf_o_fun['pf_o_fun'])
    pf_o_amb = preference.groupby(['age', 'iid', 'gender'])['pf_o_amb'].mean().reset_index(name='pf_o_amb').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_amb', value=pf_o_amb['pf_o_amb'])
    pf_o_sha = preference.groupby(['age', 'iid', 'gender'])['pf_o_sha'].mean().reset_index(name='pf_o_sha').sort_values(ascending=True, by='iid')
    research_bad.insert(loc=len(research_bad.columns), column='pf_o_sha', value=pf_o_sha['pf_o_sha'])
    research_bad = research_bad.groupby(['gender', (research_bad.age == age)]).aggregate({'pf_o_att':'mean','pf_o_sin':'mean','pf_o_int':'mean','pf_o_fun':'mean','pf_o_amb':'mean','pf_o_sha':'mean'}).reset_index()
    research_bad = research_bad[research_bad.age == True] 

    col3, col4 = st.columns(2, gap='medium')
    with col3:
         # Attribution des qualités par les hommes         
        list_search_bad_male = research_bad[research_bad['gender'] == 1].reset_index()    
        list_search_bad_male = list_search_bad_male.drop('gender', axis=1)
        list_search_bad_male = list_search_bad_male.drop('age', axis=1)            
        list_search_bad_male = list_search_bad_male.drop('index', axis=1)        
        if list_search_female.empty:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            list_search_bad_male.sort_values(ascending=True, by=0, axis=1, inplace=True)     
            list_search_bad_male_label = list_search_bad_male.columns.map(quality_pf_o) 
            
            list_search_bad_male = list_search_bad_male.squeeze()
            explode = list()            
            for i in range(len(list_search_bad_male)-1):
                explode.append(0)
            explode.append(0.1)
            fig5, ax5 = plt.subplots()
            st.subheader("Envers les femmes")
            ax5.pie(list_search_bad_male, explode=explode, labels=list_search_bad_male_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax5.axis('equal')
            st.pyplot(fig5)

    with col4:
        # Attribution des qualités par les femmes
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
            st.subheader("Envers les hommes")
            ax6.pie(list_search_female, explode=explode, labels=list_search_female_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax6.axis('equal')
            st.pyplot(fig6)