import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from function import df

st.markdown("#### <font color='tomato'><ins>**PROFIL PHYSIQUE**</ins></font>", unsafe_allow_html=True)
st.subheader("""Si on regarde par tranche d’âge, ce sont les femmes qui utilisent le plus l'application, """
             """certainement par sécurité par rapport à une relation fortuite. Cela s'estompe vers la trentaine, """
             """âge moyen du premier enfant pour les pays en développement, pour reprendre par la suite.""")

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

explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(race, explode=explode, labels=race.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)