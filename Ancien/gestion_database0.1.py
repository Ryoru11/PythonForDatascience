import pandas as pd

def get_database_commune():
  database = pd.read_csv('Revenue_Fr.csv')

  #Renommer les colonnes pour faciliter les recherches
  database = database.rename(columns={'City': 'nom_commune','Commune_Code_INSEE': 'code_commune'})
  #Tri en fonction des années
  database = database.sort_values(['Year'])
  database.to_csv('statistiques_par_commune_par_annee.csv', index=False)

  return database
