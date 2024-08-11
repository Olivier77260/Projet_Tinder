import streamlit as st
import pandas as pd

def Frequence2(x):
    if x == 1:
        size = "1_Several times a week"
    elif x == 2:
        size = "2_Twice a week"
    elif x == 3:
        size = "3_Once a week"
    elif x == 4:
        size = "4_Twice a month"
    elif x == 5:
        size = "5_Once a month"
    elif x == 6:
        size = "6_Several times a year"
    else:
        size = "7_Almost never"
    return size

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

st.markdown("#### <font color='tomato'><ins>**HABITUDES DE VIE DES PARTICIPANTS**</ins></font>", unsafe_allow_html=True)

sortie_rdv = pd.merge(df.go_out.value_counts(), df.date.value_counts(), right_index=True, left_index=True)
sortie_rdv = sortie_rdv.rename(columns={'count_x': 'Sorties', 'count_y': 'Rdv'})
sortie_rdv['index'] = sortie_rdv.index.map(Frequence2)

ethnic = df['imprace'].value_counts().reset_index(name='race')
ethnic['iid'] = ethnic['imprace']
religious = df['imprelig'].value_counts().reset_index(name='religion')
religious['iid'] = religious['imprelig']
dataset = religious.merge(ethnic, on='iid')
dataset = dataset.sort_values('iid')

tab1, tab2, tab3 = st.tabs(["Sorties et rendez-vous", "Races", "Religions"])

with tab1:
    col2, col3 = st.columns(2, gap='large')
    with col2:
        st.subheader("Fréquence des sorties.")
        st.bar_chart(sortie_rdv, x="index", y='Sorties', x_label='Fréquence des sorties', stack=False, use_container_width=True, color="#dec1ff", horizontal=True)
        st.metric(value=df.go_out.isnull().sum(), label="Nombre de valeurs manquantes.")

    with col3:
        st.subheader("Fréquence des rendez-vous.")
        st.bar_chart(sortie_rdv, x="index", y='Rdv', x_label='Fréquence des rendes-vous', stack=False, use_container_width=True, color= "#00d43c", horizontal=True)
        st.metric(value=df.date.isnull().sum(), label="Nombre de valeurs manquantes.")

    expander = st.expander("A noter")
    expander.write('''
        Une grandes majorité des participant sont des personnes qui sortent trés souvent. 
        En oposition avec les rendez-vous.
    ''')


with tab2:
    st.subheader("Importance de la race dans la relation.")
    st.bar_chart(dataset, x="iid", y="race", stack=False, use_container_width=True)
    st.metric(value=df.imprace.isnull().sum(), label="Nombre de valeurs manquantes.")
with tab3:
    st.subheader("Importance de la religion.")
    st.bar_chart(dataset, x="iid", y="religion", stack=False, use_container_width=True)
    st.metric(value=df.imprelig.isnull().sum(), label="Nombre de valeurs manquantes.")



# st.divider()
# col2, col3 = st.columns(2, gap='large')
# with col2:
#     st.subheader("Fréquence des sorties.")
#     st.bar_chart(sortie_rdv, x="index", y='Sorties', x_label='Fréquence des sorties', stack=False, use_container_width=True, color="#dec1ff", horizontal=True)
#     st.metric(value=df.go_out.isnull().sum(), label="Nombre de valeurs manquantes.")

# with col3:
#     st.subheader("Fréquence des rendez-vous.")
#     st.bar_chart(sortie_rdv, x="index", y='Rdv', x_label='Fréquence des rendes-vous', stack=False, use_container_width=True, color= "#00d43c", horizontal=True)
#     st.metric(value=df.date.isnull().sum(), label="Nombre de valeurs manquantes.")



# st.divider()
# col4, col5 = st.columns(2, gap='large')
# with col4:
#     st.subheader("Importance de la race dans la relation.")
#     st.bar_chart(dataset, x="iid", y="race", stack=False, use_container_width=True)
#     st.metric(value=df.imprace.isnull().sum(), label="Nombre de valeurs manquantes.")
    

# with col5:
#     st.subheader("Importance de la religion.")
#     st.bar_chart(dataset, x="iid", y="religion", stack=False, use_container_width=True)
#     st.metric(value=df.imprelig.isnull().sum(), label="Nombre de valeurs manquantes.")