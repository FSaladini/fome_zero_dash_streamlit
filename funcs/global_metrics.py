import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


df1 = pd.read_csv('dataset/data.csv')


# 1. Quantos restaurantes únicos estão registrados?
def uni_rest(df):
    unique_restaurant = df['restaurant_id'].nunique()
    return unique_restaurant    

# 2. Quantos países únicos estão registrados?
def ctrs(df):
    countries = df['country_code'].nunique()
    return countries

# 3. Quantas cidades únicas estão registradas?
def cities(df):
    cities = df['city'].nunique()
    return cities

# 4. Qual o total de avaliações feitas?
def uni_avs(df):
    votes = df['votes'].sum()   
    return votes

# 5. Qual o total de tipos de culinária registrados?
def uni_cui(df):
    cuisines = df['cuisines'].nunique()
    return cuisines

# 1. Qual o nome do país que possui mais cidades registradas?
def cities_by_country(countries):
    cities_by_country = df1[df1['country'].isin(countries)]
    cities_by_country = cities_by_country[['city', 'country']].groupby('country').count().sort_values('city', ascending=False).reset_index()
    fig = px.bar(
            cities_by_country,
            x="country",
            y="city",
            text="city",
            title="Quantidade de Cidades atendidas por País",
            labels={ "country": "Países", "city": "Quantidade de Cidades", },)

    return fig



# 3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
def exp_rest_by_country(countries):
    exp_rest_by_country = df1[df1['country'].isin(countries)]
    exp_rest_by_country = exp_rest_by_country[['restaurant_id', 'country']].loc[df1['price_range'] == 4].groupby('country').nunique().sort_values('restaurant_id', ascending=False).reset_index()

    fig = px.bar(
            exp_rest_by_country,
            x="country",
            y="restaurant_id",
            text="restaurant_id",
            title="Quantidade de restaurantes de alta gastronomia por País",
            labels={ "country": "Países", "restaurant_id": "Quantidade de restaurantes de alta gastronomia", },)

    return fig


# 4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
def unique_cuisines(countries):
    unique_cuisines = df1[df1['country'].isin(countries)]
    unique_cuisines = unique_cuisines[['country', 'cuisines']].groupby('country').nunique().sort_values('cuisines', ascending=False).reset_index()
    fig = px.bar(
            unique_cuisines,
            x="country",
            y="cuisines",
            text="cuisines",
            title="Quantidade de cozinhas diferentes por País",
            labels={ "country": "Paises", "cuisines": "Quantidade de tipos de cozinha", },)

    return fig


# 11. Qual a média de preço de um prato para dois por país?
def plate_for_two(countries):
    mean_price_for_two = df1[df1['country'].isin(countries)]
    mean_price_for_two = mean_price_for_two[['country', 'average_cost_for_two']].loc[df1['average_cost_for_two'] != 0].groupby('country').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
    fig = px.bar(
            mean_price_for_two,
            x="country",
            y="average_cost_for_two",
            text="average_cost_for_two",
            text_auto=".2f",
            title="Preço médio para duas pessoas (valores em moeda local)",
            labels={ "country": "Paises", "average_cost_for_two": "Valor médio em moeda local", },)

    return fig

# 2. Cidades com mais restaurantes com nota média acima de 4
def rests_with_four_stars(countries):
    good_rests = df1[df1['country'].isin(countries)]
    good_rests = good_rests[['city', 'aggregate_rating', 'country']].loc[df1['aggregate_rating'] > 4].groupby(['country', 'city']).count().sort_values('aggregate_rating', ascending=False).reset_index()
    fig = px.bar(
            good_rests.head(15),
            x="city",
            y="aggregate_rating",
            text="aggregate_rating",
            color='country',
            title="Top 15 cidades com mais restaurantes bem avaliados",
            labels={ "city": "Cidade", "aggregate_rating": "Quantidade de restaurantes bem avaliados", 'country': 'Países' },)

    return fig
# 2. Cidades com mais restaurantes cozinhas diferentes
def cities_unique_cuisines(countries):
    cuisines_by_city = df1[df1['country'].isin(countries)]
    cuisines_by_city = cuisines_by_city[['city', 'cuisines', 'country']].groupby(['country', 'city']).nunique().sort_values('cuisines', ascending=False).reset_index()
    fig = px.bar(
            cuisines_by_city.head(5),
            x="city",
            y="cuisines",
            text="cuisines",
            color='country',
            title="Top 5 cidades com mais tipos de gastronomia",
            labels={ "city": "Cidade", "cuisines": "Quantidade de tipos de gastronomia", 'country': 'Países' },)

    return fig


def better_mean_average(countries):
    mean_average = df1[df1['country'].isin(countries)]
    mean_average = mean_average[['city', 'aggregate_rating', 'country']].groupby(['country', 'city']).mean().sort_values('aggregate_rating', ascending=False).reset_index()
    fig = px.bar(
            mean_average.head(5),
            x="city",
            y="aggregate_rating",
            text="aggregate_rating",
            color='country',
            text_auto=".2f",
            title="Top 5 cidades com melhor média de avaliação",
            labels={ "city": "Cidade", "aggregate_rating": "Valor médio da avaliação", 'country': 'Países' },)

    return fig


def exp_rest_by_city(countries):
    exp_rest = df1[df1['country'].isin(countries)]
    exp_rest = exp_rest[['city', 'price_range', 'country']].loc[df1['price_range'] == 4].groupby(['country', 'city']).count().sort_values('price_range', ascending=False).reset_index()
    fig = px.bar(
            exp_rest.head(15),
            x="city",
            y="price_range",
            text="price_range",
            color='country',
            title="Índice de alta gastronomia",
            labels={ "city": "Cidade", "price_range": "Quantidade de restaurantes mais caros", 'country': 'Países' },)
    
    return fig

def chp_rest_by_city(countries):
    chp_rest = df1[df1['country'].isin(countries)]
    chp_rest = chp_rest[['city', 'price_range', 'country']].loc[df1['price_range'] == 1].groupby(['country', 'city']).count().sort_values('price_range', ascending=False).reset_index()
    fig = px.bar(
            chp_rest.head(15),
            x="city",
            y="price_range",
            text="price_range",
            color='country',
            title="Índice de baixa gastronomia",
            labels={ "city": "Cidade", "price_range": "Quantidade de restaurantes mais baratos", 'country': 'Países' },)
    
    return fig