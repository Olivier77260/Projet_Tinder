import streamlit as st

# listing des ages
@st.cache_data
def list_age(df):
    list_age = df['age'].value_counts()
    list_age = list_age.index.sort_values(ascending=True)
    return list_age
    
@st.cache_data
def nb_participant(df):
    if st.session_state.del_from:
        a = df['iid'].max()
        b = df.iid.value_counts().value_counts().sum()
        nb_participant = df['iid'].max() - (a-b)
        return nb_participant
    else:
        nb_participant = df['iid'].max()
        return nb_participant

@st.cache_data  
def delta(df):
    nb = nb_participant(df)
    delta = df['iid'].max() - nb
    return delta
