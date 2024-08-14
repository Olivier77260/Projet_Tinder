import streamlit as st

def Frequence2(x):
    if x == 1:
        size = "1_Several times a week"
    elif x == 2:
        size = "2_Twice a week"
    elif x == 3:
        size = "3_Once a week"
    elif x == 4:
        size = "4_Twice a month"
    elif x == 5:
        size = "5_Once a month"
    elif x == 6:
        size = "6_Several times a year"
    else:
        size = "7_Almost never"
    return size

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

df2 = df.groupby(['go_out', 'gender', 'date', 'age', 'imprace', 'imprelig'])['iid'].value_counts().reset_index()

st.markdown("## <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

# frequence des rendez-vous
sorties = df2.groupby('date', dropna=True)['gender'].value_counts().reset_index()
sorties['gender'] = sorties['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
sorties.date = sorties.date.map(Frequence2)

# frequence des sorties
rdv = df2.groupby('go_out', dropna=True)['gender'].value_counts().reset_index()
rdv['gender'] = rdv['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
rdv.go_out = rdv.go_out.map(Frequence2)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Sorties et rendez-vous***]", "##### :blue[***2. Races***]", "##### :blue[***3. Religions***]"])

# affichage des rdv et sorties
with tab1:
    st.divider()
    col2, col3 = st.columns(2, gap='large')
    with col2:
        st.subheader("Fréquence des rendez-vous.")
        st.bar_chart(sorties, x='date', y='count', stack=False, y_label="Fréquence des rendez-vous", use_container_width=True, color="gender", horizontal=True)
        st.metric(value=df2['date'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
        st.metric(value=df2['date'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")

    with col3:
        st.subheader("Fréquence des sorties.")        
        st.bar_chart(rdv, x='go_out', y='count', stack=False, y_label="Fréquence des sorties", use_container_width=True, color="gender", horizontal=True)
        st.metric(value=df2['go_out'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
        st.metric(value=df2['go_out'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")

    expander = st.expander("A noter")
    expander.write('''
        Une grandes majorité des participant sont des personnes qui sortent trés souvent. 
        En oposition avec les rendez-vous.
    ''')

# listing des ages
list_age = df2['age'].value_counts()
list_age = list_age.index.sort_values(ascending=True) 

# affichage race
with tab2:
    st.divider()   
    age_race = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="race",
    value=25,
    )
    race = df2.groupby(['imprace',(df2.age == age_race)], dropna=True)['gender'].value_counts().reset_index()
    race = race[race.age == True]
    race['gender'] = race['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
    race = race.drop(race[race.index==0].index)
    st.write("L'age selectionné est ", age_race, "ans")
    st.subheader("Importance interraciale dans une relation :")
    st.bar_chart(race, x="imprace", y="count", x_label="Importance de la race", stack=False, use_container_width=True, color="gender")
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.metric(value=df2['imprace'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
    with col2:
        st.metric(value=df2['imprace'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")

# affichage religion
with tab3:
    st.divider()   
    age_religion = st.select_slider(
    "Selectionner l'age",
    options=list_age,
    key="religion",
    value=25,
    )
    religion = df2.groupby(["imprelig",(df2.age == age_religion)], as_index=False)["gender"].value_counts()
    religion = religion[religion.age == True]
    religion['gender'] = religion['gender'].apply(lambda x: '#ff00ff' if x == 0 else '#4169e1')
    st.write("L'age selectionné est ", age_religion, "ans")
    st.subheader("Importance de la religion dans une relation.")
    st.bar_chart(religion, x="imprelig", y="count", stack=False, use_container_width=True, color="gender", x_label="Importance de la religion")
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.metric(value=df2['imprelig'][df2.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes chez les femmes.")
    with col2:
        st.metric(value=df2['imprelig'][df2.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes chez les hommes.")