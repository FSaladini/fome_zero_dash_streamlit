import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

from funcs import global_metrics as gm


def create_sidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "India", "South Africa", "Canada", "Qatar"],
    )

    return list(countries)

def main():
    st.set_page_config(page_title="Global", layout="wide")

    df = pd.read_csv('dataset/data.csv')
    country_list = create_sidebar(df)
    
    st.markdown('# Visão geral por cidades')

    # Cities with good restaurants
    fig = gm.rests_with_four_stars(country_list)
    st.plotly_chart(fig, use_container_width=True)
    
    cities_unique_cuisines, better_mean_average = st.columns(2)

    # cities with different cuisines
    with cities_unique_cuisines:
        fig = gm.cities_unique_cuisines(country_list)
        st.plotly_chart(fig, use_container_width=True)

    # price for a plate for two
    with better_mean_average:
        fig = gm.better_mean_average(country_list)
        st.plotly_chart(fig, use_container_width=True)

    # amount of expensive restaurants by city
    fig = gm.exp_rest_by_city(country_list)
    st.plotly_chart(fig, use_container_width=True)

    # amount of cheap restaurants by city
    fig = gm.chp_rest_by_city(country_list)
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":
    main()