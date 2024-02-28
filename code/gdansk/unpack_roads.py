# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 07:09:41 2023

@author: Sami
"""
import geopandas as gpd
from shapely.geometry import LineString
import pandas as pd

# Unpacking Gdansk roads file linestrings
# The original file's linestrings had multiple points; so each of them represents a road with multiple points
# I am unpacking that in a way so that each of the consecutive pairs will have a separate entry

# The source file ('GdanskSimplifiedHighResEdges.shp') should have an ID column ('_FID') and a 'geometry' column
# The name of the id column will be changed to 'FID'; the 'geometry' column's name will remain same.

gdf = gpd.read_file("../../source_file/gdansk/SimplifiedHighResEdges.shp")

fids = []
edges = []
for i in range(0, len(gdf)):
    points = list(gdf["geometry"][i].coords)
    for j in range(1, len(points)):
        line = LineString(points)
        edges.append(line)
        fids.append(gdf["_FID"][i])

index_for_df = range(0, len(edges))
network_edges = pd.DataFrame(edges, columns=['geometry'], index= index_for_df)
fid = index_for_df
network_edges["FID"] = fids
network_edges = network_edges[["FID","geometry"]]
    
network_edges = gpd.GeoDataFrame(network_edges, geometry="geometry")
network_edges.crs = 'EPSG:4326'
print(network_edges)

network_edges.to_file('../../output_file/gdansk/roads.shp')