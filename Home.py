import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *
import time

st.set_page_config(page_title="DGI_machine_learning", page_icon="📊", layout="wide")
st.markdown(
    "<h1 style='text-align: center; font-size: 40px;'>ANALYSE PREDICTIVE DES EVALUATIONS FISCALES 💹</h1>",
    unsafe_allow_html=True
)

st.markdown("##")

# Récupération des données et création du DataFrame
result = voire_touts_data()
df = pd.DataFrame(result, columns=[
    "id", "RE001.1", "RE001.2", "RE001.2.A", "RE001.2.B", "RE001.2.C", "RE001.2.D", "RE001.2.E", 
    "RE002.1", "RE002.2", "RE002.3", "RE002.4", "RE002.5", "RE003.1", "RE003.2", "RE003.3", 
    "RE003.4", "RE003.5", "RE003.6", "RE004.1", "RE004.2", "RE004.3", "RE004.4", "RE004.5", 
    "RE004.6", "RE004.7"
])

# Remplacer les valeurs NaN par 'Inconnu'
df.fillna('Inconnu', inplace=True)

st.sidebar.image("donnees/logo.png", caption="Analyse en ligne")
st.sidebar.header("Filtre des données")

# Filtrage avec multiselect pour chaque colonne, en excluant les NaN des valeurs par défaut
RE001_1 = st.sidebar.multiselect(
    "RE001.1. Ecart entre Chiffres d'affaires à l'IR et à la TVA",
    options=df["RE001.1"].unique(),
    default=df["RE001.1"].unique()
)

RE001_2 = st.sidebar.multiselect(
    "RE001.2. Ecart entre chiffre d'affaire déclaré et recoupements.",
    options=df["RE001.2"].unique(),
    default=df["RE001.2"].unique()
)

RE001_2_A = st.sidebar.multiselect(
    "-RE001.2.A Ecart entre chiffre d'affaire déclaré sur exportation et recoupements sur exportation",
    options=df["RE001.2.A"].unique(),
    default=df["RE001.2.A"].unique()
)

RE001_2_B = st.sidebar.multiselect(
    "-RE001.2.B Ecart entre chiffre d'affaire déclaré sur opération locale et chiffre d'affaire recoupé sur DCOM.",
    options=df["RE001.2.B"].unique(),
    default=df["RE001.2.B"].unique()
)

RE001_2_C = st.sidebar.multiselect(
    "RE001.2.C Ecart entre chiffre d'affaire déclaré sur opération locale et recoupements sur annexe TVA.",
    options=df["RE001.2.C"].unique(),
    default=df["RE001.2.C"].unique()
)

RE001_2_D = st.sidebar.multiselect(
    "RE001.2.D Ecart entre chiffre d'affaire déclaré et recoupements sur achats majoré.",
    options=df["RE001.2.D"].unique(),
    default=df["RE001.2.D"].unique()
)

RE001_2_E = st.sidebar.multiselect(
    "RE001.2.E Ecart entre chiffre d'affaire déclaré et facturation électronique.",
    options=df["RE001.2.E"].unique(),
    default=df["RE001.2.E"].unique()
)

RE002_1 = st.sidebar.multiselect(
    "RE002.1. Ecart entre charges de personnel déclarées et les déclarations sociales CNAPS/OSTIE.",
    options=df["RE002.1"].unique(),
    default=df["RE002.1"].unique()
)

RE002_2 = st.sidebar.multiselect(
    "RE002.2. Ecart entre charges de personnel déclarées à l'IR et à l'IRSA.",
    options=df["RE002.2"].unique(),
    default=df["RE002.2"].unique()
)

RE002_3 = st.sidebar.multiselect(
    "RE002.3. Ecart entre charges déclarées sur contribuables immatriculés et recoupements.",
    options=df["RE002.3"].unique(),
    default=df["RE002.3"].unique()
)

RE002_4 = st.sidebar.multiselect(
    "RE002.4. Ecart entre charges déclarées sur contribuables non immatriculés locaux et les déclarations ISI.",
    options=df["RE002.4"].unique(),
    default=df["RE002.4"].unique()
)

RE002_5 = st.sidebar.multiselect(
    "RE002.5. Ecart entre charges déclarées sur contribuables non immatriculés étrangers et les déclarations IRI et TVAI.",
    options=df["RE002.5"].unique(),
    default=df["RE002.5"].unique()
)

RE003_1 = st.sidebar.multiselect(
    "RE003.1. Ecart entre TVA déductible sur opérations locales et celles collectées par les tiers.",
    options=df["RE003.1"].unique(),
    default=df["RE003.1"].unique()
)

