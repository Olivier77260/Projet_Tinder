import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("#### <font color='tomato'><ins>**PROFIL SOCIAL**</ins></font>", unsafe_allow_html=True)
st.checkbox("Suppression des valeurs manquantes", key="del_from")
adresses = pd.read_csv('adresses.csv', sep=';')
st.subheader("Carte du monde d'où viennet les participants.")
st.map(adresses, latitude='latitude', longitude='longitude', zoom=1.5, color='#f20202', size='total')
st.subheader("Le domaine des études reste conforme aux professions exercées.")
count = df.field_cd.value_counts().sort_values(ascending=False)
other = count[count<count.quantile(.25)].sum()
count['others'] = other
count = count[count>=count.quantile(.25)]
def student(x):
    if x == 1.0:
        size = "Law"
    elif x == 2.0:
        size = "Math"
    elif x == 3.0:
        size = "Social Science, Psychologist"
    elif x == 4.0:
        size = "Medical Science, Pharmaceuticals, and Bio Tech"
    elif x == 5.0:
        size = "Engineering"
    elif x == 6.0:
        size = "English/Creative Writing/ Journalism"
    elif x == 7.0:
        size = "History/Religion/Philosophy"
    elif x == 8.0:
        size = "Business/Econ/Finance"
    elif x == 9.0:
        size = "Education, Academia"
    elif x == 10.0:
        size = "Biological Sciences/Chemistry/Physics"
    elif x == 11.0:
        size = "Social Work"
    elif x == 12.0:
        size = "Undergrad/undecided"
    elif x == 13.0:
        size = "Political Science/International Affairs"
    elif x == 14.0:
        size = "Film"
    elif x == 15.0:
        size = "Fine Arts/Arts Administration"
    elif x == 16.0:
        size = "Languages"
    elif x == 17.0:
        size = "Architecture"
    else:
        size = "Other"
    return size

count.index = count.index.map(student)
colors = sns.color_palette("bright")
labels = count.index

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(count, explode=explode, labels=labels, autopct="%0.0f%%", shadow=True, startangle=180, pctdistance=0.8)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.metric(value=df.field_cd.isnull().sum(), label="Nombre de participant n'ayant pas renseigné son domaine d'étude.")

st.divider()
st.subheader("Une vingtaine de professions sont representées, majoritairement des métiers dits intellectuels.")
carriere = df.career_c.value_counts()
other2 = carriere[carriere<carriere.quantile(.50)].sum()
carriere['others'] = other2
carriere = carriere[carriere>=carriere.quantile(.50)]

def ProfilSociaux(x):
    if x == 1.0:
        size = "Lawyer"
    elif x == 2.0:
        size = "Academic/Research"
    elif x == 3.0:
        size = "Psychologist"
    elif x == 4.0:
        size = "Doctor/Medicine"
    elif x == 5.0:
        size = "Engineer"
    elif x == 6.0:
        size = "Creative Arts/Entertainment"
    elif x == 7.0:
        size = "Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/Admin"
    elif x == 8.0:
        size = "Real Estate"
    elif x == 9.0:
        size = "International/Humanitarian Affairs"
    elif x == 10.0:
        size = "Undecided"
    elif x == 11.0:
        size = "Social Work"
    elif x == 12.0:
        size = "Speech Pathology"
    elif x == 13.0:
        size = "Politics"
    elif x == 14.0:
        size = "Pro sports/Athletics"
    elif x == 15.0:
        size = "Other"
    elif x == 16.0:
        size = "Journalism"
    elif x == 17.0:
        size = "Architecture"
    else:
        size = "Other"
    return size

carriere.index = carriere.index.map(ProfilSociaux)
labels = carriere.index

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(carriere, explode=explode, labels=labels, autopct="%0.0f%%", shadow=False, startangle=180, colors=colors, pctdistance=0.8)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.metric(value=df.career_c.isnull().sum(), label="Nombre de participant n'ayant pas renseigné sa profession.")

st.divider()
st.subheader("Les hobbies, source de rencontres, sont trés diversifiés.")

list_activites = df.loc[:, 'sports' : 'yoga'].sum().sort_values()
labels = list_activites.index
sports_nul = df.movies.isnull().sum()
yoga_nul = df.dining.isnull().sum()
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(list_activites, explode=explode, labels=labels, autopct="%0.0f%%", pctdistance=0.8)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1, use_container_width=False)

st.metric(value=sports_nul, label="Nombre de participant n'ayant pas renseigné ses activités.")

st.divider()