# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:23:46 2023

@author: Sami
"""

import geopandas as gpd
import math

road = gpd.read_file("../../source_file/gdansk/pre_addresses.shp")

drinking_water = gpd.read_file("../../output_file/gdansk/drinking_water_moved.shp")
drinking_water_loc = list(drinking_water.geometry)

transformers = gpd.read_file("../../output_file/gdansk/transformers_moved.shp")
transformers_loc = list(transformers.geometry)


def helper(point, points):
    minDist = math.hypot(point.x-points[0].x, point.y-points[0].y)
    minDistIdx = 0
    for i in range(1, len(points)):
        dist = math.hypot(point.x-points[i].x, point.y-points[i].y)
        if (dist<minDist):
            minDist = dist
            minDistIdx = i
    return minDistIdx

closest_drinking_waters = []
closest_transformers = []

check_i = 0

for i in road.geometry:
    closest_drinking_water = helper(i, drinking_water_loc)
    closest_transformer = helper(i, transformers_loc)
    closest_drinking_waters.append(drinking_water.full_id[closest_drinking_water])
    closest_transformers.append(transformers.full_id[closest_transformer])
    if(check_i%500==0):
        print(check_i, "of", len(road.geometry), "completed.")
    check_i=check_i+1

road['water_towe'] = closest_drinking_waters
road['transforme'] = closest_transformers

road.rename(columns = {'households':'Households'}, inplace = True)

road = road[['VALUE', 'Households', 'water_towe', 'transforme', 'geometry']]

print(road)

road.to_file('../../output_file/gdansk/addresses.shp')