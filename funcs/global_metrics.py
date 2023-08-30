import pandas as pd
import streamlit as st
import numpy as np

df1 = pd.read_csv('dataset\data.csv')


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


