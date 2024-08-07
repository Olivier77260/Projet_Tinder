import streamlit as st
import pandas as pd

@st.cache_data
def load_data_True():
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    df = df.dropna(subset=['from', 'race'])
    df = df.drop(df[df.age==55].index)
    return df
def load_data_False():
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    return df

def main():
    st.set_page_config(page_title="Tinder", page_icon="👩‍❤️‍👨", layout="wide", initial_sidebar_state="auto")
    st.logo("icons/tinder-logo.png")

    if 'del_from' not in st.session_state:
        st.session_state.del_from = False

    st.session_state.dfTrue = load_data_True()
    st.session_state.dfFalse = load_data_False() 

    preambule = st.Page("feuillets/preambule.py", title="Projet", icon=":material/engineering:", default=True)

    donnees = st.Page("feuillets/donnees.py", title="Données", icon=":material/database:")

    analyse = st.Page("feuillets/analyse.py", title="Analyses", icon=":material/diversity_3:")

    physique = st.Page("feuillets/physique.py", title="Physique", icon="♂️")
    social = st.Page("feuillets/social.py", title="Social", icon=":material/language:")

    habitudes = st.Page("feuillets/habitudes.py", title="Habitudes", icon=":material/person:")

    attentes = st.Page("feuillets/attentes.py", title="Attentes", icon=":material/diversity_3:")

    speed_dating = st.Page("feuillets/speed_dating.py", title="Speed Dating", icon=":material/diversity_3:")

    premier_rdv = st.Page("feuillets/first_rdv.py", title="Premier rendez-vous", icon=":material/diversity_3:")

    pages = {
        "🏠 Préambule": [preambule,],
        "📊 Données fournies": [donnees,],
        "🛠️ Analyse des données": [analyse,],
        "🌍 Profil des participants": [physique, social,],
        "🌈 Habitudes de vie des participants": [habitudes,],
        "⏱️ Attentes des participants": [attentes, speed_dating, premier_rdv,],
    }
    
    pg = st.navigation(pages)
    pg.run()

if __name__=='__main__':
    main()