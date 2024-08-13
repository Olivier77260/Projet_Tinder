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

st.markdown("## <font color='tomato'><ins>**ATTENTES DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Leurs attentes***]", "##### :blue[***2. Les qualités recherchées***]", "##### :blue[***3. Leurs espoirs***]"])

with tab1:
    st.divider()
    # listing des ages
    list_age = df['age'].value_counts()
    list_age = list_age.index.sort_values(ascending=True)
    age = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="attente",
    value=25,
    )
    st.write("L'age selectionné est ", age, "ans")
    objectifs = df.groupby(['goal', (df.age == age)], dropna=True)['gender'].value_counts().reset_index()
    objectifs['gender'] = objectifs['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
    # affichage attentes    
    col1, col2 = st.columns(2, gap='medium')
    with col1:
        # Attente des hommes
        objectifs_male = objectifs[objectifs.gender == 'Male']
        objectifs_male = objectifs_male[objectifs_male.age == True].set_index('goal')
        objectifs_male = objectifs_male.drop('gender', axis=1)
        objectifs_male = objectifs_male.drop('age', axis=1)
        fig1, ax1 = plt.subplots()
        if len(objectifs_male.index) == 1:
            plt.pie(objectifs_male.index, labels=objectifs_male.index.map(Objects), autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
        else:
            objectifs_male.index = objectifs_male.index.map(Objects)
            objectifs_male = objectifs_male.squeeze()
            plt.pie(objectifs_male, labels=objectifs_male.index, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
        ax1.axis('equal') 
        st.subheader("Attentes des hommes.")
        st.pyplot(fig1)
        st.metric(value=df['goal'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col2:
        # Attente des femmes
        objectifs_female = objectifs[objectifs.gender == 'Female']
        objectifs_female = objectifs_female[objectifs_female.age == True].set_index('goal')
        objectifs_female = objectifs_female.drop('gender', axis=1)
        objectifs_female = objectifs_female.drop('age', axis=1)
        fig2, ax2 = plt.subplots()
        if len(objectifs_female.index) == 1:
            plt.pie(objectifs_female.index, labels=objectifs_female.index.map(Objects), autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
        else:
            objectifs_female.index = objectifs_female.index.map(Objects)
            objectifs_female = objectifs_female.squeeze()
            plt.pie(objectifs_female, labels=objectifs_female.index, autopct='%0.0f%%', shadow=True, startangle=90, pctdistance=0.7)
        ax2.axis('equal')
        st.subheader("Attentes des femmes.")
        st.pyplot(fig2)
        st.metric(value=df['goal'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")

list_search = df.groupby('gender', dropna=True).aggregate({'attr1_1':'sum','shar1_1':'sum','sinc1_1':'sum','intel1_1':'sum','fun1_1':'sum','amb1_1':'sum'})

# Qualités recherchées par les femmes
list_search_female = list_search.loc[list_search.index == 0]
list_search_female_label = list_search_female.columns.map(quality)
list_search_female = list_search_female.squeeze()
colors = sns.color_palette("bright")
explode = (0, 0, 0, 0.1, 0, 0)
fig3, ax3 = plt.subplots()
ax3.pie(list_search_female, explode=explode, labels=list_search_female_label, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax3.axis('equal')

# Qualités recherchées par les hommes
list_search_male = list_search.loc[list_search.index == 1]
list_search_male_label = list_search_male.columns.map(quality)
list_search_male = list_search_male.squeeze()
colors = sns.color_palette("bright")
explode = (0.1, 0, 0, 0, 0, 0)
fig4, ax4 = plt.subplots()
ax4.pie(list_search_male, explode=explode, labels=list_search_male_label, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax4.axis('equal')

with tab2:
    st.divider()
    # affichage qualités
    col3, col4 = st.columns(2, gap='medium')
    with col3:
        st.subheader("Qualités recherchées par les femmes.")
        st.pyplot(fig3)
        st.metric(value=df['attr1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'attractive'.")
        st.metric(value=df['shar1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes intéréts et passes-temps communs.")
        st.metric(value=df['sinc1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'sincere'.")
        st.metric(value=df['intel1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'intelligent'.")
        st.metric(value=df['fun1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'fun'.")
        st.metric(value=df['amb1_1'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes 'ambitious'.")

    with col4:
        st.subheader("Qualités recherchées par les hommes.")
        st.pyplot(fig4)
        st.metric(value=df['shar1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'attractive'.")
        st.metric(value=df['shar1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes intéréts et passes-temps communs.")
        st.metric(value=df['sinc1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'sincere'.")
        st.metric(value=df['intel1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'intelligent'.")
        st.metric(value=df['fun1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'fun'.")
        st.metric(value=df['amb1_1'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes 'ambitious'.")

with tab3:
    st.divider()
    st.subheader("""Les femmes restent plus septiques par rapport aux hommes quant à trouver le bonheur avec telle application""")
    happy_gender = df.groupby('exphappy', dropna=True)['gender'].value_counts().reset_index()
    happy_gender['gender'] = happy_gender['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
    colors = "gender"
    st.bar_chart(happy_gender, x="exphappy", y="count", color=colors, stack=False, use_container_width=True)
    col5, col6 = st.columns(2, gap='large')
    with col5:
        st.metric(value=df['exphappy'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
    with col6:
        st.metric(value=df['exphappy'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")