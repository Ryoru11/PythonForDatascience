

import folium
import json
import urllib.parse
import geopandas
import pipwin
import gestion_database

def create_map():
  #Creation des frontières communales
  frontiere=create_frontiere()

  #Mise au point de la résolution et du centre de la carte
  coords = (46.8398094,2.5840685)
  map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6.5)

  france = frontiere
  #Dessin des frontières sur la carte
  sf = lambda x :{'fillColor':'#E88300', 'fillOpacity':0.5, 'color':'#E84000', 'weight':1, 'opacity':1}
  folium.GeoJson( data = france, name ="The World", style_function =sf).add_to(map)
  #Sauvegarde de la carte dans map.html
  map.save(outfile='map.html')

  return map

def create_frontiere():
  frontiere = geopandas.read_file('communes.geojson')

  return frontiere


def Info_map(map, pop_data):
  frontiere = create_frontiere()
  annees = pop_data['Year'].unique()
  for an in annees:
    data_an = pop_data[pop_data['Year'] == an]
    print(frontiere)
    folium.Choropleth(
    geo_data= frontiere,                              # geographical data( code département dans "code")
    name='choropleth',
    data= data_an,                                  # numerical data
    columns=['code_commune', 'Average_Tax_in_Euro'],                     # numerical data key/value pair
    key_on='feature.properties.code_commune',       # geographical property used to establish correspondance with numerical data
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Tax payé en euro'
    ).add_to(map)

    map.save(outfile='map{an}.html')
    map
  return map