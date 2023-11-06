from dash import Dash
import dash_html_components as html
import dash_core_components as dcc


my_app = Dash("Projet Datascience")

my_app.layout = html.div([
    html.h1('Project Datacience'),
    html.TextInput(label ='Year', value ='2019', id = 'my-input'),
    html.Plotlygraph
])

my_app.server.run(debug = True)