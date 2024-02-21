# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 07:09:41 2023

@author: Sami
"""
import geopandas as gpd
from shapely.geometry import LineString
import pandas as pd
import random

# Unpacking Gdansk roads file linestrings
# The original file's linestrings had multiple points; so each of them represents a road with multiple points
# I am unpacking that in a way so that each of the pairs will have a separate entry

gdf = gpd.read_file("../../source_file/gdansk/GdanskSimplifiedHighResEdges.shp")

edges = []
for i in range(0, len(gdf)):
    points = list(gdf["geometry"][i].coords)
    #print(points)
    for j in range(1, len(points)):
        line = LineString(points)
        edges.append(line)
    print(i)

random.shuffle(edges)

index_for_df = range(0, len(edges))
network_edges = pd.DataFrame(edges, columns=['geometry'], index= index_for_df)
fid = index_for_df
network_edges["FID"] = fid
network_edges = network_edges[["FID","geometry"]]
    
network_edges = gpd.GeoDataFrame(network_edges, geometry="geometry")
network_edges.crs = 'EPSG:4326'
print(network_edges)

#network_edges.to_file('../../source_file/gdansk/roads_temp.shp')