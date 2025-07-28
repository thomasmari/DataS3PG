# Import libraries
#marie
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
#mohamed
import numpy as np
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import shapely
import geopandas as gpd
from datetime import timedelta
import matplotlib.pyplot as plt
import streamlit as st

#jamila
import seaborn as sns
import matplotlib.pyplot as plt
#thomas
import matplotlib
import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import statsmodels.api as sm #ols




# ### 1. Foisonnement de la production renouvelable en France :
# idée 1 : Par région : Barplot de la production anuelle par région, stacked (solaire éolien)\
# idée 2 : Évoluation (lineplot) au cours d'une année\
#     - faire des courbes différente par région ou type d'énergie produite.

# ### 2. Thermo-sensibilité de la consommation :
# idée 1 : Tracer deux lineplot évolution de la température dans le temps et évolution de la consommation dans le temps.
#         (moyenné par journée)

# idée optionelle : effet de la canicule sur la consommation

# ### 3. Mix énergétique en France :
# Stacked plot


##############marie
#--- Import des données

st.title("Energies en France")


def ene_renou():
    st.header("1. Production d'énergies renouvelables")

    st.write("L’éolien, au même titre que le photovoltaïque, est une énergie variable dont la production dépend des conditions météorologiques.")

    # st.subheader("**Lissage des énergies renouvelables grâce à la temporalité**")
    # st.write("Complémentarité entre l’éolien (automne/hiver) et le photovoltaïque (printemps/été).")

    # st.subheader("**Lissage d'une énergie grâce à la régionalité**")
    # st.write("Le foisonnement décrit la capacité de la production d’une zone climatique à compenser un excès ou un déficit de production dans une autre zone climatique.")
    # st.write("Si la variabilité de production entre les régions est forte, cette variabilité est lissée à l’échelle nationale.")

    st.subheader('**Répartition de la production en énergies renouvelables selon les régions**')
    st.write("La région PACA est la région produisant le plus d'énergies renouvelables.")
    st.write("Toutes les régions produisent plus d'énergie éolienne que d'énergie solaire.")
    st.write("La région Nouvelle Aquitaine est la région avec la production d'énergie renouvelable la plus équilibrée.")
    st.write("La région Occitanie est la région avec la production d'énergie renouvelable la plus deséquilibrée.")


    eol_sol_total_percent = pd.read_csv("eol_sol_percent.csv")
    eol_sol_total_unit = pd.read_csv("eol_sol_unit.csv")

    selected_y = st.selectbox("Sélectionner l'unité à afficher", ['GWh', 'Pourcentage'])

    energy_options = ['Production totale', "Production d'énergie éolienne", "Production d'énergie solaire"]

    selected_energies = st.multiselect("Sélectionner le type d'énergie à afficher", energy_options, default=energy_options)


    if selected_y == 'GWh':
        df = eol_sol_total_unit
    if selected_y == 'Pourcentage':
        df = eol_sol_total_percent


    fig = go.Figure()
    if 'Production totale' in selected_energies:
        fig.add_trace(go.Bar(
            x=df['nom'],
            y=df['total'],
            name='Production totale',
            marker_color='seagreen'
        ))
    if "Production d'énergie éolienne" in selected_energies:
        fig.add_trace(go.Bar(
            x=df['nom'],
            y=df['mean_wind_nrj_pdt'],
            name="Production d'énergie éolienne",
            marker_color='cadetblue'
        ))
    if "Production d'énergie solaire" in selected_energies:
        fig.add_trace(go.Bar(
            x=df['nom'],
            y=df['mean_solar_nrj_pdt'],
            name="Production d'énergie solaire",
            marker_color='indianred'
        ))

    fig.layout.title = "Production d'énergies renouvelables dans les régions françaises"

    if selected_y == 'GWh':
        fig.update_layout(yaxis=dict(title='GWh produced'))
    if selected_y == 'Pourcentage':
        fig.update_layout(yaxis=dict(title="Pourcentage de l'énergie produite totale"))

    fig.update_layout(barmode='group', xaxis_tickangle=-45)

    st.write(fig)

