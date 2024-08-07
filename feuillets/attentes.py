import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("#### <font color='tomato'><ins>**ATTENTES DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

objectifs = df.groupby('goal')['gender'].value_counts().reset_index()
objectifs['gender'] = objectifs['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
objectifs = objectifs[objectifs.gender == 'Male'].set_index('goal')
objectifs = objectifs.drop('gender', axis=1)
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
objectifs.index = objectifs.index.map(Objects)
objectifs = objectifs.squeeze()
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(objectifs, explode=explode, labels=objectifs.index, autopct='%0.0f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

list_search = df.loc[:, 'attr1_1' : 'shar1_1'].sum().sort_values()
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
list_search.index = list_search.index.map(quality)

colors = sns.color_palette("bright")
explode = (0, 0, 0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig2, ax2 = plt.subplots()
ax2.pie(list_search, explode=explode, labels=list_search.index, colors=colors, autopct='%0.0f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.divider()
col1, col2 = st.columns(2, gap='medium')
with col1:
    st.subheader("Attentes des participants hommes.")
    st.pyplot(fig1)
    st.metric(value=df['goal'].isnull().sum(), label="Nombre de valeurs manquantes.")
    st.checkbox("Suppression des valeurs manquantes", key="del_from")

with col2:
    st.subheader("Qualités recherchées dans le sexe opposé.")
    st.pyplot(fig2)
    st.metric(value=df['intel1_1'].isnull().sum(), label="Nombre de valeurs manquantes.")

st.divider()
st.subheader("""Les femmes restent plus septiques par rapport aux hommes quant à trouver le bonheur avec telle application""")
happy_gender = df.groupby('exphappy')['gender'].value_counts().reset_index()
happy_gender['gender'] = happy_gender['gender'].apply(lambda x: 'Female' if x == 0 else 'Male')
# sns.catplot(x="exphappy", y="count", kind="bar", hue="gender", data=happy_gender, aspect=2.5)
colors = "gender"
st.bar_chart(happy_gender, x="exphappy", y="count", color=colors, stack=False, use_container_width=True)