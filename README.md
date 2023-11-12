# **User Guide**

## 1- Introduction du projet

Le traitement des données est un élément important de nos jours. Avec le développement des nouvelles technologies et de l'intelligence artificielle, la visualisation et l'interprétation des données est important dans la prise de décision pour pouvoir comprendre des événements.
Dans le cadre de notre projet, nous allons concevoir un dashboard intéractif en langage Python. Notre objectif est de créer une interface d'affichage d'un jeu de données de façon structuré et accessible. Nous allons créer un moyen d'intéraction avec la base de donnée en offrant des fonctionnalités d'analyse et de manipulation de ces derniers en temps réels.

Python est un des langages de programmation les plus répandus dans le monde. Notamment grâce à sa facilité d'utilisation et son vaste écosystème de bibliothèques dédiées à la visualisation de données, telles que Matplotlib, Seaborn, et Plotly.Ces outils offrent une variété de possibilités pour la création de visualisations de données interactives et informatives.

## 2- La base de données

Pour notre projet nous avons dû d'abord choisir un dataset avec lequel il nous fallait travailler, nous avons choisi un dataset issu du site web Kaggle. [Data](https://www.kaggle.com/datasets/santiagopatioserna/5-year-french-wealth-analysis),
La source de ce dataset est : [Source](https://www.data.gouv.fr/fr/datasets/impot-de-solidarite-sur-la-fortune-impot-sur-la-fortune-immobiliere-par-collectivite-territoriale/) soit un site du gouvernement français.
Notre dataset comporte 9 colonnes distinctes qui sont : Year, Commune_code_INSEE, number_of_taxpayers, City, Average_Assets_in_Euro, Average_Tax_in_Euro, source_file, Department, Region. Ce dataset présente différentes informations fiscales des habitants en fonction des différents endroits. Pour les fichiers GeoJsons, nous avons pris 3 fichiers représentant chacun une échelle différente: 
1. [Région](https://france-geojson.gregoiredavid.fr/)
2. [Département](https://france-geojson.gregoiredavid.fr/)
3. [Commune](https://bpce.opendatasoft.com/explore/dataset/iris-millesime-france/export/?disjunctive.reg_name&disjunctive.dep_name&disjunctive.arrdep_name&disjunctive.ze2020_name&disjunctive.bv2022_name&disjunctive.epci_name&disjunctive.ept_name&disjunctive.com_name&disjunctive.com_arm_name&disjunctive.iris_name&sort=com_code&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImlyaXMtbWlsbGVzaW1lLWZyYW5jZSIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUucmVnX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLmRlcF9uYW1lIjp0cnVlLCJkaXNqdW5jdGl2ZS5hcnJkZXBfbmFtZSI6dHJ1ZSwiZGlzanVuY3RpdmUuemUyMDIwX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLmJ2MjAyMl9uYW1lIjp0cnVlLCJkaXNqdW5jdGl2ZS5lcGNpX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLmVwdF9uYW1lIjp0cnVlLCJkaXNqdW5jdGl2ZS5jb21fbmFtZSI6dHJ1ZSwiZGlzanVuY3RpdmUuY29tX2FybV9uYW1lIjp0cnVlLCJkaXNqdW5jdGl2ZS5pcmlzX25hbWUiOnRydWUsInNvcnQiOiJ5ZWFyIn19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJsaW5lIiwiZnVuYyI6IkNPVU5UIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzUxMjQ3MiJ9XSwieEF4aXMiOiJ5ZWFyIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIifV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9) Dû à une taille importante du fichier, vous devez impérativement télécharger le GeoJson de Commune via ce lien et le mettre dans le même répertoire que 'conception_carte.py' et 'dashboard.py' 

## 3- Les librairies

Pour le développement de ce projet, nous avons utilisé les librairies suivantes:
- '$ python -m pip -r install pipwin'
- '$ python -m pip -r install gdal'
- '$ python -m pip -r install fiona'
- '$ python -m pip -r install pandas'
- '$ python -m pip -r install unidecode'
- '$ python -m pip -r install geopandas'
- '$ python -m pip -r install datapackage'
- '$ python -m pip -r install dash'
- '$ python -m pip -r install plotly.express'

## 4- Présentation du site

Notre dashboard se divise en 4 parties distinctes:
1. La sélection de données
2. Le graphique des données choisies
3. L'histogramme des données choisies
4. La carte choropleth des données choisies

### A-La sélection de données
Dans le cadre de ce projet, nous avons voulu rendre l'interaction le jeu de données la plus vaste possible. Pour cela, nous mettons à disposition 3 facteurs les plus déterminant de la base de donnée à choisir. Parmi elle, nous retrouvons:
1. L'année d'étude
2. Le type de données à étudier
3. L'échelle de l'étude

   
Pour l'année, nous donnons le choix entre les valeurs suivantes: 2019,2020,2021,2022.
Pour le type de données, nous donnons le choix entre les valeurs suivantes: Nombre d'impôt payé, Coût des impôts, Assets des impôts.
Pour l'échelle, nous donnons le choix entre les valeurs suivantes: Commune, Département, Région.
A chaque modification de ces données, les éléments suivants vont se mettre à jour en fonction du choix réaliser.

### B-Le graphique des données choisies
Nous vous proposons ici de mettre dans la forme d'un graphique la représentation de l'année choisi des types de données de chaque élément de l'échelle demandé. Cela permettra de réaliser des comparaisons de chaque élément.

### C-L'histogramme des données à étudier
Grâce à cet histogramme, nous pouvons observer la distribution des valeurs des types de données des types d'élément choisi sur l'année choisi.

### D- La carte choropleth
Avec le choropleth, nous donnons la possibilité d'observer la répartition des données déterminées sur l'échelle de la France en fonction des années.



# Rapport d'analyse

# Developper guide
