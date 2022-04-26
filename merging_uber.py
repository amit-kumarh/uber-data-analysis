import pandas as pd
import numpy as np
import geopandas as gpd

files = ['apr14', 'may14', 'jun14']

df = pd.DataFrame()
for f in files:
    path = f'uber_data/uber-raw-data-{f}.csv'
    toadd = pd.read_csv(path)
    df = pd.concat([df, toadd])

df.reset_index(inplace=True, drop=True)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Lon, df.Lat))
gdf.set_crs(epsg=4326, inplace=True)
gdf.to_feather('apr-june_2014.feather')

df15 = pd.read_csv('uber_data/uber-raw-data-janjune-15.csv')
df15['ts'] = pd.to_datetime(df15['Pickup_date'], infer_datetime_format=True, errors='coerce')
df15['month'] = df15['ts'].dt.month
subset = df15[df15['month'] >= 4].reset_index(drop=True)
subset.to_feather('apr-june_2015.feather')
