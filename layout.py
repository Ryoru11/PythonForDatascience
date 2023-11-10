from dash import dcc
from dash import html

def get_layout():
    layout = html.Div([
         dcc.Dropdown(
        id='year_selector',
        options=[{'label': str(i), 'value': i} for i in range(2019, 2022)],
        value=2019  # valeur initiale
    ),
        dcc.Graph(id='histogram'),
        dcc.Graph(id='histogram-bottom-regions',),
        dcc.Input(id='some-input', value='Initial Value', type='text'),
        dcc.Graph(id='histogram-top-regions',),
        # Ajoutez ici d'autres composants comme des sélecteurs de date ou de région.
    ])
    return layout
