import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

def Objects(x):
    if x == 1.0:
        size = "Passer une agréable soirée"
    elif x == 2.0:
        size = "Rencontrer des nouvelles personnes"
    elif x == 3.0:
        size = "Avoir un rendez-vous"
    elif x == 4.0:
        size = "Rechercher une relation sérieuse"
    elif x == 5.0:
        size = "Dire que je l'ai fait !!!"
    else:
        size = "Autre"
    return size

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

df2 = df.groupby(['exphappy', 'gender', 'age', 'goal', 'attr1_1','shar1_1','sinc1_1','intel1_1','fun1_1','amb1_1'])['iid'].value_counts().reset_index()

st.markdown("## <font color='tomato'><ins>**ATTENTES DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Leurs attentes***]", "##### :blue[***2. Les qualités recherchées***]", "##### :blue[***3. Leurs espoirs***]"])

list_age = df2['age'].value_counts()
list_age = list_age.index.sort_values(ascending=True)
with tab1:
    st.divider()
    # listing des ages
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="attente",
    value=25,
    )
    st.write("L'age selectionné est ", age, "ans")
    objectifs = df2.groupby(['goal', (df2.age == age)], dropna=True)['gender'].value_counts().reset_index()
    objectifs = objectifs[objectifs.age == True]
    objectifs['gender'] = objectifs['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
    # affichage attentes    
    col1, col2 = st.columns(2, gap='medium')
    with col1:
        # Attente des hommes
        objectifs_male = objectifs[objectifs.gender == 'Male']
        objectifs_male = objectifs_male[objectifs_male.age == True].set_index('goal')
        objectifs_male = objectifs_male.drop('gender', axis=1)
        objectifs_male = objectifs_male.drop('age', axis=1)
        explode = list()
        for i in range(len(objectifs_male)-1):
            explode.append(0)
        explode.append(0.1)
        fig1, ax1 = plt.subplots()
        if len(objectifs_male.index) == 0:
            st.subheader("Pas de données masculine pour "+str(age)+ " ans")
        else:
            if len(objectifs_male.index) == 1:
                ax1.pie(objectifs_male.index, labels=objectifs_male.index.map(Objects), autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            else:
                objectifs_male.index = objectifs_male.index.map(Objects)
                objectifs_male.sort_values(ascending=True, inplace=True, by="count") 
                objectifs_male = objectifs_male.squeeze()
                ax1.pie(objectifs_male, explode=explode, labels=objectifs_male.index, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax1.axis('equal') 
            st.subheader("Attentes des hommes.")
            st.pyplot(fig1)
        st.metric(value=df2['goal'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col2:
        # Attente des femmes
        objectifs_female = objectifs[objectifs.gender == 'Female']
        objectifs_female = objectifs_female[objectifs_female.age == True].set_index('goal')
        objectifs_female = objectifs_female.drop('gender', axis=1)
        objectifs_female = objectifs_female.drop('age', axis=1)
        explode = list()
        for i in range(len(objectifs_female)-1):
            explode.append(0)
        explode.append(0.1)
        fig2, ax2 = plt.subplots()
        if len(objectifs_female.index) == 0:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            if len(objectifs_female.index) == 1:
                ax2.pie(objectifs_female.index, labels=objectifs_female.index.map(Objects), autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            else:
                objectifs_female.index = objectifs_female.index.map(Objects) 
                objectifs_female.sort_values(ascending=True, inplace=True, by="count") 
                objectifs_female = objectifs_female.squeeze()            
                ax2.pie(objectifs_female, explode=explode, labels=objectifs_female.index, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax2.axis('equal')
            st.subheader("Attentes des femmes.")
            st.pyplot(fig2)
        st.metric(value=df2['goal'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")

with tab2:
    st.divider()
    # listing des ages
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="qualite",
    value=25,
    )
    st.write("L'age selectionné est ", age, "ans")
    list_search = df2.groupby(['gender', (df2.age == age)], dropna=True).aggregate({'attr1_1':'sum','shar1_1':'sum','sinc1_1':'sum','intel1_1':'sum','fun1_1':'sum','amb1_1':'sum'}).reset_index()
    list_search = list_search[list_search.age == True]    
    # affichage qualités
    col3, col4 = st.columns(2, gap='medium')
    with col3:
        # Qualités recherchées par les femmes
        list_search_female = list_search[list_search['gender'] == 0].reset_index()
        list_search_female = list_search_female.drop('gender', axis=1)
        list_search_female = list_search_female.drop('age', axis=1)
        if list_search_female.empty:
            st.subheader("Pas de données féminine pour "+str(age)+ " ans")
        else:
            list_search_female.sort_values(ascending=True, by=0, axis=1, inplace=True)  
            list_search_female = list_search_female.drop('index', axis=1)      
            list_search_female_label = list_search_female.columns.map(quality)        
            list_search_female = list_search_female.squeeze()
            explode = list()
            for i in range(len(list_search_female)-1):
                explode.append(0)
            explode.append(0.1)
            fig3, ax3 = plt.subplots()

            st.subheader("Qualités recherchées par les femmes.")
            ax3.pie(list_search_female, explode=explode, labels=list_search_female_label,  autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax3.axis('equal')
            st.pyplot(fig3)   
        st.metric(value=df2['attr1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'attractive'.")
        st.metric(value=df2['shar1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes intéréts et passes-temps communs.")
        st.metric(value=df2['sinc1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'sincere'.")
        st.metric(value=df2['intel1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'intelligent'.")
        st.metric(value=df2['fun1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'fun'.")
        st.metric(value=df2['amb1_1'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'ambitious'.")

    with col4:
        # Qualités recherchées par les hommes
        list_search_male = list_search[list_search['gender'] == 1].reset_index()      
        list_search_male = list_search_male.drop('gender', axis=1)
        list_search_male = list_search_male.drop('age', axis=1)
        if list_search_male.empty: 
            st.subheader("Pas de données masculine pour "+str(age)+ " ans")
        else:
            list_search_male.sort_values(ascending=True, by=0, axis=1, inplace=True)
            list_search_male = list_search_male.drop('index', axis=1)  
            list_search_male_label = list_search_male.columns.map(quality)        
            list_search_male = list_search_male.squeeze()        
            explode = list()
            for i in range(len(list_search_male)-1):
                explode.append(0)
            explode.append(0.1)
            fig4, ax4 = plt.subplots()

            st.subheader("Qualités recherchées par les hommes.")            
            ax4.pie(list_search_male, explode=explode, labels=list_search_male_label, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
            ax4.axis('equal')
            st.pyplot(fig4)
        st.metric(value=df2['shar1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'attractive'.")
        st.metric(value=df2['shar1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes intéréts et passes-temps communs.")
        st.metric(value=df2['sinc1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'sincere'.")
        st.metric(value=df2['intel1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'intelligent'.")
        st.metric(value=df2['fun1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'fun'.")
        st.metric(value=df2['amb1_1'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'ambitious'.")

with tab3:
    st.divider()
    st.subheader("""Les femmes restent plus septiques par rapport aux hommes quant à trouver le bonheur avec telle application""")
    happy_gender = df2.groupby('exphappy', dropna=True)['gender'].value_counts().reset_index()
    happy_gender['gender'] = happy_gender['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
    colors = "gender"
    st.bar_chart(happy_gender, x="exphappy", y="count", x_label="Espoir d'une rencontre heureuse", color=colors, stack=False, use_container_width=True)
    col5, col6 = st.columns(2, gap='large')
    with col5:
        st.metric(value=df2['exphappy'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
    with col6:
        st.metric(value=df2['exphappy'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")