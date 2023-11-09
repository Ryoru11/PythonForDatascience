

import folium
import json
import urllib.parse
import geopandas
import pipwin
import gestion_database
import plotly.express as px
import requests

def create_map():
  #Creation des frontières communales
  frontiere=create_frontiere()

  #Mise au point de la résolution et du centre de la carte
  coords = (46.8398094,2.5840685)
  map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6.5)

  france = frontiere
  #Dessin des frontières sur la carte
  sf = lambda x :{'fillColor':'#E88300', 'fillOpacity':0, 'color':'#E84000', 'weight':0.5, 'opacity':0.5}
  folium.GeoJson( data = france, name ="The World", style_function =sf).add_to(map)
  #Sauvegarde de la carte dans map.html
  map.save(outfile='map.html')

  return map

def create_frontiere():
  frontiere = geopandas.read_file('communes.geojson')
  #frontiere = requests.get("communes.geojson")
  return frontiere


def Info_map(map, frontiere, pop_data):
  print("Info map in progress")

  final_df = frontiere.merge(pop_data, on = "code_commune")
  print("Fusion Complete")
  print("New model progress")
  folium.Choropleth(
    geo_data= final_df,                              # geographical data( code département dans "code")
    name='choropleth',
    data= final_df,                                  # numerical data
    columns=['code_commune', "Average_Tax_in_Euro"],# numerical data key/value pair
    key_on='feature.properties.code_commune',       # geographical property used to establish correspondance with numerical data
    fill_color='YlGn',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='Tax payé en euro'
    ).add_to(map)
  print("New model Completed")
  folium.LayerControl().add_to(map)
  map.save(outfile='map.html')
  print("New model Online")
  return None

def final_map(data):
  frontiere = create_frontiere()
  print("creation de la map")
  map = px.choropleth_mapbox(data,
                             frontiere,
                             locations = 'code_commune',
                             color='Average_Tax_in_Euro',
                             color_continuous_scale="Viridis",
                             range_color=(0, 10000),
                             mapbox_style = "carto-positron",
                             zoom = 6.5,
                             center = {"lat": 46.8398094, "lon": 2.5840685} ,
                             opacity = 1,
                             labels = {'Average_ Tax_in_Euro': 'Moyenne des taxes'}
                             )
  print("Map ready")
  map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  map.show()
  return map
                            
