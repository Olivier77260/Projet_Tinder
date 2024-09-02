import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, f1_score
from sklearn.linear_model import LogisticRegression

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

@st.cache_data
def ProfilSociaux(x):
    if x == 1.0:
        size = "Lawyer"
    elif x == 2.0:
        size = "Academic/Research"
    elif x == 3.0:
        size = "Psychologist"
    elif x == 4.0:
        size = "Doctor/Medicine"
    elif x == 5.0:
        size = "Engineer"
    elif x == 6.0:
        size = "Creative Arts/Entertainment"
    elif x == 7.0:
        size = "Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/Admin"
    elif x == 8.0:
        size = "Real Estate"
    elif x == 9.0:
        size = "International/Humanitarian Affairs"
    elif x == 10.0:
        size = "Undecided"
    elif x == 11.0:
        size = "Social Work"
    elif x == 12.0:
        size = "Speech Pathology"
    elif x == 13.0:
        size = "Politics"
    elif x == 14.0:
        size = "Pro sports/Athletics"
    elif x == 15.0:
        size = "Other"
    elif x == 16.0:
        size = "Journalism"
    elif x == 17.0:
        size = "Architecture"
    else:
        size = "Other"
    return size

@st.cache_resource
def modele(df):
    features_list = ['age', 'fun', 'samerace', 'career_c', 'attr', 'gender' ]

    X = df.loc[:,features_list]
    y = df.loc[:,"dec"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    X_test = X_test.reset_index().drop(columns=["index"])
    X_test_age = X_test[X_test["attr"]==8]
    X_test_age.index.tolist()

    numeric_features = ['age', 'fun', 'samerace', 'attr', 'gender' ] # Choose which column index we are going to scale
    numeric_transformer = StandardScaler()

    categorical_features = ['career_c']
    categorical_transformer = OneHotEncoder(handle_unknown="ignore", drop='first')

    # Apply ColumnTransformer to create a pipeline that will apply the above preprocessing
    feature_encoder = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features),    
            ('num', numeric_transformer, numeric_features)
            ]
        )

    X_train = feature_encoder.fit_transform(X_train)
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)
    y_train_pred = regressor.predict(X_train)
    X_test2 = feature_encoder.transform(X_test)
    y_test_pred = regressor.predict(X_test2)

    return X_train, y_train, X_test2, y_test, regressor, y_test_pred, feature_encoder

with st.spinner('Veuillez patienter... Chargement du modéle...'):
    df.career_c = df.career_c.map(ProfilSociaux)
    list_carrer = df['career_c'].value_counts().reset_index()
    derived_df = df[['age', 'fun', 'samerace', 'career_c', 'attr', 'gender', 'dec' ]]
    df = derived_df.dropna()
    mod_reg_logistique = modele(df)

# formulaire pour notre prédiction
with st.form("my_form"):
    st.write("Renseigner les élements ci-dessous")
    age = st.number_input("Votre age", min_value=18, max_value=55, format="%0.0f", step=1, placeholder="Type age...")
    career = st.selectbox(
        "Sélectionner votre profession",
        (list_carrer.career_c),
        index=None,
        placeholder="Select career...",
        )
    col1, col2, col3 = st.columns(3)
    with col1:
        genre = st.radio(
                "Quel est votre genre ?",
                ["0", "1"],
                captions=[
                    "Femme",
                    "Homme",
                ],
            )
    with col2:
        samerace = st.radio(
                "Es-ce important pour vous d'être de la même race ?",
                ["0", "1"],
                captions=[
                    "Non",
                    "Oui",
                ],
            )
    with col3:
        attractivite = st.slider("Es-ce important pour vous l'attractivité envers cette personne ?", 1, 10, 1)
        fun = st.slider("Es-ce important pour vous que cette personne soit fun ?", 1, 10, 1)
    submitted = st.form_submit_button("Submit")
    if submitted:
        data_dict = {"age":[age], "fun":[fun], "samerace":[samerace], "career_c":[career], "attr":[attractivite], "gender":[genre]}
        data_to_pred = pd.DataFrame(data_dict)
        st.write(data_to_pred)
        data_to_pred_encoded = mod_reg_logistique[6].transform(data_to_pred)
        pred = mod_reg_logistique[4].predict(data_to_pred_encoded)
        if pred[0] == 0:
            st.write("Les posibilités d'obtenir un rendez-vous sont faibles :umbrella_with_rain_drops:")
        else:
            st.success("Les posibilités d'obtenir un rendez-vous sont importantes", icon="🔥")

mse = mean_squared_error(mod_reg_logistique[3], mod_reg_logistique[5])
R2_train = mod_reg_logistique[4].score(mod_reg_logistique[0], mod_reg_logistique[1])
R2_test = mod_reg_logistique[4].score(mod_reg_logistique[2], mod_reg_logistique[3])

expander = st.expander("considérations :", icon="🚨")
expander.write("R2 score on training set : " + str(R2_train))
expander.write("R2 score on test set : " + str(R2_test))
expander.write("MSE est de : " + str(mse))