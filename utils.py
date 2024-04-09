import pandas as pd
import geopandas as gpd
import shapely
from shapely import Point, Polygon
from shapely import wkt
import os

def extract_centroids_from_geodata(geodata_path: str) -> list[Point]:
    geodata_df = pd.read_csv(geodata_path, delimiter=";")
    geodata_df.drop(columns=['ID','OBJETO', 'COMUNAS', 'PERIMETRO', 'AREA'], inplace=True)
    geodata_df['WKT'] = geodata_df['WKT'].apply(wkt.loads)
    geodata_gdf = gpd.GeoDataFrame(data=geodata_df, geometry=geodata_df['WKT']).drop(columns=['WKT'])

    centroids = []
    
    for polygon in geodata_gdf['geometry']:
        centroid = polygon.centroid
        latitude, longitude = centroid.y, centroid.x

        # Rounding values (Google Maps format)
        latitude = round(latitude, 7)
        longitude = round(longitude, 7)

        centroids.append((latitude, longitude))

    return centroids

def create_dataframe(names: list, addresses: list, numbers: list, websites: list, ratings: list, geocoders:list) -> pd.DataFrame:
    return pd.DataFrame(data={
        "names": names, 
        "addresses": addresses,
        "numbers": numbers,
        "websites": websites,
        "ratings": ratings,
        "geocoders": geocoders
        })

def export_data(dataframe: pd.DataFrame):
    current_directory = os.getcwd()

    export_data_directory = os.path.join(current_directory, r'./export_data')
    
    if not os.path.exists(export_data_directory):
        os.makedirs(export_data_directory)

    dataframe.to_csv(f"{export_data_directory}/data.csv", encoding='utf-8')
    dataframe.to_excel(f"{export_data_directory}/data.xlsx")