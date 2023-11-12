import folium
import geopandas
import pandas as pd
import plotly.express as px
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
  map.save(outfile='mapcom.html')

  return map
#######################################
def create_frontiere_commune():
  print("Frontiere in progress")
  frontiere = geopandas.read_file('iris-millesime-france.geojson')
  frontiere = frontiere.rename(columns={'com_code': 'code_commune'})
  frontiere = frontiere.drop_duplicates(subset=['code_commune'])
  print("Frontiere Complete")
  frontiere = frontiere[['code_commune','geometry']]
  frontiere['code_commune'] = frontiere['code_commune'].apply(lambda x: x[0])
  print("New Complete")

  return frontiere


def create_frontiere_region():
  print("Frontiere in progress")
  frontiere = geopandas.read_file('regions.geojson')
  frontiere = frontiere.rename(columns={'nom': 'nom_region'})
  frontiere['nom_region'] = frontiere['nom_region'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  return frontiere


def create_frontiere_departement():
  print("Frontiere in progress")
  frontiere = geopandas.read_file('contour-des-departements.geojson')
  frontiere = frontiere.rename(columns={'nom': 'nom_departement'})
  frontiere['nom_departement'] = frontiere['nom_departement'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  return frontiere




