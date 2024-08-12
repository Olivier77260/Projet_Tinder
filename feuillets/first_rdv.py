import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("## <font color='tomato'><ins>**PREMIERS RENDEZ-VOUS**</ins></font>", unsafe_allow_html=True)

st.balloons()