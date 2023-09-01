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
    
    st.markdown('# Visão geral por países')

    # cities by country metric
    fig = gm.cities_by_country(country_list)
    st.plotly_chart(fig, use_container_width=True)
    
    # amount of expensive restaurants
    fig = gm.exp_rest_by_country(country_list)
    st.plotly_chart(fig, use_container_width=True)

    unique_cuisines, plate_for_two = st.columns(2)

    # different cuisines
    with unique_cuisines:
        fig = gm.unique_cuisines(country_list)
        st.plotly_chart(fig, use_container_width=True)

    # price for a plate for two
    with plate_for_two:
        fig = gm.plate_for_two(country_list)
        st.plotly_chart(fig, use_container_width=True)


    return None

if __name__ == "__main__":
    main()