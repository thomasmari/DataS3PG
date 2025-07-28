# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:04:12 2025

@author: Elise
"""
# Import libraries

import pandas as pd
import numpy as np
import matplotlib
import plotly.express as px
import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import geopandas as gpd
import streamlit as st
#ols
import statsmodels.api as sm







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


