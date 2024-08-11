import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

def Objects(x):
    if x == 1.0:
        size = "Seemed like a fun night out"
    elif x == 2.0:
        size = "To meet new people"
    elif x == 3.0:
        size = "To get a date"
    elif x == 4.0:
        size = "Looking for a serious relationship"
    elif x == 5.0:
        size = "To say I did it"
    else:
        size = "Other"
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

st.markdown("#### <font color='tomato'><ins>**ATTENTES DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

objectifs = df.groupby('goal', dropna=True)['gender'].value_counts().reset_index()
objectifs['gender'] = objectifs['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
# Attente des hommes
objectifs_male = objectifs[objectifs.gender == 'Male'].set_index('goal')
objectifs_male = objectifs_male.drop('gender', axis=1)
objectifs_male.index = objectifs_male.index.map(Objects)
objectifs_male = objectifs_male.squeeze()
explode = (0.1, 0, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(objectifs_male, explode=explode, labels=objectifs_male.index, autopct='%0.0f%%', shadow=True, startangle=90)
ax1.axis('equal') 

# Attente des femmes
objectifs_female = objectifs[objectifs.gender == 'Female'].set_index('goal')
objectifs_female = objectifs_female.drop('gender', axis=1)
objectifs_female.index = objectifs_female.index.map(Objects)
objectifs_female = objectifs_female.squeeze()
explode = (0.1, 0, 0, 0, 0, 0) 
fig2, ax2 = plt.subplots()
ax2.pie(objectifs_female, explode=explode, labels=objectifs_male.index, autopct='%0.0f%%', shadow=True, startangle=90)
ax2.axis('equal')

# affichage attentes
st.divider()
col1, col2 = st.columns(2, gap='medium')
with col1:
    st.subheader("Attentes des hommes.")
    st.pyplot(fig1)
    st.metric(value=df['goal'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

with col2:
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

# affichage qualités
st.divider()
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

st.divider()
st.subheader("""Les femmes restent plus septiques par rapport aux hommes quant à trouver le bonheur avec telle application""")
happy_gender = df.groupby('exphappy', dropna=True)['gender'].value_counts().reset_index()
happy_gender['gender'] = happy_gender['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
colors = "gender"
st.bar_chart(happy_gender, x="exphappy", y="count", color=colors, stack=False, use_container_width=True)
st.metric(value=df['exphappy'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
st.metric(value=df['exphappy'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")