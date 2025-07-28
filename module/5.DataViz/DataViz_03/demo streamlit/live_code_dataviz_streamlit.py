# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:04:12 2025

@author: Elise
"""

import pandas as pd
import plotly.express as px

import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPolygon

import matplotlib
import geopandas as gpd



#---Chargement des données
data_pop = pd.read_csv("data/Chiffres-des-naissances-et-des-deces---Metropole.csv")

data_pop_gre = data_pop[data_pop["commune"]=="Grenoble"]


data_bornes = gpd.read_file("data/bornes recharge véhicules électriques métro grenoble.json")



#---Graphiques et tableau

#st.set_page_config(layout="wide") #pour étendre sur toute la largeur de la page

#Représentations graphiques des naissances à Grenoble

communes_select = ["Grenoble"]

data_com_select = data_pop[data_pop["commune"].isin(communes_select)]

data_annee_com_select = pd.DataFrame(data_com_select.groupby('annee')['nombre_naissances'].sum()).reset_index()

fig = px.line(data_annee_com_select, x="annee", y="nombre_naissances",
             title="Evolution du nombre de naissances",
             labels={"annee":"Année","nombre_naissances":"Nombre de naissances"}) #noms des axes
fig.show()


fig = px.bar(data_annee_com_select, x="annee", y="nombre_naissances",
             title="Evolution du nombre de naissances",
             labels={"annee":"Année","nombre_naissances":"Nombre de naissances"})
fig.show()


#Carte des bornes de recharge électriques

fig = px.scatter_mapbox(data_bornes,lat="Ylatitude", lon="Xlongitude", 
                        mapbox_style="carto-positron", #fond de carte
                        custom_data=["n_station","id_station"]) #pour customiser les variables qui apparaissent dans l'étiquette (quand on survole)

fig.update_traces(hovertemplate="<br>".join([ "Nom station : %{customdata[0]}", "ID station : %{customdata[1]}" ])) #pour customiser les variables qui apparaissent dans l'étiquette (quand on survole)
fig.show()
