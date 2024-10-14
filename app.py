import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from streamlit_extras.metric_cards import style_metric_cards
import seaborn as sns

st.set_page_config(page_title="ANALYSE", layout="wide")

st.markdown(
    "<h1 style='text-align: center; font-size: 40px;'>MACHINE LEARNING 💹</h1>",
    unsafe_allow_html=True
)
st.image("image/logo2.webp")
st.sidebar.image("image/logos.webp", caption="MULTI-VARIATION D'ANALYSE")

# Lecture du fichier Excel
df = pd.read_excel("db_regression.xlsx")

# Sélection des variables pour la régression
X = df[['NIF', 'Nombre activite']]
Y = df['CA']

# Création du modèle de régression linéaire
model = LinearRegression()
model.fit(X, Y)

# Prédictions du modèle
prediction = model.predict(X)

# Interception et coefficients de la régression
interception = model.intercept_
coefficient = model.coef_

# Calcul de R² et de R² ajusté
r2 = r2_score(Y, prediction)
n = len(Y)
k = X.shape[1]
ajuste_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)

# Calcul de SSE et SSR
sse = np.sum((Y - prediction) ** 2)
ssr = np.sum((prediction - np.mean(Y)) ** 2)

# Visualisation des résultats de la régression
with st.expander("REGRESSION DE COEFFICIENT"):
    col_1, col_2, col_3 = st.columns(3)
    col_1.metric("Y Intercepte", value=f'{interception:.4f}', delta="Bo")
    col_2.metric("B1 COEFFICIENT", value=f'{coefficient[0]:.4f}', delta="B1 X1 ou NIF")
    col_3.metric("Somme des erreurs SSE", value=f'{sse:.4f}', delta="(Y-Y^)²")
    style_metric_cards(background_color="#FFFFFF", border_left_color="#0ac4ea", border_color="#40f9ee", box_shadow="#6efcf4")

with st.expander("MESURE DE VARIATION"):
    col_1, col_2, col_3 = st.columns(3)
    col_1.metric("Coefficient de détermination (R²)", value=f'{r2:.4f}', delta="R²")
    col_2.metric("Coefficient ajusté (R² ajusté)", value=f'{ajuste_r2:.4f}', delta="R² ajusté")
    col_3.metric("SSE", value=f'{sse:.4f}', delta="Somme des erreurs")
    style_metric_cards(background_color="#FFFFFF", border_left_color="#0ac4ea", border_color="#40f9ee", box_shadow="#6efcf4")

# Affichage des données sous forme de tableau
result_df = pd.DataFrame({
    'Nom': df['Nom'],
    'Activite': df['Activite'],
    'CA': df['CA'],
    'NIF': df['NIF'],
    'Nombre activite': df['Nombre activite'],
    'Prédiction (Y^)': prediction
})

result_df['SSE'] = sse
result_df['SSR'] = ssr

# Affichage du tableau et option de téléchargement
with st.expander("DETECTION DE TABLE"):
    st.dataframe(result_df, use_container_width=True)
    
    df_tele = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Télécharger la table de prédiction",
        data=df_tele,
        file_name="table_de_prediction.csv",
        mime='text/csv'
    )

# Visualisation de l'écart ou du résiduel et de la ligne d'ajustement
with st.expander("ÉCART ou RÉSIDUEL ET LIGNE D'AJUSTEMENT"):
    residuel = Y - prediction
    residuel_df = pd.DataFrame({
        'Y actuel (CA)': Y,
        'Valeur prédite': prediction,
        'ÉCART ou RÉSIDUEL': residuel
    })

    st.dataframe(residuel_df, use_container_width=True)
    
    col_1, col_2 = st.columns(2)
    with col_1:
        # Création du premier graphique
        fig1, ax1 = plt.subplots()
        ax1.scatter(Y, prediction, label="Points prédits")
        ax1.plot([min(Y), max(Y)], [min(Y), max(Y)], '--k', label="Meilleure ligne d'ajustement")
        ax1.set_xlabel("Y actuel (CA)")
        ax1.set_ylabel("Y prédit (CA)")
        ax1.legend()
        ax1.grid(True)
        
        # Affichage du premier graphique dans Streamlit
        st.pyplot(fig1)
        
    with col_2:
        # Création du deuxième graphique avec Seaborn
        fig2, ax2 = plt.subplots()
        sns.kdeplot(residuel, ax=ax2, color="green", fill=True)
        ax2.set_title("Distribution des résidus")
        ax2.set_xlabel("Résidu")
        ax2.grid(True)
        
        # Affichage du deuxième graphique dans Streamlit
        st.pyplot(fig2)
#prédire une nouvelle valeur entrante
with st.sidebar:
    with st.form("imput_from",clear_on_submit=True):
        x1 = st.number_input("Entez une novelle declaration CA", max_value=1000000000000)
        x2 = st.number_input("Entez une novelle declaration nombre d'activite", max_value=1000000000000)
        submit = st.form_submit_button(label="cliquez pour vérifier la prédiction")
        
if submit:
    #faire des prédictions
    new_data = np.array([[x1,x2]])
    nwe_prediction = model.predict(new_data)
    with st.expander("OUVRIR"):
        st.write(f"<span style='font-size:34; color:green;'> Prédit output: {nwe_prediction}</span>", unsafe_allow_html=True)