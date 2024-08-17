import streamlit as st
import matplotlib.pyplot as plt
from fonctions import nb_participant

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

@st.cache_data
def age_gender(genre, df):
    age_gender = df.groupby('age')['gender'].value_counts().reset_index(name='count')
    age_gender = age_gender.loc[age_gender['gender'] == genre]
    return age_gender

st.markdown("## <font color='tomato'><ins>**ANALYSE DES DONNEES**</ins></font>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["##### :blue[***1. Profil du fichier csv***]", "##### :blue[***2. Nom des colonnes***]", "##### :blue[***3. Problématique des données***]", "##### :blue[***4. Ages***]"])

# profil du fichier csv
with tab1:
    col1, col2 = st.columns(2, gap="medium")
    with col1:        
        st.metric(label="Nombre de lignes", value=df.shape[0])
    with col2:
        st.metric(label="Nombre de colonnes", value=df.shape[1])

    st.write("Affichage des 5 premiéres lignes")

    st.dataframe(df.head(), hide_index=True)
    st.divider()
    df_num = df.select_dtypes(exclude="object")
    somme_num_value = df_num.columns.value_counts()
    df_categories = df.select_dtypes(include="object")
    somme_cat_value = df_categories.columns.value_counts()

    col3, col4 = st.columns(2, gap="medium")
    with col3:
        st.metric(label="Nombre de colonnes numérique", value=somme_num_value.sum())
    with col4:
        st.metric(label="Nombre de colonnes catégorielles", value=somme_cat_value.sum())

    st.subheader("Beaucoup de données catégorielles ont été converties numériquement et ne pouront être utilisées pour des calculs.")

# noms des colonnes
with tab2:
    st.subheader("Le nombre de participants à cette enquête est de " + str(nb_participant(df)) + " personnes, déterminé par la colonne iid suivant la note explicative, ce qui n'est pas très élevé aux vues des 65 milliards de match dans le monde.")

    st.subheader("Le nom des colonnes n'étant pas très explicite, la documentation fournie nous sera d'une grande aide.")
    st.write('Nom des colonnes')
    name_colonnes = df.columns
    st.dataframe(name_colonnes, width=200)

# données manquantes
with tab3:
    in_null = df.isnull().sum().reset_index(name="nul")
    st.write('Données manquantes')
    st.dataframe(in_null, width=200)
    st.subheader("""On peut voir que le nombre 79 revient souvent dans les différentes colonnes et donc elles seront supprimées car elles contiennent des données essentielles à l'étude."""
                 """ Beaucoup de données restent manquantes et demanderont une attention particulière.""")
    st.subheader("""Les évaluations demandées ne sont pas notées dans la même base en fonction de la wave. Les waves de 6 à 9 sont évaluées en fonction d'une échelle allant de 1 à 10."""
                 """ Alors que les waves de 1 à 5 et de 10 à 21 ont 100 points à répartir entre les différents attributs.""")
    st.subheader('Donc il faudra bien les séparer lors des différents calculs.')
    st.subheader('Certaines wave de 6 à 9 ne respectent pas la notation de 1 à 10 et seront simplement exclut des calculs car non conforme à la base de notation.')
    st.write("Exemple de valeurs non conforme de la wave 6")
    exemple = df.groupby(['gender', (df.wave == 6)]).aggregate({'pf_o_att':'mean','pf_o_sin':'mean','pf_o_int':'mean','pf_o_fun':'mean','pf_o_amb':'mean','pf_o_sha':'mean'}).reset_index()
    st.dataframe(exemple)

# ages
with tab4:
    st.subheader("Profil des ages masculins et féminins de nos participants")
    # age_gender = df.groupby('age')['gender'].value_counts().reset_index(name='count')
    # age_gender_female = age_gender.loc[age_gender['gender'] == 0]
    age_gender_female = age_gender(0, df)
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel('age')
    ax1.set_title('Outlier des ages féminins')
    ax1.boxplot(age_gender_female['age'], 0, 'gD', patch_artist=True, boxprops={'facecolor': 'bisque'}, widths=0.5)

    # age_gender_male = age_gender.loc[age_gender['gender'] == 1]
    age_gender_male = age_gender(1, df)
    fig2, ax2 = plt.subplots()
    ax2.set_ylabel('age')
    ax2.set_title('Outlier des ages masculins')
    ax2.boxplot(age_gender_male['age'], 0, 'gD', patch_artist=True, boxprops={'facecolor': 'bisque'}, widths=0.5)

    col5, col6 = st.columns(2, gap="medium")
    with col5:
        st.pyplot(fig1)
    with col6:
        st.pyplot(fig2)

    st.subheader("""Nous avons une personnes de sexe féminin agée de 55 ans qui """
                """a obtenu plusieurs rendez-vous avec des jeunes, je pense qu'il s'agit certainement d'une erreur de saisie de son age.""")
    st.subheader("J'ai décidé de mettre en place un bouton de selèction qui permet de supprimer de l'étude ces valeurs dites aberrantes, ce qui permettra de voir l'impact réel sur notre étude")