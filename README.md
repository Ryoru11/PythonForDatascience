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
- ' $ python -m pip -r install pipwin '
- ' $ python -m pip -r install gdal '
- ' $ python -m pip -r install fiona '
- ' $ python -m pip -r install pandas '
- ' $ python -m pip -r install unidecode '
- ' $ python -m pip -r install geopandas '
- ' $ python -m pip -r install datapackage '
- ' $ python -m pip -r install dash '
- ' $ python -m pip -r install plotly.express '

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

**___________________________________________________________________________________________________________________________________**
**___________________________________________________________________________________________________________________________________**
# **Rapport d'analyse**

Les différentes visualisations graphiques illustrent des aspects de la fiscalité et des revenus à travers différents départements de la France, offrant un aperçu des inégalités économiques régionales.

## 1- Graphique du type de donnée choisi en fonction des éléments de l'échelle choisie

Le premier graphique montre la somme de l'impôt moyen en euros par département. Il révèle des disparités notables dans la charge fiscale moyenne qui pourrait refléter les différences de revenus entre les départements. Par exemple, certains départements comme Paris affichent des barres beaucoup plus hautes que d'autres, ce qui indique une imposition moyenne plus élevée. Cela peut être attribué à la concentration de la richesse, de l'emploi, et des opportunités économiques dans la capitale par rapport aux autres régions françaises. À l'inverse, des départements plus petits ou ruraux, dans lesquels le coût de la vie est généralement plus bas et les revenus moyens inférieurs, montrent des montants d'imposition plus modestes.

## 2- Histogramme de répartition du type de donnée choisi à l'échelle choisie

L'histogramme montre une distribution fortement asymétrique avec une concentration élevée de cas dans la tranche d'imposition la plus basse, indiquant que la majorité des contribuables se situent dans cette catégorie. Cela suggère que la plupart des contribuables ont un impôt moyen relativement bas, ce qui pourrait refléter une prédominance de revenus moyens à faibles dans la population considérée. La chute rapide du nombre de cas plus le montant de l'impôt augmente montre que les contribuables avec un impôt moyen plus élevé sont nettement moins nombreux que les autres, ce qui est indicatif d'une répartition des revenus où peu de personnes atteignent des tranches supérieures.Il y a très peu de cas dans les tranches d'imposition plus élevées, ce qui peut indiquer une faible proportion de contribuables à haut revenu dans la population ou une capacité limitée de ces contribuables à générer des revenus exceptionnellement élevés.

## 3- Carte choropleth de répartition du type de donnée sur le territoire français

L'histogramme montre une distribution fortement asymétrique avec une concentration élevée de cas dans la tranche d'imposition la plus basse, indiquant que la majorité des contribuables se situent dans cette catégorie. Cela suggère que la plupart des contribuables ont un impôt moyen relativement bas, ce qui pourrait refléter une prédominance de revenus moyens à faibles dans la population considérée. La chute rapide du nombre de cas plus le montant de l'impôt augmente montre que les contribuables avec un impôt moyen plus élevé sont nettement moins nombreux que les autres, ce qui est indicatif d'une répartition des revenus où peu de personnes atteignent des tranches supérieures.Il y a très peu de cas dans les tranches d'imposition plus élevées, ce qui peut indiquer une faible proportion de contribuables à haut revenu dans la population ou une capacité limitée de ces contribuables à générer des revenus exceptionnellement élevés.

## Conclusion

En conclusion, ces graphiques mettent en évidence le contraste économique entre les différentes régions ou zones de la France. Ils soulignent l'existence d'une certaine centralisation économique, où des régions urbaines et économiquement dynamiques telles que Paris et Lyon portent une part disproportionnée de la charge fiscale du pays, tandis que d'autres régions peuvent avoir des niveaux de revenus et donc des contributions fiscales nettement inférieures. Ces différences illustrent la diversité économique de la France et peuvent avoir des implications importantes pour les politiques de développement régional et la redistribution fiscale.

**___________________________________________________________________________________________________________________________________**
**___________________________________________________________________________________________________________________________________**
# **Developper guide**

Le code de notre projet est divisé en 4 parties différentes:
- conception_carte.py
- gestion_database.py
- dashboard.py
- main.py
  
