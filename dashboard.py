import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import conception_carte
import gestion_database
import datetime

# Creation de l'instance générale de l'application
my_app = dash.Dash("Projet Datascience")
print("App created")
data = gestion_database.get_database_commune()
print("Data downloaded")

frontiere1 = conception_carte.create_frontiere1()
map1  = conception_carte.create_map(frontiere1)

frontiere2 = conception_carte.create_frontiere2()
map2  = conception_carte.create_map(frontiere2)

print("Map Downloaded")
my_app.layout = html.Div([
    html.H1('Project Datacience'),


    ######### INPUT######################
    dcc.Dropdown(
            id="Year",
            options= [{'label': str(year), 'value': year} for year in data['Year'].unique()],
            value = data['Year'].max()
        ),
    dcc.Dropdown(
            id="nom_departement",
            options= [{'label': str(commune), 'value': commune} for commune in data['nom_commune'].unique()],
            value = data['nom_commune'].max()
        ),
    #####################################
    # Graphe
    #     
    dcc.Graph(id='Number_paid_tax'),
    dcc.Graph(id='Cout_tax'),
    dcc.Graph(id = 'Asset_tax'),
    # Carte
    
    html.Iframe(id="map", srcDoc=open("map.html",'r').read(), height=500, width=600, title = "Carte de la moyenne des Impôts par commune INSEE en France" ),

    html.Iframe(id="map", srcDoc=open("map2.html",'r').read(), height=500, width=600, title = "Carte du nombre de taxe payé par commune INSEE en France" ),
    #html.Iframe(id="map", srcDoc=open("map.html").read())  
    
    #Fonction de mise à jour
    dcc.Interval(
            id='interval-component',
            interval=1*1000,  # en millisecondes
            n_intervals=0,
            disabled =False)
])
print("Project ready")

#############################################################################################
#############################################################################################

#Mis à jour de l'Histogramme du nombre de taxe payé
@my_app.callback(
        Output('Number_paid_tax', 'figure'),
        [Input('Year', 'value')]
    )
def update_nbTax(selected_year):
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        print("Number_paid_tax")
        filtered_df = data[data['Year'] == selected_year]
        fig = px.histogram(filtered_df, x="nom_commune", y="Number_of_Taxpayers")
        print("Histogram updated")
        return fig




#### Mis à jour Histogramme du coût des taxes
@my_app.callback(
    Output('Cout_tax', 'figure'),
    [Input('Year', 'value')]
)
def update_avAssets(selected_year):
    # Triez le DataFrame pour obtenir l'ordre décroissant des taxes payées par département
        print("histogram_top in progress")
        filtered_df = data[data['Year'] == selected_year]
        top_commune = filtered_df.sort_values(by="Average_Assets_in_Euro", ascending=False)
        fig = px.histogram(top_commune, x="nom_commune", y="Average_Assets_in_Euro", title="Coût des taxes de chaque commune")
        print("histogram_top updated")
        return fig 

#### Mis à jour Histogramme du coût des taxes
@my_app.callback(
    Output('Asset_tax', 'figure'),
    [Input('Year', 'value')]
)
def update_avTax(selected_year):
    # Triez le DataFrame pour obtenir l'ordre décroissant des taxes payées par département
        print("histogram_top in progress")
        filtered_df = data[data['Year'] == selected_year]
        top_commune = filtered_df.sort_values(by="Average_Tax_in_Euro", ascending=False)
        fig = px.histogram(top_commune, x="nom_commune", y="Average_Tax_in_Euro", title="Coût des taxes de chaque commune")
        print("histogram_top updated")
        return fig 

#### Mise à jour de la carte de la Carte 1
@my_app.callback(
        Output('map', 'srcDoc'),
        [Input('Year', 'value')]
    )

    # Fonction de mis à jour
def update_map1(selected_year):
        print("map1")
        filtered_df = data[data['Year'] == selected_year]
        print(filtered_df)
        #map = conception_carte.final_map(frontiere,filtered_df)
        conception_carte.Info_map1(map, frontiere1, filtered_df)
        print("map1_updated")
        
        return None 

#### Mise à jour de la carte de la Carte 2
@my_app.callback(
        Output('map', 'srcDoc'),
        [Input('Year', 'value')]
    )

    # Fonction de mis à jour
def update_map2(selected_year):
        print("map2")
        filtered_df = data[data['Year'] == selected_year]
        print(filtered_df)
        #map = conception_carte.final_map(frontiere,filtered_df)
        conception_carte.Info_map2(map, frontiere2, filtered_df)
        print("map2_updated")
        
        return None 
#######Mise à jour de la page
@my_app.callback(Output('content', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_content(n):
    # Insérez ici le code pour mettre à jour le contenu HTML
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    return f"Contenu mis à jour à {current_time}"


# Lancement de l'application
my_app.server.run(debug = True)