ene_renou()


##############Mohamed

def pres_mohamed():

    df_solaire = pd.read_pickle("../data/Pickles/df_solaire_norm.pkl")
    df_eolien = pd.read_pickle("../data/Pickles/df_eolien_norm.pkl")
    df_nationales = pd.read_pickle("../data/Pickles/df_data_nationales.pkl")
    df_temperatures = pd.read_pickle("../data/Pickles/df_temperatures.pkl")
    df_eolien["oceanique"] = df_eolien.iloc[:,[2, 3, 11]].sum(axis=1)
    df_solaire["oceanique"] = df_solaire.iloc[:,[2, 3, 11]].sum(axis=1)
    df_eolien = df_eolien.iloc[:,[12, 4, 9]]
    df_solaire = df_solaire.iloc[:,[12, 4, 9]]

    df_eolien18 = pd.DataFrame(df_eolien[["oceanique", "Grand-Est", "Occitanie"]].dropna(axis=0).resample('W').mean())
    df_solaire18 = pd.DataFrame(df_solaire[["oceanique", "Grand-Est", "Occitanie"]].dropna(axis=0).resample('W').mean())



    df_sol = df_solaire18[df_solaire18.index.year==2018]
    df_eol = df_eolien18[df_eolien18.index.year==2018]



    fig_1 = plt.figure(figsize=(12, 8))

    plt.plot(df_eol.index, df_eol['oceanique'], color='green', label='Océanique')
    plt.plot(df_eol.index, df_eol['Occitanie'], color='red', label='Occitanie')
    plt.plot(df_eol.index, df_eol['Grand-Est'], color='blue', label='Grand-Est')

    plt.xlabel("Date en 2018")
    plt.ylabel("Production en TWh")
    plt.title("Production éolienne journalière en 2018")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    st.write(fig_1)

    fig_2 = plt.figure(figsize=(12, 8))

    plt.plot(df_sol.index, df_sol['oceanique'], color='green', label='Océanique')
    plt.plot(df_sol.index, df_sol['Occitanie'], color='red', label='Occitanie')
    plt.plot(df_sol.index, df_sol['Grand-Est'], color='blue', label='Grand-Est')

    plt.xlabel("Date en 2018")
    plt.ylabel("Production en TWh")
    plt.title("Production solaire journalière en 2018")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    st.write(fig_2)

st.header("2. Production d'énergies renouvelables en France")
pres_mohamed()
##############jamila


