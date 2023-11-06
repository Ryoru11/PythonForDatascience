import plotly_express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import streamlit as st
import conception_carte
import gestion_database
from layout import get_layout
from callbacks import register_callbacks
import matplotlib.pyplot as plt

def dashboard():
    
    st.set_page_config(page_title= "Sales Dashboard", page_icon = 'profil.png', layout= "wide")
    data = gestion_database.get_database_commune()
    st.dataframe(data)
    st.map(conception_carte.Info_map(conception_carte.create_map(), data))
    plt.hist(data.Dist_norm)
    st.pyplot()
    

#-----------Sidebar-----------------

    st.sidebar.header("Filter by")
    commune = st.sidebar.multiselect(
        "Select the commune:",
        options = data["nom_commune"].unique(),
        default = data["nom_commune"].unique()
    )

    year = st.sidebar.multiselect(
    "Select the year: ",
    options = data["Year"].unique(),
    default = data["Year"].unique()
    )

    df_selection = data.query("nom_commune== @commune & Year== @year")

    st.dataframe(df_selection)
    return None     