(Si vous êtes intéressé par l'hitorique de tout le programme, le lien est [ici](https://github.com/Ryoru11/PythonForDatascience/tree/main/Ancien))
  ## 1- conception_carte.py

  Le fichier 'conception_carte' contient le code permettant de réaliser une carte de la France sur plusieurs échelles.
  Pour chaque échelle, nous avons créer une fonction permettant de créer les frontières et les normaliser pour que les éléments 
  de ces documents soit identiques à la database.
  Pour ce fichier, nous avons utilisé les librairies 'geopandas', 'unidecode' de 'unidecode' et  'request' de 'urllib'.

  Dans un premier temps, nous avons importé un fichier volumineux à partir d'un lien source 'iris-millesime-france.geojson' à l'aide de la librairie 'urllib'.
  Dans la première fonction 'create_frontiere_commune', nous avons dessiner les frontières des communes recensées par l'INSEE en France.Nous avons utilisé le fichier 'iris-millesime-france.geojson' qui contient les différentes coordonnées permettant de dessiner les communes. Nous avons ensuite traîter les données comme ceci:
  - changement de nom de colonne de 'com_code' à 'code_commune' pour rattacher au set de données.
  - suppresion de toutes les duplications ayants le même 'code_commune'
  - sélection des données ('code_commune' et 'geometry') nécessaire pour diminuer le poid du tableau
  - normalisation de 'code_commune' en integer.

  Pour la seconde fonction 'create_frontiere_region', nous avons dessiner les frontières des régions de France. 
  Nous avons utilisé le fichier 'regions.geojson' qui contient les différentes coordonnées permettant de dessiner les régions. Nous avons ensuite traîter les données comme ceci:
  - changement de nom de colonne de 'nom' à 'nom_region' pour rattacher au set de données.
  - suppresion de toutes les duplications ayants le même 'nom_region'
  - normalisation de 'nom_region' en majuscule et sans ponctuation.

  Pour la dernière fonction 'create_frontiere_departement', nous avons dessiner les frontières des départements de France. 
  Nous avons utilisé le fichier 'contour-des-departements.geojson' qui contient les différentes coordonnées permettant de dessiner les départements. Nous avons ensuite traîter les données comme ceci:
  - changement de nom de colonne de 'nom' à 'nom_département' pour rattacher au set de données.
  - suppresion de toutes les duplications ayants le même 'nom_département'
  - normalisation de 'nom_departement' en majuscule et sans ponctuation.


  ## 2- gestion_database  

  Le fichier 'gestion_database' contient le code permettant de gérer et traîter la database des Revenues en France sur plusieurs échelles. Pour chaque échelle, nous avons créer une fonction permettant de mettre les données à l'échelle de l'étude et de les normaliser pour que les données de ces documents soit identiques. Pour ce fichier, nous avons utilisé les librairies: 'pandas' et 'unidecode'. 

  Dans la première fonction, 'get_database_commune', nous avons extrait les données du jeu de données pour réaliser une étude sur les communes en France.Nous avons utilisé le fichier 'Revenue_Fr.csv' qui contient les différentes données sur les Revenues et impôts en France. Nous avons ensuite traîter les données comme ceci:
  - tri des données en fonctions des années.
  - renommer les colonnes: 'City' en 'nom_commune' et 'Commune_Code_INSEE' en 'code_commune'.

  Dans la deuxième fonction, 'get_database_departement', nous avons extrait les données du jeu de données pour réaliser une étude sur les départements en France. Nous avons utilisé le fichier 'Revenue_Fr.csv' qui contient les différentes données sur les Revenues et impôts en France. Nous avons ensuite traîter les données comme ceci:
  - tri des données en fonctions des années et des départements.
  - renommer la colonne 'Department' en 'nom_departement'
  - Réalisation de la somme de 'Number_of_taxpayers', ' Average_Assets_in_Euro' et ' Average_Tax_in_Euro' de toutes les communes pour les adapter à l'échelle départementale.
  - normalisation de 'nom_departement' en majuscule et sans ponctuation avec l'aide de 'unidecode'. 

  Dans la dernière fonction, 'get_database_region', nous avons extrait les données du jeu de données pour réaliser une étude sur les régions en France. Nous avons utilisé le fichier 'Revenue_Fr.csv' qui contient les différentes données sur les Revenues et impôts en France. Nous avons ensuite traîter les données comme ceci:
  - tri des données en fonctions des années et des régions.
  - renommer la colonne 'Region' en 'nom_region'
  - Réalisation de la somme de 'Number_of_taxpayers', ' Average_Assets_in_Euro' et ' Average_Tax_in_Euro' de toutes les communes pour les adapter à l'échelle régionale.
  - normalisation de 'nom_region' en majuscule et sans ponctuation avec l'aide de 'unidecode'. 

## 3- dashboard.py

  Le fichier 'dashboard.py' gère les différentes instances du tableau de bord. Il permet de créer une vue d'ensemble rapide et compréhensible facilement de la situation que la base de données peut nous décrire, grâce à des instances visuelles.
Dans ce fichier, nous avons besoin d'importer les librairies 'dash', 'plotly.express', 'conception_carte' et 'gestion_database'.
La concetption du Dashboard est divisé en 3 parties: 

- Création des instances qui sont utilisés tout le long du programme
- Le layout de l'application
- Les fonctions de mise à jour/ fonction de callback.

### A- Création des instances

Dans cette première partie, nous avons créer les instances que nous allons utilisé. Nous créons ici:

  - L'application 'my_app' avec 'dash.Dash'
  - La database à différentes échelles ('data_commune', 'data_departement' et 'data_region') avec les fonctions de 'gestion_database'
  - Les frontières à différentes échelles ('frontiere_commune', 'frontiere_departement' et 'frontiere_region') avec les fonctions de 'conception_carte'.

### B- Layout de l'application

L'organisation de l'application se décline en quatre parties:

- Le choix des données
- Le graphique du type de données par rapport aux éléments de l'échelle
- L'histogramme des types de données
- La carte géographique des distributions du type de données.

Dans la partie choix de données, nous mettons à disposition 3 choix de facteurs les plus déterminant de la base de donnée. Ils seront utilisés notamment en tant que Input dans les fonctions de mise à jour des éléments . Parmi elles, nous retrouvons:

1. L'année d'étude
2. Le type de données à étudier
3. L'échelle de l'étude

Pour l'année, nous utilisons un slider pour chaque année avec 'dcc.Slider'. Le choix se fait entre les valeurs suivantes: 2019,2020,2021,2022. La valeur par défaut est 2019. Pour le type de données, nous utilisons un Dropdown pour chaque type de données avec 'dcc.Dopdown'. Le choix se fait entre les valeurs suivantes: Nombre d'impôt payé, Coût des impôts, Assets des impôts.
Pour l'échelle, nous utilisons un Dropdown pour chaque échelle avec 'dcc.Dropdown'. Le choix se fait entre les valeurs suivantes: Commune, Département, Région. A chaque modification de ces données, les éléments du Dashboard vont se mettre à jour avec les nouveaux choix réalisés.

Dans la seconde partie, le graphique représente le type de données à étudier en fonction des différents élements de l'échelle choisie. Il est mis à jour par la fonction update_Graphique que nous allons aborder dans la partie "Fonctions de mise à jour".

Dans la troisième partie, l'histogramme représente la tendance du type de données à étudier à l'échelle choisie. Il est mis à jour par la fonction update_Histogramme que nous allons aborder dans la partie "Fonctions de mise à jour". 

Dans la dernière partie, la carte choropleth de la France représente la répartition des données du type de données à l'échelle choisie.
Il est mis à jour par la fonction display_chropleth que nous allons aborder dans la partie "Fonctions de mise à jour".

## C- Fonctions de mise à jour/ Fonction de callback

Dans cette partie, chaque fonction de mise à jour et de Callback permet d'actualiser les éléments du layout à chaque modification des données. Pour chaque partie, nous allons appeler la fonction '@my_app.callback' pour faire le lien entre les fonctions et le layout de l'application. Dans le callback, nous allons utiliser les éléments Output et Input pour réaliser des mise à jour du layout. L'Output (sortie de fonction) permet de délivrer un élément de la fonction vers layout en direction de la partie ciblée avec l'id présent de chaque élément. 
L'Input (entrée de fonction) permet de recevoir des éléments en provenance du layout. Dans toutes les fonctions, les valeurs attribués viennent de la partie 'choix des données', soit 'Year', Type_de_donnes' et 'Echelle'.

Pour la mise à jour du **Graphique**, nous utilisons la fonction 'update_Graphique' qui prend en entrée l'année, le type de données et l'échelle. Pour chaque type de données, nous l'associons à une colonne du tableau de la base de données. Pour chaque échelle, nous l'associons à une data et à un nom de la colonne respective. Enfin, nous avons extrait les données en fonction de l'année. Nous dessinon ensuite un histogramme à l'aide de la librairie 'plotly.express' avec la commande 'px.histogram' qui prend en coordonnées: la data filtré, le nom de la colonne de l'échelle et le type de données à étudier. Il produit en sortie la figure du Graphique.

Pour la mise à jour de **Histogramme**, nous utilisons la fonction 'update_Histogramme' qui prend en entrée l'année, le type de données et l'échelle. Pour chaque type de données, nous l'associons à une colonne du tableau de la base de données. Pour chaque écheelle, nous l'associons à une data et à un nom de la colonne respective. Enfin, nous avons extrait les données en fonction de l'année. Nous dessinon ensuite un histogramme à l'aide de la librairie 'plotly.express' avec la commande 'px.histogram' qui prend en coordonnées: la data filtré,le type de données à étudier. Il produit en sortie la figure de l'Histogramme.

Pour la mise à jour de **Carte**, nous utilisons la fonction 'display_choropleth' qui prend en entrée l'année, le type de données et l'échelle. Pour chaque type de données, nous l'associons à une colonne du tableau de la base de données. Pour chaque échelle, nous l'associons à une data, un nom de la colonne respective, une frontière et le degrès de zoom. Enfin, nous avons extrait les données en fonction de l'année. Nous dessinon ensuite une carte choropleth à l'aide de la librairie 'plotly.express' avec la commande 'px.choropleth_mapbox' qui prend en coordonnées: la data filtré,le type de données à étudier, le degrès de zoom, la clé de l'id du paramètre étudié. Il produit en sortie la figure de la Carte.

## 4- main.py

Le fichier 'main' permet d'exécuter le programme et générer l'application. Il suffit d'importer le fichier 'dashboard.py'. La fonction main() permettra de lancer l'exécution de la fonction 'dashboard'.
