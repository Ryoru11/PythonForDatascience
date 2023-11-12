

import folium
import json
import urllib.parse
import geopandas
import pipwin
import gestion_database
import pandas as pd
import plotly.express as px
import requests
from unidecode import unidecode

def create_map(frontiere):
  #Creation des frontières communales

  #Mise au point de la résolution et du centre de la carte
  coords = (46.8398094,2.5840685)
  map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=4)

  france = frontiere
  #Dessin des frontières sur la carte
  sf = lambda x :{'fillColor':'#E88300', 'fillOpacity':0, 'color':'#E84000', 'weight':0.5, 'opacity':0.5}
  folium.GeoJson( data = france, name ="The World", style_function =sf).add_to(map)
  #Sauvegarde de la carte dans map.html
  map.save(outfile='map.html')

  return map
#######################################
def create_frontiere1():
  print("Frontiere in progress")
  frontiere = geopandas.read_file('iris-millesime-france.geojson')
  frontiere = frontiere.rename(columns={'com_code': 'code_commune'})
  frontiere = frontiere.drop_duplicates(subset=['code_commune'])
  print(frontiere['code_commune'])
  #frontiere['nom_departement'] = frontiere['nom_departement'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  frontiere = frontiere[['code_commune','geometry']]
  frontiere['code_commune'] = frontiere['code_commune'].apply(lambda x: x[0])
  print("New Complete")
  print(frontiere)
  print("save complete")

  #frontiere = requests.get("communes.geojson")
  return frontiere

def Info_map1(map, frontiere, pop_data):
  print("Info map in progress")
  print(pop_data)
  final_df = frontiere.merge(pop_data, on = "code_commune")
  print("Fusion Complete")
  print("New model progress")
  folium.Choropleth(
    geo_data= final_df,                              # geographical data( code département dans "code")
    name='choropleth',
    data= final_df,                                  # numerical data
    columns=['code_commune', "Average_Tax_in_Euro"],# numerical data key/value pair
    key_on='feature.properties.code_commune',       # geographical property used to establish correspondance with numerical data
    fill_color='RdYlBu',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='Tax payé en euro',
    smooth_factor=0,
    Highlight= True,
    line_color = "#0000",
    ).add_to(map)
  print("New model Completed")
  folium.LayerControl().add_to(map)
  map.save(outfile='map.html')
  print("New model Online")
  return None

#################
def create_frontiere2():
  print("Frontiere in progress")
  frontiere = geopandas.read_file('contour-des-departements.geojson')
  frontiere = frontiere.rename(columns={'nom': 'nom_departement'})
  frontiere['nom_departement'] = frontiere['nom_departement'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  #frontiere = requests.get("communes.geojson")
  return frontiere

def Info_map2(map, frontiere, pop_data):
  print("Info map in progress")
  print(pop_data)
  final_df = frontiere.merge(pop_data, on = "nom_departement")
  print("Fusion Complete")
  print("New model progress")
  folium.Choropleth(
    geo_data= final_df,                              # geographical data( code département dans "code")
    name='choropleth',
    data= final_df,                                  # numerical data
    columns=['nom_departement', "Average_Tax_in_Euro"],# numerical data key/value pair
    key_on='feature.properties.nom_departement',       # geographical property used to establish correspondance with numerical data
    fill_color='RdYlBu',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='Tax payé en euro',
    smooth_factor=0,
    Highlight= True,
    line_color = "#0000",
    ).add_to(map)
  print("New model Completed")
  folium.LayerControl().add_to(map)
  map.save(outfile='map.html')
  print("New model Online")
  return None

