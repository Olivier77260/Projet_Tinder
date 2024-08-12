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

st.markdown("## <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

# frequence des sorties
sorties = df.groupby('date', dropna=True)['gender'].value_counts().reset_index()
sorties.date = sorties.date.map(Frequence2)

# frequence des rendez-vous
rdv = df.groupby('go_out', dropna=True)['gender'].value_counts().reset_index()
rdv.go_out = rdv.go_out.map(Frequence2)

# race masculine
race = df.groupby('imprace', dropna=True)['gender'].value_counts().reset_index()
race_male = race[race.gender == 1].set_index('imprace')
race_male = race_male.drop('gender', axis=1)
race_male.sort_values(by="count", ascending=False, inplace=True)

# race féminine
race_female = race[race.gender == 0].set_index('imprace')
race_female = race_female.drop('gender', axis=1)
race_female = race_female.drop(race_female[race_female.index==0].index)
race_female.sort_values(by="count", ascending=False, inplace=True)

# religion masculine
religion = df.groupby('imprelig', dropna=True)['gender'].value_counts().reset_index()
religion_male = religion[religion.gender == 1].set_index('imprelig')
religion_male = religion_male.drop('gender', axis=1)
religion_male.sort_values(by="count", ascending=False, inplace=True)

# religion féminine
religion_female = religion[religion.gender == 0].set_index('imprelig')
religion_female = religion_female.drop('gender', axis=1)
religion_female.sort_values(by="count", ascending=False, inplace=True)

tab1, tab2, tab3 = st.tabs(["##### :blue[***1. Sorties et rendez-vous***]", "##### :blue[***2. Races***]", "##### :blue[***3. Religions***]"])

# affichage des rdv et sorties
with tab1:
    st.divider()
    col2, col3 = st.columns(2, gap='large')
    with col2:
        st.subheader("Fréquence des sorties.")
        st.bar_chart(sorties, x='date', y='count', stack=False, y_label="Fréquence des sorties", use_container_width=True, color="gender", horizontal=True)
        st.metric(value=df.date.isnull().sum(), label="Nombre de valeurs manquantes.")

    with col3:
        st.subheader("Fréquence des rendez-vous.")        
        st.bar_chart(rdv, x='go_out', y='count', stack=False, y_label="Fréquence des rendez-vous", use_container_width=True, color="gender", horizontal=True)
        st.metric(value=df.go_out.isnull().sum(), label="Nombre de valeurs manquantes.")

    expander = st.expander("A noter")
    expander.write('''
        Une grandes majorité des participant sont des personnes qui sortent trés souvent. 
        En oposition avec les rendez-vous.
    ''')

# affichage race
with tab2:
    st.divider()
    st.subheader("Importance de la race dans la relation.")
    col4, col5 = st.columns(2, gap='medium')
    with col4:
        st.subheader("Chez les hommes :")
        st.bar_chart(race_male, y="count", stack=False, use_container_width=True)
        st.metric(value=df['imprace'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col5:
        st.subheader("Chez les femmes :")
        st.bar_chart(race_female, y="count", stack=False, use_container_width=True)
        st.metric(value=df['imprace'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")

# affichage religion
with tab3:
    st.divider()
    st.subheader("Importance de la religion.")
    col4, col5 = st.columns(2, gap='medium')
    with col4:
        st.subheader("Chez les hommes :")
        st.bar_chart(religion_male, y="count", stack=False, use_container_width=True)
        st.metric(value=df['imprelig'][df.gender == 1].isnull().sum(), label="Nombre de valeurs manquantes.")

    with col5:
        st.subheader("Chez les femmes :")
        st.bar_chart(religion_female, y="count", stack=False, use_container_width=True)
        st.metric(value=df['imprelig'][df.gender == 0].isnull().sum(), label="Nombre de valeurs manquantes.")