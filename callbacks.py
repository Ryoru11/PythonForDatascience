from dash.dependencies import Input, Output
import plotly.express as px
from utils import load_data

df = load_data()

def register_callbacks(app):
    @app.callback(
        Output('histogram', 'figure'),
        [Input('year_selector', 'value')]  # ajoutez des dépendances d'entrée si nécessaire
    )
    def update_histogram(selected_year):
        # Créer un histogramme (exemple basé sur le nombre de contribuables par région)
        filtered_df = df[df['Year'] == selected_year]
        fig = px.histogram(filtered_df, x="Department", y="Number_of_Taxpayers")
        return fig

    @app.callback(
        Output('map-view', 'figure'),
        [Input('year_selector', 'value')]  # ajoutez des dépendances d'entrée si nécessaire
    )
    def update_map(selected_year):
        # Créez une visualisation géographique (exemple basique ici)
        filtered_df = df[df['Year'] == selected_year]
        fig = px.scatter_geo(filtered_df, lat='lat_column', lon='lon_column', text='City')  # vous aurez besoin des colonnes latitude et longitude
        return fig
    
    @app.callback(
    Output('histogram-top-regions', 'figure'),
    [Input('year_selector', 'value')]
)
    def update_histogram_top(selected_year):
    # Triez le DataFrame pour obtenir les 15 régions qui paient le plus d'impôts
        filtered_df = df[df['Year'] == selected_year]
        top_regions = filtered_df.sort_values(by="Average_Tax_in_Euro", ascending=False).head(15)
        fig = px.bar(top_regions, x="Department", y="Average_Tax_in_Euro", title="Top 15 départements payant le plus d'impôt")
        return fig 

    @app.callback(
    Output('histogram-bottom-regions', 'figure'),
    [Input('year_selector', 'value')]
)
    def update_histogram_bottom(selected_year):
        # Triez le DataFrame pour obtenir les 15 régions qui paient le moins d'impôts
        filtered_df = df[df['Year'] == selected_year]
        bottom_regions = filtered_df.sort_values(by="Average_Tax_in_Euro", ascending=True).head(15)
        fig = px.bar(bottom_regions, x="Department", y="Average_Tax_in_Euro", title="15 départements payant le moins d'impôt")
        return fig
