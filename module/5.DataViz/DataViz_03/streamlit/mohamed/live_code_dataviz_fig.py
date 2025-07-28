
import pandas as pd
import numpy as np
import matplotlib
import plotly.express as px
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import shapely
import geopandas as gpd
from datetime import timedelta
import matplotlib.pyplot as plt
import streamlit as st


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



plt.figure(figsize=(12, 8))

plt.plot(df_eol.index, df_eol['oceanique'], color='green', label='Océanique')
plt.plot(df_eol.index, df_eol['Occitanie'], color='red', label='Occitanie')
plt.plot(df_eol.index, df_eol['Grand-Est'], color='blue', label='Grand-Est')

plt.xlabel("Date en 2018")
plt.ylabel("Production en TWh")
plt.title("Production éolienne journalière en 2018")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 8))

plt.plot(df_sol.index, df_sol['oceanique'], color='green', label='Océanique')
plt.plot(df_sol.index, df_sol['Occitanie'], color='red', label='Occitanie')
plt.plot(df_sol.index, df_sol['Grand-Est'], color='blue', label='Grand-Est')

plt.xlabel("Date en 2018")
plt.ylabel("Production en TWh")
plt.title("Production solaire journalière en 2018")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


