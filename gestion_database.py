################################
#Code réalisé par Alexandre NGUYEN pour le projet de Python et Datascience 2023
#Mis à jour le 12/11
#Le fichier 'gestion_database' contient le code permettant de gérer et traîter la database des Revenues en France sur plusieurs échelles. Pour chaque échelle, nous avons créer une fonction permettant de mettre les données à l'échelle de l'étude et de les normaliser pour que les données de ces documents soit identiques.


################################
################################
import pandas as pd

#Traitement de la database adaptée à l'échelle Communale
def get_database_commune():
  #Lecture du fichier 'Revenue_Fr.csv'
  database = pd.read_csv('Revenue_Fr.csv')

  #Renommer les colonnes pour faciliter les recherches
  database = database.rename(columns={'City': 'nom_commune','Commune_Code_INSEE': 'code_commune'})
  #Tri en fonction des années
  database = database.sort_values(['Year'])
  print("DatabaseFinish")
  #retourne la database à l'échelle communale
  return database
#################################

from unidecode import unidecode

#Traitement de la database adaptée à l'échelle Departementale
def get_database_departement():
  #Lecture du fichier 'Revenue_Fr.csv'
  database = pd.read_csv('Revenue_Fr.csv')
  #Mise à l'échelle Departementale en réalisant la somme des données numériques
  result = database.groupby(['Year', 'Department'])[['Number_of_Taxpayers', 'Average_Assets_in_Euro', 'Average_Tax_in_Euro']].sum().reset_index()
  result.to_csv('statistiques_par_departement_par_annee.csv', index=False)
  #Changer le nom de 'Departement' en 'nom_departement'
  result = result.rename(columns={'Department': 'nom_departement'})
  #Enlever les ponctuations et mettre en Majuscule.
  result['nom_departement'] = result['nom_departement'].apply(lambda x: unidecode(x).upper())
  #Retourne la database à l'échelle départementale
  return result

############################################
def get_database_region():
  #Lecture du fichier 'Revenue_Fr.csv'
  database = pd.read_csv('Revenue_Fr.csv')
  #Mise à l'échelle Regionale en réalisant la somme des données numériques
  result = database.groupby(['Year', 'Region'])[['Number_of_Taxpayers', 'Average_Assets_in_Euro', 'Average_Tax_in_Euro']].sum().reset_index()
  result.to_csv('statistiques_par_region_par_annee.csv', index=False)
  #Changer le nom de 'Region' en 'nom_region'
  result = result.rename(columns={'Region': 'nom_region'})
  #Enlever les ponctuations et mettre en Majuscule.
  result['nom_region'] = result['nom_region'].apply(lambda x: unidecode(x).upper())
  #Retourne la database à l'échelle régionale
  return result
