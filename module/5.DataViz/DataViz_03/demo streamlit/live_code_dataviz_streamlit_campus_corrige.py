
#--- Imports des packages

import pandas as pd
import geopandas as gpd
import plotly.express as px

import streamlit as st


#--- Import des données

data_pop = pd.read_csv("data/Chiffres-des-naissances-et-des-deces---Metropole.csv") 

data_bornes = gpd.read_file("data/bornes recharge véhicules électriques métro grenoble.json")

st.text("Data naissances")
st.write(data_pop)



#--- Représentations graphiques des naissances dans la Métropole de Grenoble

st.header("Représentations graphiques des naissances dans la Métropole de Grenoble")

#sélecteur commune
com_select = st.multiselect(
    "Communes sélectionnées",
    data_pop["commune"].unique(),
    ["Grenoble"],
)

data_com_select = data_pop[data_pop["commune"].isin(com_select)]

#nombre de naissances par an (total sur toutes les communes)
data_pop_tot_com = pd.DataFrame(data_com_select.groupby('annee')['nombre_naissances'].sum()).reset_index()

#line chart
fig = px.line(data_pop_tot_com, x="annee", y="nombre_naissances",
             title="Evolution du nombre de naissances dans la Métropole de Grenoble",
             labels={"annee":"Année","nombre_naissances":"Nombre de naissances"}
             ) 
st.write(fig)

#bar chart
fig = px.bar(data_pop_tot_com, x="annee", y="nombre_naissances",
             title="Evolution du nombre de naissances dans la Métropole de Grenoble",
             labels={"annee":"Année","nombre_naissances":"Nombre de naissances"})
st.write(fig)



#--- Représenter des données géographiques

st.header("Carte des bornes de recharge électriques")

#carte
fig = px.scatter_mapbox(data_bornes,lat="Ylatitude", lon="Xlongitude", 
                        mapbox_style="carto-positron", #fond de carte
                        custom_data=["n_station","id_station"]) #pour customiser les variables qui apparaissent dans l'étiquette (quand on survole)

fig.update_traces(hovertemplate="<br>".join([ "Nom station : %{customdata[0]}", "ID station : %{customdata[1]}" ])) #pour customiser les variables qui apparaissent dans l'étiquette (quand on survole)
st.write(fig)