def pres_jamila():
    #--- Import des données
    prefix_path = '../'
    df_temperatures = pd.read_pickle(prefix_path+"data/Pickles/df_temperatures.pkl")

    df_nationales = pd.read_pickle(prefix_path+"data/Pickles/df_data_nationales.pkl")

    consommation = pd.DataFrame(df_nationales['Consommation'].dropna(axis=0).resample('d').mean())

    temperatures = pd.DataFrame(df_temperatures.mean(axis=1).resample('d').mean())



    temperatures.reset_index(inplace=True)

    temperatures = temperatures.rename(columns={"date_validite":"DateTime",0:"temperature"})


    consommation = pd.DataFrame(df_nationales['Consommation'].dropna(axis=0).resample('d').mean())

    consommation.reset_index(inplace=True)

    df_temperatur_conso =pd.merge(temperatures,consommation,how='inner',on= 'DateTime')

    st.text("temperatures, Consommation")
    st.write(df_temperatur_conso)

    #--- Représentations graphiques des courbe de temperatures, Consommation
    fig = go.Figure()

    # Ajout de la courbe de consommation
    fig.add_trace(go.Scatter(
        x=df_temperatur_conso["DateTime"],
        y=df_temperatur_conso["Consommation"],
        name="Consommation",
        mode="lines",
        line=dict(color="blue")
    ))

    # Ajout de la courbe de température (2ème axe Y)
    fig.add_trace(go.Scatter(
        x=df_temperatur_conso["DateTime"],
        y=df_temperatur_conso["temperature"],
        name="Température",
        mode="lines",
        line=dict(color="red"),
        yaxis="y2"  # Associer à l'axe Y secondaire
    ))

    # Configuration des axes
    fig.update_layout(
        title="Consommation vs Température",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Consommation (kWh)", color="blue"),
        yaxis2=dict(title="Température (°C)", overlaying="y", side="right", color="red"),
        legend=dict(x=0.01, y=0.99)
    )

    st.write(fig)





    # Définition du seuil de canicule
    seuil_canicule = 25 
    seuil_froid = 15 

    # Si tes données sont horaires, il est préférable de les regrouper par jour
    df_jour = df_temperatur_conso.copy()
    df_jour['Date'] = pd.to_datetime(df_jour['DateTime']).dt.date
    df_jour = df_jour.groupby('Date').mean().reset_index()

    # Création d'une colonne "canicule" (True/False)
    df_jour['canicule'] = df_jour['temperature'] > seuil_canicule
    df_jour['froid'] = df_jour['temperature']< seuil_froid

    # Calcul des moyennes de consommation
    moyenne_canicule = df_jour[df_jour['canicule']]['Consommation'].mean()
    moyenne_hors_canicule = df_jour[~df_jour['canicule']]['Consommation'].mean()
    moyenne_jours_froid = df_jour[df_jour['froid']]['Consommation'].mean()

    moyenne_jours_tempere = df_jour[(~df_jour['canicule'])& (~df_jour['froid'])]['Consommation'].mean()


    print(f"Consommation moyenne en période de canicule : {moyenne_canicule:.2f} kWh")
    print(f"Consommation moyenne hors canicule : {moyenne_hors_canicule:.2f} kWh")
    print(f"Consommation moyenne tempere : {moyenne_jours_tempere:.2f} kWh")

    def classer_temperature(row):
        if row['canicule'] == 1:
            return 'canicule'
        elif row['froid'] == 1:
            return 'froid'
        else:
            return 'tempéré'

    df_jour['climat'] = df_jour.apply(classer_temperature, axis=1)

    st.text("Impact de la canicule sur la consommation")
    st.write(df_jour)

    # representation 

    import seaborn as sns
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    sns.boxplot(data=df_jour, x='climat', y='Consommation')


    plt.title('Impact de la canicule sur la consommation')
    plt.ylabel('Consommation (kWh)')
    st.write(fig)


    fig = px.box(df_jour, x='climat', y='Consommation')
    #plt.title('Impact de la canicule sur la consommation')
    #plt.ylabel('Consommation (kWh)')
    st.write(fig)

st.header("3. Évolution de la consommation énergétique en fonction de la température")
pres_jamila()


############################Thomas

