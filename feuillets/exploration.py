import streamlit as st
import matplotlib.pyplot as plt

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**ANALYSE DES DONNEES**</ins></font>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["##### :blue[***1. Profil du fichier csv***]", "##### :blue[***2. Nom des colonnes***]", "##### :blue[***3. Données manquantes***]", "##### :blue[***4. Ages***]"])

with tab1:
    st.divider()
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

    st.subheader("Beaucoup de données catégorielles ont été converties numériquement.")

with tab2:
    st.divider()
    nb_participant = str(df['iid'].max())
    st.subheader("Le nombre de participants à cette enquête est de " + nb_participant + " personnes, déterminé par la colonne iid suivant la note explicative, ce qui n'est pas très élevé aux vues des 65 milliards de match dans le monde.")

    st.subheader("Le nom des colonnes n'étant pas très explicite, la documentation fournie nous sera d'une grande aide.")

    name_colonnes = df.columns
    st.dataframe(name_colonnes, width=200)

with tab3:
    st.divider()
    in_null = df.isnull().sum()
    non_conforme = str(df['attr1_1'][df.wave == 9].max())
    st.dataframe(in_null, width=160)
    st.subheader("Beaucoup de données sont manquantes et demanderont une attention particulière.")
    st.subheader("""Les évaluations demandées ne sont pas notées dans la même base en fonction de la wave. Les waves de 6 à 9 sont évaluées en fonction d'une échelle allant de 1 à 10."""
                 """ Alors que les waves de 1 à 5 et de 10 à 21 ont 100 points à répartir entre les différents attributs.""")
    st.subheader('Donc il faudra bien les séparer lors des différents calculs.')
    st.subheader('Certaines wave de 6 à 9 ne respectent pas la notation de 1 à 10 et seront simplement exclut des calcul car non conforme à la base de notation.')
    st.metric(value=non_conforme, label="Exemple de valeur non conforme")


with tab4:
    st.divider()
    st.subheader("Profil des ages masculins et féminins de nos participants")
    age_gender = df.groupby('age')['gender'].value_counts().reset_index(name='count')

    age_gender_female = age_gender.loc[age_gender['gender'] == 0]
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel('age')
    ax1.set_title('Outlier des ages féminins')
    ax1.boxplot(age_gender_female['age'], 0, 'gD', patch_artist=True, boxprops={'facecolor': 'bisque'}, widths=0.5)

    age_gender_male = age_gender.loc[age_gender['gender'] == 1]
    fig2, ax2 = plt.subplots()
    ax2.set_ylabel('age')
    ax2.set_title('Outlier des ages masculins')
    ax2.boxplot(age_gender_male['age'], 0, 'gD', patch_artist=True, boxprops={'facecolor': 'bisque'}, widths=0.5)

    col5, col6 = st.columns(2, gap="medium")
    with col5:
        st.pyplot(fig1)
    with col6:
        st.pyplot(fig2)

    st.caption("""Nous avons une personnes de sexe féminin agée de 55 ans qui """
                """a obtenu plusieurs rendez-vous avec des jeunes, je pense qu'il s'agit certainement une erreur dans la saissie réelle de son age.""")