RE003_2 = st.sidebar.multiselect(
    "RE003.2. Ecart entre TVA déductible sur importations de biens et les TVA recoupées sur DAU.",
    options=df["RE003.2"].unique(),
    default=df["RE003.2"].unique()
)

RE003_3 = st.sidebar.multiselect(
    "RE003.3. Ecart entre TVA déductible sur importations de services et les TVAI déclarées.",
    options=df["RE003.3"].unique(),
    default=df["RE003.3"].unique()
)

RE003_4 = st.sidebar.multiselect(
    "RE003.4. Correspondance entre TVAI et IRI déclarées.",
    options=df["RE003.4"].unique(),
    default=df["RE003.4"].unique()
)

RE003_5 = st.sidebar.multiselect(
    "RE003.5. Ecart entre TVA collectées sur opérations locales et celles déduites par les tiers.",
    options=df["RE003.5"].unique(),
    default=df["RE003.5"].unique()
)

RE003_6 = st.sidebar.multiselect(
    "RE003.6. Permanence du crédit de TVA pour les contribuables autres que exportateurs, ZEF, investisseurs.",
    options=df["RE003.6"].unique(),
    default=df["RE003.6"].unique()
)

RE004_1 = st.sidebar.multiselect(
    "RE004.1. Poids de l'impôt comparé à celui du secteur du contribuable.",
    options=df["RE004.1"].unique(),
    default=df["RE004.1"].unique()
)

RE004_2 = st.sidebar.multiselect(
    "RE004.2. Importance des opérations avec les non immatriculés.",
    options=df["RE004.2"].unique(),
    default=df["RE004.2"].unique()
)

RE004_3 = st.sidebar.multiselect(
    "RE004.3. Ecart entre CA sur Etats financiers et CA sur DCOM.",
    options=df["RE004.3"].unique(),
    default=df["RE004.3"].unique()
)

RE004_4 = st.sidebar.multiselect(
    "RE004.4. Ecart entre les charges sur Etats financiers et les achats et sommes versées sur DCOM.",
    options=df["RE004.4"].unique(),
    default=df["RE004.4"].unique()
)

RE004_5 = st.sidebar.multiselect(
    "RE004.5. Ecart entre achats déclarés et achats recoupés auprès des tiers.",
    options=df["RE004.5"].unique(),
    default=df["RE004.5"].unique()
)

RE004_6 = st.sidebar.multiselect(
    "RE004.6. Ecart entre Ratio nombre de salariés sur CA et celui du secteur du contribuable.",
    options=df["RE004.6"].unique(),
    default=df["RE004.6"].unique()
)

RE004_7 = st.sidebar.multiselect(
    "RE004.7. Permanence du déficit à l'IR.",
    options=df["RE004.7"].unique(),
    default=df["RE004.7"].unique()
)

# Filtrer le DataFrame selon les sélections
df_selection = df.query(
    "`RE001.1` == @RE001_1 & `RE001.2` == @RE001_2 & `RE001.2.A` == @RE001_2_A & `RE001.2.B` == @RE001_2_B & "
    "`RE001.2.C` == @RE001_2_C & `RE001.2.D` == @RE001_2_D & `RE001.2.E` == @RE001_2_E & `RE002.1` == @RE002_1 & "
    "`RE002.2` == @RE002_2 & `RE002.3` == @RE002_3 & `RE002.4` == @RE002_4 & `RE002.5` == @RE002_5 & "
    "`RE003.1` == @RE003_1 & `RE003.2` == @RE003_2 & `RE003.3` == @RE003_3 & `RE003.4` == @RE003_4 & "
    "`RE003.5` == @RE003_5 & `RE003.6` == @RE003_6 & `RE004.1` == @RE004_1 & `RE004.2` == @RE004_2 & "
    "`RE004.3` == @RE004_3 & `RE004.4` == @RE004_4 & `RE004.5` == @RE004_5 & `RE004.6` == @RE004_6 & "
    "`RE004.7` == @RE004_7"
)

# st.dataframe(df_selection)

