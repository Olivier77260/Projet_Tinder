import streamlit as st

st.markdown("#### <font color='tomato'><ins>**INTRODUCTION**</ins></font>", unsafe_allow_html=True)
if 'del_from' not in st.session_state:
    st.session_state.del_from = False
st.image("icons/tinder-logo.png")
st.subheader("Tinder est une application de rencontres en ligne et de réseautage géosocial. Dans Tinder, les utilisateurs « glissent vers la droite » pour aimer ou « glissent vers la gauche » pour ne pas aimer les profils des autres utilisateurs, qui incluent leurs photos, une courte biographie et une liste de leurs intérêts.")
st.subheader("En 2021, Tinder a enregistré plus de 65 milliards de matchs dans le monde.")