def pres_thomas():
    #input
    df_data_nationales = pd.read_pickle('../data/Pickles/df_data_nationales_2012-23.pkl')
    #Data Processing
    #sampling and choosing features
    df_energy_monthly = df_data_nationales.resample('ME').sum()
    # df_energy_monthly = df_energy.set_index('DateTime').resample('ME').sum()
    col_prod = ['Nucléaire','Hydraulique','Gaz','Eolien','Bioénergies','Solaire','Charbon','Fioul']
    #computing proportions
    df_energy_monthly_total = df_energy_monthly[col_prod].sum(axis=1)
    df_prop = pd.DataFrame(index = df_energy_monthly.index.copy())
    for c in col_prod:
        df_prop[c] = df_energy_monthly[c]/df_energy_monthly_total*100

    #  st.selectbox(label="Groupé par :", option = [''], index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")

    #ploting
    import plotly.graph_objects as go

    fig1 = go.Figure()
    for prod_src in col_prod.__reversed__():
    # for prod_src in col_prod:
        fig1.add_trace(go.Scatter(
            x=df_energy_monthly.index,
            y=df_prop[prod_src],
            fill='tonexty',
            name=prod_src,
            stackgroup='one'
        ))

    fig1.update_layout(title='Proportions du mix Énergétique au cours du temps', xaxis_title='Temps', yaxis_title='proportion (en %)')
    # st.write(fig1,)
    st.plotly_chart(fig1, key="chart1")  # Unique key for first chart


    #plotting more interractive

    # Groupe 1 : Example label and options
    label = "Select Groupe 1"
    options_1 = col_prod
    # Correct usage of st.multiselect
    selected_options_1 = st.multiselect(label, options=options_1)
    # Display the selected options
    st.write("You selected:", selected_options_1)
    print(selected_options_1)
    # Groupe 2 : Example label and options
    label = "Select Groupe 2"
    # Correct usage of st.multiselect
    option_2 = st.selectbox(
        "Select Groupe 2",
        ('Rien','Complémentaire'),
        # default=('Rien')
    )
    st.write("You selected:", option_2,)# Display the selected options
    #data_processing

    #input
    #Data Processing

    # df_energy_monthly = df_energy.set_index('DateTime').resample('ME').sum()
    col_group = ['Groupe_1','Groupe_2']
    col_g1 = list(selected_options_1)
    if option_2 == 'Rien':
        col_group = ['Groupe_1']
        title=f"Évolution de la production groupée,<br>{col_group[0]} : {', '.join(col_g1)}"
    else :
        col_g2 = list(set(col_prod) - set(col_g1))
        col_group = ['Groupe_1','Groupe_2']
        title=f"Proportions du mix Énergétique au cours du temps,<br>{col_group[0]} : {', '.join(col_g1)},<br>{col_group[1]} : {', '.join(col_g2)}"
    
    df_energy_group = pd.DataFrame()
    if option_2 == 'Rien':
        df_energy_group[col_group[0]] = df_energy_monthly[col_g1].sum(axis=1)
    else : 
    #computing proportions
        df_energy_group[col_group[0]] = (df_energy_monthly[col_g1].sum(axis=1)/  df_energy_monthly_total *100).map(lambda x : float(x))
        df_energy_group[col_group[1]] = (df_energy_monthly[col_g2].sum(axis=1)/  df_energy_monthly_total *100).map(lambda x : float(x))

    df_prop = pd.DataFrame(index = df_energy_monthly.index.copy())
    for c in col_prod:
        df_prop[c] = (df_energy_monthly[c]/df_energy_monthly_total*100).map(lambda x : float(x))

    #ploting
    fig2 = go.Figure()
    for prod_src in col_group:
    # for prod_src in col_prod:
        fig2.add_trace(go.Scatter(
            x=df_energy_group.index,
            y=df_energy_group[prod_src],
            fill='tonexty',
            name=prod_src,
            stackgroup='one'
        ))
    if option_2=='Rien':
        df_pred = df_energy_group.reset_index().reset_index()
        Y = df_pred[col_group[0]].map(lambda x : float(x))
        X = df_pred['index']
        X = sm.add_constant(X)
        model = sm.OLS(Y,X)
        results = model.fit()
        a,b = results.params[1],results.params[0]
        df_pred['y_pred'] = a*df_pred['index']+b
        fig2.add_trace(go.Scatter(
            x=df_pred['DateTime'],
            y=df_pred['y_pred'],
            name=f"OLS : {np.format_float_scientific(a,precision=3)}x + {np.format_float_scientific(b,precision=3)}",
            fillcolor='red'
            # fill='tonexty',
            # stackgroup='one'
        ))
    else:
        df_pred = df_energy_group.reset_index().reset_index()
        Y = df_pred[col_group[0]]
        X = df_pred['index']
        X = sm.add_constant(X)
        model = sm.OLS(Y,X)
        results = model.fit()
        a,b = results.params[1],results.params[0]
        df_pred['y_pred'] = a*df_pred['index']+b
        fig2.add_trace(go.Scatter(
            x=df_pred['DateTime'],
            y=df_pred['y_pred'],
            name=f"OLS : {np.format_float_scientific(a,precision=3)}x + {np.format_float_scientific(b,precision=3)}",
            fillcolor='red'
            # fill='tonexty',
            # stackgroup='one'
        ))    



    fig2.update_layout(title=title, xaxis_title='Temps', yaxis_title='proportion (en %)')
    # st.write(fig2)
    st.plotly_chart(fig2, key="chart2")  # Unique key for second chart

st.header("4. Mix énergétique en France")
pres_thomas()

