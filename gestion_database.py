import pandas as pd

def get_database_commune():
  database = pd.read_csv('Revenue_Fr.csv')

  #Renommer les colonnes pour faciliter les recherches
  database = database.rename(columns={'City': 'nom_commune','Commune_Code_INSEE': 'code_commune'})
  #Tri en fonction des années
  database = database.sort_values(['Year'])
  database.to_csv('statistiques_par_commune_par_annee.csv', index=False)
  print("DatabaseFinish")
  return database


from unidecode import unidecode
def get_database_departement():
  
  database = pd.read_csv('Revenue_Fr.csv')
  #Changement de la forme de Revenue_Fr en Département par année
  result = database.groupby(['Year', 'Department'])[['Number_of_Taxpayers', 'Average_Assets_in_Euro', 'Average_Tax_in_Euro']].sum().reset_index()
  result.to_csv('statistiques_par_departement_par_annee.csv', index=False)
  #Changer le nom de 'Departement' en 'nom_departement'
  result = result.rename(columns={'Department': 'nom_departement'})
  result['nom_departement'] = result['nom_departement'].apply(lambda x: unidecode(x).upper())
  return result


def get_database_region():
  
  database = pd.read_csv('Revenue_Fr.csv')
  #Changement de la forme de Revenue_Fr en Region par année
  result = database.groupby(['Year', 'Region'])[['Number_of_Taxpayers', 'Average_Assets_in_Euro', 'Average_Tax_in_Euro']].sum().reset_index()
  result.to_csv('statistiques_par_region_par_annee.csv', index=False)
  #Changer le nom de 'Departement' en 'nom_departement'
  result = result.rename(columns={'Region': 'nom_region'})
  #Fusion de 'statistiques_par_departement_par_annee.csv' avec 'departements-france.csv' pour avoir les codes départementaux selon le nom des départements.
#Enlever les accents+ tirets des deux et mettre en Majuscule.
  result['nom_region'] = result['nom_region'].apply(lambda x: unidecode(x).upper())

  return result