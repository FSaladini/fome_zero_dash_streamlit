import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

from funcs import global_metrics as gm


raw_data_path = '\dataset\zomato.csv'


def create_sidebar(df):
    image_path = "img/"
    image = Image.open(image_path + "icon.png")

    col1, col2 = st.sidebar.columns([1, 4], gap="small")
    col1.image(image, width=35)
    col2.markdown("# Fome Zero")

    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "India", "South Africa", "Canada", "Qatar"],
    )

    st.sidebar.markdown("### Dados Tratados")

    processed_data = pd.read_csv("dataset/data.csv")

    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )

    return list(countries)

def mapers(df):
    
    f = folium.Figure(width=1920, height=1080)
    m = folium.Map(max_bounds=False).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in df.iterrows():
        folium.Marker(
                [line["latitude"], line["longitude"]],
                icon=folium.Icon( icon="home", prefix="fa"),
                popup = line['restaurant_name']
            ).add_to(marker_cluster)


    folium_static(m, width=1024, height=768)



def main():

    df = pd.read_csv('dataset/data.csv')

    st.set_page_config(page_title="Home", layout="wide", initial_sidebar_state = "collapsed")

    selected_countries = create_sidebar(df)

    st.markdown("# Fome Zero!")

    st.markdown("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")

    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")

    rests, ctrs, cities, votes, cuisines = st.columns(5)

    rests.metric(
        "Restaurantes Cadastrados",
        gm.uni_rest(df),
    )

    ctrs.metric(
        "Países Cadastrados",
        gm.ctrs(df),
    )

    cities.metric(
        "Cidades Cadastrados",
        gm.cities(df),
    )

    votes.metric(
        "Avaliações Feitas na Plataforma",
        f"{gm.uni_avs(df):,}".replace(",", "."),
    )

    cuisines.metric(
        f"Tipos de Culinárias",
        f"{gm.uni_cui(df):,}",
    )

    # create map
    map_df = df.loc[df["country"].isin(selected_countries), :]
    mapers(map_df)

    return None

if __name__ == "__main__":
    main()


