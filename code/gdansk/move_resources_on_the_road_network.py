from RN import *
#import winsound


#use the RN class to move points on a map addresses to the closest node on the road network.

def main():
 
    import geopandas as gp
    import pandas as pd
    import numpy as np
    from shapely.geometry import LineString, Point


    outputs = []
    folder_path = "../../source_file/gdansk/"
    a = RN(folder_path+"roads.shp") # read the simplified road network (use qgis to simplify the network for now) #?
    
    #a.move_points_to_road_network([folder_path+"transformers.shp",folder_path+"power_switches.shp",folder_path+"power_plants.shp",
    #                               folder_path+"water_pumps.shp",folder_path+"industrial.shp",folder_path+"gas_stations.shp",folder_path+"switch_yards.shp",folder_path+"households.shp"])
    
    #a.move_points_to_road_network([folder_path+"drinking_water.shp"])
    
    #a.move_points_to_road_network(["../../output_file/gdansk/"+"hospitals.shp"])
    
    #a.move_points_to_road_network(["../../output_file/gdansk/"+"addresses.shp"])
    
    a.move_points_to_road_network(["../../output_file/gdansk/"+"grocery_stores_with_warehouse_attr.shp"]) #MANUALLY RENAME
    
    a.move_points_to_road_network(["../../output_file/gdansk/"+"food_warehouses_with_warehouse_attr.shp"]) #MANUALLY RENAME
    
    a.move_points_to_road_network(["../../output_file/gdansk/"+"fuel_depots.shp"])
    
    #,"water_towers.shp",r"transformers_complete_reprojected.shp",r"boundedReprojected — Natural gas.shp",r"water_pumps.shp"]) # read in address files (with a geometry type of  gpd.read_file("Gdansk_Gas_stations.shp") ?

    

if __name__ == '__main__':
    try:
        main()
       #winsound.Beep(440, 1000) #make a sound when the program is done
    except Exception as e:
        print(e)
        #winsound.Beep(440, 1000) #make a sound when the program fails and is done

#%%