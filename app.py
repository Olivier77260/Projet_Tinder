import streamlit as st
import pandas as pd

@st.cache_data
def load_data_True():
    df = pd.read_csv("Speed_Dating_Data.csv", encoding="cp1252")
    # df = df.dropna(subset=['from', 'race'])
    # indexNames = df[df["age"] <= 40].index
    # df.drop(indexNames, inplace=True)
    # df = df.drop(df[df.age<=55].index)
    # indexNames = df[(df["age"] >= 37) & (df["age"] <= 18)].index
    # # Delete these row indexes from dataFrame
    # df = df.drop(indexNames)

    return df[(df["age"] < 37) & (df["age"] > 18)]

@st.cache_data
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

    with st.sidebar:
        manque = st.radio(
        "Suppression des valeurs abérantes",
        ["Non", "Oui"],
        horizontal=True,
        )

    if manque == "Non":
        st.session_state.del_from = False
    else:
        st.session_state.del_from = True
    
    preambule = st.Page("feuillets/preambule.py", title="1 - Préambule", icon="📇", default=True)
    projet = st.Page("feuillets/projet.py", title="2 - Projet", icon="🚧", default=False)
    objectif = st.Page("feuillets/objectif.py", title="3 - Objectif", icon="🎯", default=False)
    portee = st.Page("feuillets/portee.py", title="4 - Portée du projet", icon="🖼️", default=False)

    donnees = st.Page("feuillets/donnees.py", title="- Données", icon=":material/database:")

    exploration = st.Page("feuillets/exploration.py", title="- Exploration", icon="📈")

    physique = st.Page("feuillets/physique.py", title="1 - Physique", icon="♂️")
    social = st.Page("feuillets/social.py", title="2 - Social", icon=":material/language:")

    habitudes = st.Page("feuillets/habitudes.py", title="- Habitudes", icon="🍀")

    attentes = st.Page("feuillets/attentes.py", title="1 - Attentes", icon="⏱️")
    speed_dating = st.Page("feuillets/speed_dating.py", title="2 - Speed Dating", icon="🎈")
    premier_rdv = st.Page("feuillets/first_rdv.py", title="3 - Premier rendez-vous", icon="🎉")
    
    pages = {
        "🏠 Préambule": [preambule, projet, objectif, portee,],
        "📊 Données fournies": [donnees,],
        "🛠️ Analyse des données": [exploration,],
        "🌍 Profil des participants": [physique, social,],
        "🌈 Habitudes de vie des participants": [habitudes,],
        "👩‍🚀 Expérimentation": [attentes, speed_dating, premier_rdv,],
    }
    
    pg = st.navigation(pages)
    pg.run()

if __name__=='__main__':
    main()
