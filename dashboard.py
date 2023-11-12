import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import conception_carte
import gestion_database


# Creation de l'instance générale de l'application
my_app = dash.Dash("Projet Datascience")
print("App created")
data_commune = gestion_database.get_database_commune()
data_departement = gestion_database.get_database_departement()
data_region = gestion_database.get_database_region()
print("Data downloaded")
print("Frontieres in progress")

frontiere_commune = conception_carte.create_frontiere_commune()
frontiere_departement = conception_carte.create_frontiere_departement()
frontiere_region = conception_carte.create_frontiere_region()

print("frontieres Downloaded")
my_app.layout = html.Div([
    html.H1('Project Datacience'),


    ######### INPUT###################### 
    html.H3("Choisissez vos données"),  

    html.H4("Choisissez l'année"),
    dcc.Slider(id = "Year",
               min = data_commune['Year'].min(),
               max = data_commune['Year'].max(),
               step = 1,
               value = 2019,
               tooltip = {"placement": "bottom", "always_visible":True},
               updatemode = "drag",
               persistence = True,
               persistence_type ='session'
               ),

    html.H4("Choisissez le type de données"),
    dcc.Dropdown(
          id = "Type_de_donnees",
          options= ["Nombre d'impôt payé", "Cout des impôts", "Assets des impôts"],
          value = "Nombre d'impôt payé"
    ),
    html.H4("Choisissez l'échelle"),
    dcc.Dropdown(
            id="Echelle",
            options= ["Region", "Departement", "Commune"],
            value = "Commune"
        ),
    #####################################
    # Graphe
    #
    html.H3("Graphique"),
    dcc.Graph(id='graph'),

    html.H3("Histogramme"),
    dcc.Graph(id='histogramme'),

    # Carte
    html.H3("Carte"),
    dcc.Graph(id='map'),

    # Tableau

    html.H3("Tableau"),
    dash.dash_table.DataTable(id ='dataset')



])
print("Project ready")

#############################################################################################
#############################################################################################

#Mis à jour du graphique
@my_app.callback(
        Output('graph', 'figure'),
        Input('Year', 'value'),
        Input('Type_de_donnees', 'value'),
        Input('Echelle', 'value')
    )
def update_Graphique(year_value, type_de_donnees_value, echelle_value):
        # Créer un histogramme 
        print("graph in progress")
        #Choix du type de données à afficher
        if type_de_donnees_value == "Nombre d'impôt payé":
              type = "Number_of_Taxpayers"
        elif type_de_donnees_value == "Cout des impôts":
              type = "Average_Tax_in_Euro"
        else:
              type = "Average_Assets_in_Euro"
        
        #Choix de l'échelle
        if echelle_value == "Region":
              f_data = data_region
              nom = "nom_region"
        elif echelle_value == "Departement":
              f_data = data_departement
              nom = "nom_departement"
        else:
              f_data = data_commune
              nom = "nom_commune"
        

        filtered_df = f_data[f_data['Year'] == year_value]
        fig = px.histogram(filtered_df, x= nom, y= type)
        print("graph updated")
        return fig

#Mis à jour de l'histogramme
@my_app.callback(
        Output('histogramme', 'figure'),
        Input('Year', 'value'),
        Input('Type_de_donnees', 'value'),
        Input('Echelle', 'value')
    )
def update_Histogramme(year_value, type_de_donnees_value, echelle_value):
        # Créer un histogramme 
        print("Histogram in progress")
        #Choix du type de données à afficher
        if type_de_donnees_value == "Nombre d'impôt payé":
              type = "Number_of_Taxpayers"
        elif type_de_donnees_value == "Cout des impôts":
              type = "Average_Tax_in_Euro"
        else:
              type = "Average_Assets_in_Euro"
        
        #Choix de l'échelle
        if echelle_value == "Region":
              f_data = data_region
              nom = "nom_region"
        elif echelle_value == "Departement":
              f_data = data_departement
              nom = "nom_departement"
        else:
              f_data = data_commune
              nom = "nom_commune"
        

        filtered_df = f_data[f_data['Year'] == year_value]
        fig = px.histogram(filtered_df, x= type)
        print("Histogram updated")
        return fig


#### Carte
@my_app.callback(
        Output('map', 'figure'),
        Input('Year', 'value'),
        Input('Type_de_donnees', 'value'),
        Input('Echelle', 'value')
        )

def display_choropleth(year_value, type_de_donnees_value, echelle_value):
    
    print("mapcom in progress")
    
    if type_de_donnees_value == "Nombre d'impôt payé":
              type = "Number_of_Taxpayers"
    elif type_de_donnees_value == "Cout des impôts":
              type = "Average_Tax_in_Euro"
    else:
        type = "Average_Assets_in_Euro"


        #Choix de l'échelle
    if echelle_value == "Region":
              f_data = data_region
              frontiere = frontiere_region
              nom = "nom_region"
              zoom_rate = 4
    elif echelle_value == "Departement":
              f_data = data_departement
              frontiere = frontiere_departement
              nom = "nom_departement"
              zoom_rate = 6
    else:
              f_data = data_commune
              frontiere = frontiere_commune
              nom = "code_commune"
              zoom_rate = 9
    fig = px.choropleth_mapbox(
        f_data, geojson= frontiere, color=type,
        locations= nom,
        featureidkey="properties."+nom, 
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        center={"lat": 48.856614, "lon": 2.3522219}, zoom=zoom_rate,
        opacity=0.5,

        template="plotly_dark",
        labels={type:type_de_donnees_value})
    
    print("mapcom updated")

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        )

    return fig


# Lancement de l'application
my_app.server.run(debug = False)
