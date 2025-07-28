#--- Imports des packages
import pandas as pd

import plotly.express as px

import streamlit as st

import seaborn as sns
import matplotlib.pyplot as plt

#--- Import des données

df_temperatures = pd.read_pickle("data/Pickles/df_temperatures.pkl")

df_nationales = pd.read_pickle("data/Pickles/df_data_nationales.pkl")

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

import plotly.graph_objects as go

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


import plotly.express as px
#plt.title('Impact de la canicule sur la consommation')
#plt.ylabel('Consommation (kWh)')
st.write(fig)
