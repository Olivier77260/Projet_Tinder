import streamlit as st

def main():
    st.set_page_config(page_title="Tinder", page_icon=":couple:", layout="centered", initial_sidebar_state="auto")
    st.write("# Projet Tinder")

    st.logo("icons/tinder-logo.png")
    preambule = st.Page("pages/preambule.py", title="Projet", icon=":material/engineering:", default=True)
    donnees = st.Page("pages/donnees.py", title="Forme des données fournies", icon=":material/database:")
    physique = st.Page("pages/physique.py", title="Physique", icon=":material/directions_run:")

    origines = st.Page("pages/origines.py", title="Origine", icon=":material/diversity_3:")
    age = st.Page("pages/age.py", title="Age", icon=":material/person:")
    social = st.Page("pages/social.py", title="Profil social", icon=":material/language:")

    pages = {
        "🏠 Préambule": [preambule,],
        "📊 Données fournies": [donnees,],
        "🌍 Profil des participants": [physique, origines, age, social],
        "📈 Attentes des participants": [],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__=='__main__':
    main()