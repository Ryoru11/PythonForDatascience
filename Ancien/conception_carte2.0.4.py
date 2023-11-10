import  folium
import plotly.express as px
import geopandas

def create_map():
  #Creation des frontières communales
  frontiere=create_frontiere()

  #Mise au point de la résolution et du centre de la carte
  coords = (46.8398094,2.5840685)
  map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6.5)

def create_frontiere():
  frontiere = geopandas.read_file('communes.geojson')
  #frontiere = requests.get("communes.geojson")
  return frontiere



def final_map(frontiere,data):

# Initialize folium map.
    sample_map = folium.Map(location=[46.8398094, 2.5840685], zoom_start=4)
    
    print("Info map in progress")

    final_df = frontiere.merge(data, on = "code_commune")
    print("Fusion Complete")
    print (final_df)

    folium.Choropleth(
geo_data=final_df,
data=final_df,
columns=['code_commune', "Average_Tax_in_Euro"],
key_on="feature.properties.code_commune",
fill_color='YlGnBu',
fill_opacity=1,
line_opacity=0.2,
legend_name="Average_Tax_in_Euro",
smooth_factor=0,
Highlight= True,
line_color = "#0000",
name = "Average_Tax_in_Euro",
show=False,
overlay=True,
nan_fill_color = "White"
).add_to(sample_map)
    print("New model progress")
    sample_map.save(outfile='map2.html')
    return 
