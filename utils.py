import pandas as pd
import os

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