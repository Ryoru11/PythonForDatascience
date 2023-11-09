import dash
import dash_html_components as html
import dash_core_components as dcc
import conception_carte

my_app = dash.Dash("Projet Datascience")

my_app.layout = html.Div([
    html.H1('Project Datacience'),
    dcc.Input(
            id="input_{}".format(_),
            type=_,
            placeholder="input type {}".format(_),
        )
        for _ in ALLOWED_TYPES #A changer avec le nombre d'année unique
    
    
    #Prendre le Input et le mettre dans conception_carte.py
    html.Iframe(id = 'Map', src = 'map.html', style={"height": "1067px", "width": "100%"}),
    html.Plotlygraph
])+ [html.Div(id="out-all-types")]

@dash.callback(
    dcc.Output("out-all-types", "children"),
    [dcc.Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES])

my_app.Dash.server.run(debug = True)
