################################
#Code réalisé par Alexandre NGUYEN pour le projet de Python et Datascience 2023
#Mis à jour le 12/11
#Le fichier 'conception_carte' contient le code permettant de réaliser une carte de la France sur plusieurs échelles. Pour chaque échelle, nous avons développer une fonction permettant de créer les frontières et les normaliser pour que les éléments de ces documents soit identiques à la database.


################################
import geopandas
from unidecode import unidecode
from urllib import request

#Importation de "iris-millesime-france.geojson" contenant les coordonnées des frontières des communes INSEE
URL = "https://bpce.opendatasoft.com/api/explore/v2.1/catalog/datasets/iris-millesime-france/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
response = request.urlretrieve(URL, "iris-millesime-france.geojson")


#######################################
#Creation des frontières communales
def create_frontiere_commune():
  print("Frontiere in progress")
  #Lecture du fichier 'iris-millesime-france.geojson'
  frontiere = geopandas.read_file('iris-millesime-france.geojson')
  #Renommer la colonne 'com_code' en 'code_commune' pour faciliter le traitement avec la base de donnée
  frontiere = frontiere.rename(columns={'com_code': 'code_commune'})
  #Elimination des duplications qui ont le même code commune
  frontiere = frontiere.drop_duplicates(subset=['code_commune'])
  print("Frontiere Complete")
  #Simplification des données de frontière car il contenait 32 colonnes au total. Nous avons décider de prendre la décision de réduire le tableau car nous essayons de limiter le temps d'éxécution de la machine
  frontiere = frontiere[['code_commune','geometry']]
  #Les données dans la colonne 'code_commune' dans frontiere sont dans des listes à une valeur. Nous devons extraire les valeurs des tableaux et les replacer dans le tableau en tant que integer
  frontiere['code_commune'] = frontiere['code_commune'].apply(lambda x: x[0])
  print("New Complete")
  # Tableau des frontières des communes en sortie
  return frontiere

########################################
#Creation de frontière régionale
def create_frontiere_region():
  print("Frontiere in progress")
  #Lecture du fichier 'regions.geojson'
  frontiere = geopandas.read_file('regions.geojson')
  #Renommer la colonne 'nom' en 'nom_region' pour faciliter la lisibilité et le traitement avec la base de donnée
  frontiere = frontiere.rename(columns={'nom': 'nom_region'})
  # Normalisation de 'nom_region' en majuscule et sans ponctuation
  frontiere['nom_region'] = frontiere['nom_region'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  # Tableau des frontières des régions en sortie
  return frontiere

##########################################
#Creation de frontière départementale
def create_frontiere_departement():
  print("Frontiere in progress")
  #Lecture du fichier 'contour-des-departements.geojson'
  frontiere = geopandas.read_file('contour-des-departements.geojson')
  #Renommer la colonne 'nom' en 'nom_departement' pour faciliter la lisibilité et le traitement avec la base de donnée
  frontiere = frontiere.rename(columns={'nom': 'nom_departement'})
  # Normalisation de 'nom_departement' en majuscule et sans ponctuation
  frontiere['nom_departement'] = frontiere['nom_departement'].apply(lambda x: unidecode(x).upper())
  print("Frontiere Complete")
  # Tableau des frontières des départements en sortie
  return frontiere


