# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:21:23 2023

@author: Sami
"""

# importing libraries
import pandas as pd # Reading csv file 
from shapely.geometry import Point # Shapely for converting latitude/longtitude to geometry
import geopandas as gpd # To create GeodataFrame
import numpy as np # To check if lat-long is nan


def hospital_shapefiles_generator():
    hospitals = pd.read_csv('../../source_file/gdansk/hospitals.csv', encoding='latin-1')

    # creating unique id
    hospitals_id = ["hospital"+str(s) for s in list(hospitals.index)]
    hospitals['uid']=hospitals_id
    hospitals['# Beds'] = hospitals['# Beds'].fillna(0).astype(int)
    print(hospitals['# Beds'])
    
    # creating a geometry column 
    geometry = [Point(xy) for xy in zip(hospitals['Longitude'], hospitals['Latitude'])]
    
    # Coordinate reference system : WGS84
    crs = {'init': 'epsg:4326'}
    
    # Creating a Geographic data frame 
    gdf_hospitals = gpd.GeoDataFrame(hospitals, crs=crs, geometry=geometry)
    
    # dropping rows for invalid lat-long
    gdf_hospitals = gdf_hospitals[~np.isnan(gdf_hospitals.Longitude)]
    gdf_hospitals = gdf_hospitals[~np.isnan(gdf_hospitals.Latitude)]
    
    gdf_hospitals = gdf_hospitals.rename(columns={"Hospitals_Medical facilities in Gdansk": "name", "Address": "address", 
                                                  "# Beds": "bed", "Latitude": "lat", "Longitude": "lng"})
    
    gdf_hospitals = gdf_hospitals[["uid", "name", "address", "bed", "lat", "lng", "geometry"]]
    
    print(gdf_hospitals.columns)
    
    gdf_hospitals = gdf_hospitals[gdf_hospitals["bed"] > 0]
    
    print(gdf_hospitals)
    
    gdf_hospitals.to_file('../../output_file/gdansk/hospitals.shp')


hospital_shapefiles_generator()