def Home():
    with st.expander("tabulaire"):
        showData = st.multiselect('Filtre: ',df_selection.columns,default=[])
        st.write(df_selection[showData])
        
    total_Ecart_entre_Chiffres_d_affaires_à_l_IR_et_à_la_TVA = df_selection["RE001.1"].astype(float).sum()
    RE001_1_mode = df_selection["RE001.1"].astype(float).mode()[0]
    RE001_1_mean = df_selection["RE001.1"].astype(float).mean()
    RE001_1_median = df_selection["RE001.1"].astype(float).median()
    RE004_6 = df_selection["RE004.6"].astype(float).sum()
    
    total_1,total_2,total_3,total_4,total_5 = st.columns(5,gap='large')
    with total_1:
        st.info('Total ecart entre Chiffres d_affaires à l_IR et à la TVA', icon="📌")
        st.metric(label="Somme de TVA", value=f"{total_Ecart_entre_Chiffres_d_affaires_à_l_IR_et_à_la_TVA:,.0f}")
    
    with total_2:
        st.info('le plus fréquent', icon="📌")
        st.metric(label="Mode de TVA", value=f"{RE001_1_mode:,.0f}")
        
    with total_3:
        st.info('moyenne', icon="📌")
        st.metric(label="Moyenne de TVA", value=f"{RE001_1_mean:,.0f}")
        
    with total_4:
        st.info('Median', icon="📌")
        st.metric(label="médiane de TVA", value=f"{RE001_1_median:,.0f}")
        
    with total_5:
        st.info('Ecart entre Ratio nombre de salariés sur CA et celui du secteur du contribuable.', icon="📌")
        st.metric(label="RE004.6", value=numerize(RE004_6), help=f"""Total de RE004.6: {RE004_6} """)
        
    st.markdown("""---""")



def graphs():
    #total_Ecart_entre_Chiffres_d_affaires_à_l_IR_et_à_la_TVA = int(df_selection["RE001.1"]).sum()
    #moyenneRE004_6 = int(round(df_selection["RE004.6"]).mean(),2)
    
    #simple bar
    
    Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM = (
        df_selection.groupby(by= ["RE004.4"]).count()[["RE001.1"]].sort_values(by="RE001.1")
    )
    
    fig_RE001_1 = px.bar(
        Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM,
        x="RE001.1",
        y=Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM.index,
        orientation="h",
        title="<b>RE001_1 par RE004_4 </b>",
        color_discrete_sequence= ["#0083b8"]*len(Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM),
        template= "plotly_white",
    )
    
    fig_RE001_1.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis= (dict(showgrid=False))
    )
    
    #simple ligne
    
    Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM_stat = df_selection.groupby(by= ["RE004.5"]).count()[["RE001.1"]]
    
    fig_RE004_5 = px.line(
        Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM_stat,
        x=Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM_stat.index,
        y="RE001.1",
        orientation="v",
        title="<b>RE001_1 par Statistique </b>",
        color_discrete_sequence= ["#0083b8"]*len(Ecart_entre_les_charges_sur_Etats_financiers_et_les_achats_et_sommes_versées_sur_DCOM_stat),
        template= "plotly_white",
    )
    
    fig_RE004_5.update_layout(
        xaxis= dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis= (dict(showgrid=False))
    )
    
    left,right = st.columns(2)
    left.plotly_chart(fig_RE004_5,use_container_width=True)
    right.plotly_chart(fig_RE001_1,use_container_width=True)

# Home()
# graphs()
#ProgressBar()

def ProgressBar():
    st.markdown("""<style>.stProgress > div > div > div > div{background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""",unsafe_allow_html=True,)
    target = 300
    current = df_selection["RE001.1"].sum()
    percent=round((current/target*100))
    myBar= st.progress(0)
    
    if percent>100:
        st.subheader("objectif atteint!")
    else:
        st.write("Vous avez",percent,"%", "pour", (format(target, 'd')), "RE001.2")
        for percent_complete in range(percent):
            time.sleep(0.1)
            myBar.progress(percent_complete+1,text="pourcentage cible")
            
def sideBar():
    
    selected = option_menu(
            menu_title="Menu principal",
            options= ["Home" , "Progression"],
            icons= ["house","eye"],
            menu_icon= "cast",
            default_index=0,
            orientation="horizontal"
        )
    if selected == "Home":
        st.subheader(f"Page: {selected}")
        Home()
        graphs()
    if selected == "Progression":
        st.subheader(f"Page: {selected}")
        ProgressBar()
        graphs()
    
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu principal",
            options= ["Home" , "Progression"],
            icons= ["house","eye"],
            menu_icon= "cast",
            default_index=0
        )
    if selected == "Home":
        st.subheader(f"Page: {selected}")
        Home()
        graphs()
    if selected == "Progression":
        st.subheader(f"Page: {selected}")
        ProgressBar()
        graphs()
sideBar()

#theme

hide_st_style= """

<style>
#MenuPricipale {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""