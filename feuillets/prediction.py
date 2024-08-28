import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if st.session_state.del_from:
    df = st.session_state.dfTrue
else:
    df = st.session_state.dfFalse

@st.cache_data
def Races(x):
    if x == 1.0:
        size = "Black/African American"
    elif x == 2.0:
        size = "European/Caucasian-American"
    elif x == 3.0:
        size = "Latino/Hispanic American"
    elif x == 4.0:
        size = "Asian/Pacific Islander/Asian-American"
    elif x == 5.0:
        size = "Native American"
    else:
        size = "Other"
    return size

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

df.race = df.race.map(Races)
list_race = df['race'].value_counts().reset_index()
df.career_c = df.career_c.map(ProfilSociaux)
list_carrer = df['career_c'].value_counts().reset_index()

df = df.fillna(df.mean(numeric_only=True))
with st.spinner('Please wait...'):
    features_list = ['age', 'race', 'samerace', 'career_c', 'imprelig', 'imprace', 'gender' ]

    X = df.loc[:,features_list]
    y = df.loc[:,"match"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=0)

    X_test = X_test.reset_index().drop(columns=["index"])
    X_test_age = X_test[X_test["age"]==28]
    X_test_age.index.tolist()

    numeric_features = ['age', 'samerace', 'imprelig', 'imprace', 'gender' ] # Choose which column index we are going to scale
    numeric_transformer = StandardScaler()

    categorical_features = ['race', 'career_c']
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
    mse = mean_squared_error(y_test, y_test_pred)

st.success("Performance du modéle", icon="🚨")
st.write("R2 score on training set : ", regressor.score(X_train, y_train))
st.write("R2 score on test set : ", regressor.score(X_test2, y_test))
st.success("Erreur quadratique moyenne", icon="🚨")
st.write("MSE est de :", mse)

# formulaire pour notre prédiction
with st.form("my_form"):
    st.write("Renseigner les élements ci-dessous")
    age = st.number_input("Votre age", min_value=18, max_value=55, format="%0.0f", step=1, placeholder="Type age...")
    race = st.selectbox(
        "Sélectionner votre race",
        (list_race.race),
        index=None,
        placeholder="Select race...",
        )
    career = st.selectbox(
        "Sélectionner votre profession",
        (list_carrer.career_c),
        index=None,
        placeholder="Select career...",
        )
    col1, col2, col3, col4 = st.columns(4)
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
        imprelig = st.slider("Es-ce important pour vous d'être de la même religion ?", 1, 10, 1)
    with col4:
        imprace = st.slider("Es-ce important pour vous d'être de la même race ?", 1, 10, 1)
    submitted = st.form_submit_button("Submit")
    if submitted:
        data_dict = {"age":[age], "race":[race], "samerace":[samerace], "career_c":[career], "imprelig":[imprelig], "imprace":[imprace], "gender":[genre]}
        data_to_pred = pd.DataFrame(data_dict)
        st.write(data_to_pred)
        data_to_pred_encoded = feature_encoder.transform(data_to_pred)
        pred = regressor.predict(data_to_pred_encoded)
        if pred[0] == 0:
            st.write("Les posibilités d'obtenir un rendez-vous sont faible")
        else:
            st.write("Les posibilités d'obtenir un rendez-vous sont important")