import streamlit as st

def main():    
    st.set_page_config(page_title="Tinder", page_icon="👩‍❤️‍👨", layout="wide", initial_sidebar_state="auto")
    st.logo("icons/tinder-logo.png")

    preambule = st.Page("feuillets/preambule.py", title="Projet", icon=":material/engineering:", default=True)

    donnees = st.Page("feuillets/donnees.py", title="Données", icon=":material/database:")

    analyse = st.Page("feuillets/analyse.py", title="Analyses", icon=":material/diversity_3:")

    physique = st.Page("feuillets/physique.py", title="Physique", icon="♂️")
    social = st.Page("feuillets/social.py", title="Social", icon=":material/language:")

    habitudes = st.Page("feuillets/habitudes.py", title="Habitudes", icon=":material/person:")

    attentes = st.Page("feuillets/attentes.py", title="Attentes", icon=":material/diversity_3:")

    premier_rdv = st.Page("feuillets/first_rdv.py", title="Premier rendez-vous", icon=":material/diversity_3:")

    pages = {
        "🏠 Préambule": [preambule,],
        "📊 Données fournies": [donnees,],
        "🛠️ Analyse des données": [analyse,],
        "🌍 Profil des participants": [physique, social,],
        "🌈 Habitudes de vie des participants": [habitudes,],
        "⏱️ Attentes des participants": [attentes, premier_rdv,],
    }
    
    pg = st.navigation(pages)
    pg.run()

if __name__=='__main__':
    main()