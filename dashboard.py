import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import conception_carte
import gestion_database

my_app = dash.Dash("Projet Datascience")
print("App created")
data = gestion_database.get_database_departement()
print("Data downloaded")
map  = conception_carte.create_map()
frontiere = conception_carte.create_frontiere()
#with open('map.html', 'r') as file:
#    map_html_content = file.read()
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
            options= [{'label': str(departement), 'value': departement} for departement in data['nom_departement'].unique()],
            value = data['nom_departement'].max()
        ),
    #####################################
    # Graphe    
    dcc.Graph(id='histogram'),
    
    dcc.Graph(id='Cout_tax'),
    # Carte
    #dcc.Graph(id = 'map'),
    
    html.Iframe(id="map", srcDoc=open("map.html",'r').read()),

    #html.Iframe(id="map", srcDoc=open("map.html").read())    
    
    #Fonction de mise à jour
    dcc.Interval(
            id='interval-component',
            interval=10*1000,  # en millisecondes
            n_intervals=60)
])
print("Project ready")

#############################################################################################
#############################################################################################

#Histogramme du nombre de taxe payé
@my_app.callback(
        Output('histogram', 'figure'),
        [Input('Year', 'value')]
    )
def update_histogram(selected_year):
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        print("Histogram")
        filtered_df = data[data['Year'] == selected_year]
        fig = px.histogram(filtered_df, x="nom_departement", y="Number_of_Taxpayers")
        print("Histogram updated")
        return fig




#### Histogramme du coût des taxes
@my_app.callback(
    Output('Cout_tax', 'figure'),
    [Input('year_selector', 'value')]
)
def update_histogram_top(selected_year):
    # Triez le DataFrame pour obtenir l'ordre décroissant des taxes payées par département
        print("histogram_top in progress")
        filtered_df = data[data['Year'] == selected_year]
        top_regions = filtered_df.sort_values(by="Average_Tax_in_Euro", ascending=False)
        fig = px.histogram(top_regions, x="nom_departement", y="Average_Tax_in_Euro", title="Coût des taxes de chaque région")
        print("histogram_top updated")
        return fig 

#### Affichage de la Carte
@my_app.callback(
        Output('map', 'figure'),
        [Input('Year', 'value')]
    )
def update_map(selected_year):
        print("map")
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        #f_data = gestion_database.get_database_commune()
        filtered_df = data[data['Year'] == selected_year]
        print(filtered_df)
        #map = conception_carte.final_map(frontiere,filtered_df)
        conception_carte.Info_map(map, frontiere, filtered_df)
        print("map_updated")
        
        return None 



#######Mise à jour de la page
@my_app.callback(Output('content', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_content(n):
    # Insérez ici le code pour mettre à jour le contenu HTML
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    return f"Contenu mis à jour à {current_time}"
my_app.server.run(debug = True)
