import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("#### <font color='tomato'><ins>**PROFIL PHYSIQUE**</ins></font>", unsafe_allow_html=True)
st.subheader("""Si on regarde par tranche d’âge, ce sont les femmes qui utilisent le plus l'application, """
             """certainement par sécurité par rapport à une relation fortuite. Cela s'estompe vers la trentaine, """
             """âge moyen du premier enfant pour les pays en développement, pour reprendre par la suite.""")

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

age_gender = df.groupby('age')['gender'].value_counts().reset_index()
age_gender['gender'] = age_gender['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
st.bar_chart(age_gender, x="age", y="count", color="gender", stack=False, use_container_width=True)

st.subheader("La race majoritairement représentée est de type European/Caucasian-American suivie par le type Asian/Pacific Islander/Asian-American.")

race = df.race.value_counts()
def Races(x):
    if x == 1.0:
        size = "Black/African American"
    elif x == 2.0:
        size = "European/Caucasian-American"
    elif x == 3.0:
        size = "Latino/Hispanic American"
    elif x == 4.0:
        size = "Asian/Pacific Islander/Asian-American"
    elif x == 5.0:
        size = "Native American"
    else:
        size = "Other"
    return size
race.index = race.index.map(Races)
color = sns.color_palette("bright")
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(race, explode=explode, labels=race.index, colors=color, autopct="%0.0f%%", shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st.metric(value=df['race'].isnull().sum(), label="Nombre de participant n'ayant pas renseigné son origine.")
st.checkbox("Suppression des valeurs manquantes", key="del_from")