from pathlib import Path
import geopandas as gpd
import pandas as pd
import os

app_dir = Path(__file__).parent
merged_gdf_shapefile_path = os.path.join(app_dir, 'data', 'merged_gdf_shapefile', 'merged_gdf_shapefile.shp')

merged_gdf_shapefile = gpd.read_file(merged_gdf_shapefile_path)

merged_gdf = merged_gdf_shapefile.rename(columns={
    'certifie_1': 'certified_tot_mean',  
    'certified_': 'certified_tot',  
    'township_1': 'township_code',  
    'neighborho': 'neighborhood_code_clean', 
})

# Dynamically construct the path
app_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
fc_gdf_shapefile_path = os.path.join(app_dir, 'data', 'fc_gdf_shapefile', 'fc_gdf_shapefile.shp')

# Load the shapefile
fc_gdf_shapefile = gpd.read_file(fc_gdf_shapefile_path)

# Rename columns (adjust based on actual column names)
fc_gdf = fc_gdf_shapefile.rename(columns={
    'num_fore_1': 'num_foreclosure_in_half_mile_past_5_years_mean',  
    'num_forecl': 'num_foreclosure_in_half_mile_past_5_years',  
    'neighborho': 'neighborhood_code_clean', 
})


