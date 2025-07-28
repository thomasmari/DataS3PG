import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go


import streamlit as st

#--- Import des données

st.title("Energies en France")


def ene_renou():
    st.header("Production d'énergies renouvelables")

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

