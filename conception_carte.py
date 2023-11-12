import folium
import geopandas
from unidecode import unidecode
from urllib import request

URL = "https://bpce.opendatasoft.com/api/explore/v2.1/catalog/datasets/iris-millesime-france/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
response = request.urlretrieve(URL, "iris-millesime-france.geojson")
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




