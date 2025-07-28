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







#input
# df_data_nationales = pd.read_pickle('../data/Pickles/df_data_nationales.pkl')
#Data Processing
#sampling and choosing features
df_energy_monthly = df_data_nationales.resample('ME').sum()
# df_energy_monthly = df_energy.set_index('DateTime').resample('ME').sum()
col_prod = ['Nucléaire','Hydraulique','Gaz','Eolien','Charbon','Bioénergies','Solaire','Fioul']
df_energy_monthly[col_prod]
#computing proportions
df_energy_monthly_total = df_energy_monthly[col_prod].sum(axis=1)
df_prop = pd.DataFrame(index = df_energy_monthly.index.copy())
for c in col_prod:
    df_prop[c] = df_energy_monthly[c]/df_energy_monthly_total*100

#ploting
import plotly.graph_objects as go

fig = go.Figure()
# for prod_src in col_prod.__reversed__():
for prod_src in col_prod:
    fig.add_trace(go.Scatter(
        x=df_energy_monthly.index,
        y=df_prop[prod_src],
        fill='tonexty',
        name=prod_src,
        stackgroup='one'
    ))

fig.update_layout(title='Proportions du mix Énergétique au cours du temps', xaxis_title='Temps', yaxis_title='proportion (en %)')
fig.show()