import geopandas as gp
from shapely.geometry import Point
from shapely.ops import nearest_points
import pandas as pd
 

class RN:
    def __init__(self,Path_to_road_network_file):
        if  Path_to_road_network_file !=None:
             self.road_network = gp.read_file(Path_to_road_network_file)

    from shapely.ops import nearest_points
    def move_points_to_road_network(self, Paths_to_addresses_shapefile, outputfile=True):
        self.points = Paths_to_addresses_shapefile
        if not isinstance(Paths_to_addresses_shapefile,str) and not isinstance(Paths_to_addresses_shapefile,list):
            raise ValueError("you must pass a string or an address str")
        stats = {}
        
        for percentage in range(1,2):
            print(percentage/4)
            stats[percentage/4] = []
            print(stats)
            print ("Please wait for the code to end. It may take a while...")
            roads = self.road_network.unary_union
            roads = [Point(m) for i in self.road_network.geometry for m in i.coords] 
            roads = pd.DataFrame(roads)
            roads = gp.GeoDataFrame(geometry = roads[0],crs = 'EPSG:4326')

            roads = roads.unary_union 
            
            for x in self.points:
                print(x)
                points = gp.read_file(x)
                print(points.keys())
                new_points =[]
            
                for ind,i in enumerate( points ['geometry']):
                    p2 =  nearest_points(i, roads)[1]
                    new_points.append(p2)
                       
                    shortest = i.distance(roads)
                    stats[percentage/4].append(shortest)                            
                            
                points ['geometry']= pd.DataFrame(new_points)[0]
                points.to_file("../../output_file/gdansk/"+(x.split(".shp")[0]).split("/")[-1]+"_moved.shp")