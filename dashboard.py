import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_leaflet as dl
import plotly.express as px
import conception_carte
import gestion_database

my_app = dash.Dash("Projet Datascience")
print("App created")
data = gestion_database.get_database_commune()
print("Data downloaded")
map  = conception_carte.create_map()
frontiere = conception_carte.create_frontiere()
#with open('map.html', 'r') as file:
#    map_html_content = file.read()
print("Map Downloaded")
my_app.layout = html.Div([
    html.H1('Project Datacience'),
    dcc.Dropdown(
            id="Year",
            options= [{'label': str(year), 'value': year} for year in data['Year'].unique()],
            value = data['Year'].max()
        ),
    dcc.Dropdown(
            id="nom_departement",
            options= [{'label': str(departement), 'value': departement} for departement in data['Department'].unique()],
            value = data['Department'].max()
        ),    
    dcc.Graph(id='histogram'),
    
    #dcc.Graph(id = 'map'),
    
    html.Iframe(id="map", srcDoc=open("./map.html", 'r').read())
    #html.Iframe(id="map", srcDoc=open("map.html").read())    
    #html.Div([
    #    dcc.Markdown(children=map_html_content)])
    
    #Prendre le Input et le mettre dans conception_carte.py
    
            
    
])
print("Project ready")



@my_app.callback(
        Output('histogram', 'figure'),
        [Input('Year', 'value')]
    )
def update_histogram(selected_year):
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        print("Histogram")
        filtered_df = data[data['Year'] == selected_year]
        fig = px.histogram(filtered_df, x="Department", y="Number_of_Taxpayers")
        print("Histogram updated")
        return fig

@my_app.callback(
        Output('map', 'figure'),
        [Input('Year', 'value')]
    )
def update_map(selected_year):
        print("map")
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        #f_data = gestion_database.get_database_commune()
        filtered_df = data[data['Year'] == selected_year]
        #map = conception_carte.final_map(filtered_df)
        conception_carte.Info_map(map, frontiere, filtered_df)
        print("map_updated")
        return None 

my_app.server.run(debug = True)
