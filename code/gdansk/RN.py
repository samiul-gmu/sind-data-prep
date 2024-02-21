from warnings import simplefilter
import geopandas as gp
from shapely.wkt import loads,dumps
import shapely
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points
import numpy as np
import pandas as pd
import os
 

class RN:
    def __init__(self,Path_to_road_network_file):
    #    self,Path_to_road_network_file:str =None, Path_to_addresses_shapefile:str = None
        # Path_to_road_network_file, Path_to_addresses_shapefile= r"src\main\resources\fortworth\DallasFtWorthSimplifiedHighResEdges.shp",r"src\main\resources\fortworth\landscan_population_numbers_centroids.shp"
        if  Path_to_road_network_file !=None:
             self.road_network = gp.read_file(Path_to_road_network_file)
        # else:
        #     print("Warning you did not specify a road network you will need to specify one to apply methods part of this class")
        # if Path_to_addresses_shapefile !=None:
        #      self.addresses = gp.read_file(Path_to_addresses_shapefile)
    from shapely.ops import nearest_points
    def move_points_to_road_network(self, Paths_to_addresses_shapefile, outputfile=True):
        self.points = Paths_to_addresses_shapefile
        if not isinstance(Paths_to_addresses_shapefile,str) and not isinstance(Paths_to_addresses_shapefile,list):
            raise ValueError("you must pass a string or an address str")
        stats = {}
        # points.geometry =[loads(dumps(geom, rounding_precision=10)) for geom in points.geometry]
        
        for percentage in range(1,2):
            print(percentage/4) # Not sure what percentage means and why we are printing this
            # self.increase_nodes(interval = (percentage/4))
            # print(self.road_network.head)
            new_lines = [] # This empty list remains unused
            stats[percentage/4] = [] # Entering an empty list to a dictionary with a key of 0.25
            print(stats) # Printing out the dictionary to see if it has something useful
            # stats['old_methods'] = []
            # self.road_network.geometry
            roads = self.road_network.unary_union # It creates a multistring containing all the linestring of road network
            roads = [Point(m) for i in self.road_network.geometry for m in i.coords] 
            # +[list(gp.read_file(x).geometry) for x in self.points]
            roads = pd.DataFrame(roads)
            roads = gp.GeoDataFrame(geometry = roads[0],crs = 'EPSG:4326')

            roads = roads.unary_union 
            
            for x in self.points:
                print(x)
                points = gp.read_file(x)
                print(points.keys())
                new_points =[]
                shortest_lines = {}
                # if x == self.points[0]:
                #     new_road_network =points
                # else:

                # shortest = lines['geometry'][0].distance(points ['geometry'][0])
                driveways = []
            
                for ind,i in enumerate( points ['geometry']):
                    # shortest_lines = {}
                    p2 =  nearest_points(i, roads)[1]
                    # shortest = i.distance(p2)
                    # print(i,p2,shortest)
                    # old_method = lines['geometry'][0].interpolate(lines['geometry'][0].project(i))
                    # old_shortest = i.distance(old_method)
                    new_points.append(p2)
                    closest_point = p2
                    
                    
                        
                    shortest = i.distance(roads)
                    # closest_point = [ind,p2]
                        # old_method = m.interpolate(m.project(i))
                        # old_shortest = i.distance(old_method)
                    stats[percentage/4].append(shortest)
                    # stats['old_methods'].append(old_shortest)
                            
                            
                points ['geometry']= pd.DataFrame(new_points)[0]
                points.to_file("../../output_file/gdansk/"+(x.split(".shp")[0]).split("/")[-1]+"_moved.shp")

'''           
        # for statistic in stats.keys():
        #     print(statistic,np.mean(stats[statistic]),np.std(stats[statistic]),np.max(stats[statistic])) 
    def increase_nodes(self,Path_to_road_network_file =False,interval = 0.001,outputfile = True):
        #A methods to increase the number of nodes on a Linestring (road segments)
        #for simulation purposes (higher sensitivety to destruction)
            
        
        lines = []
        distance = 0 ## starting at length 0
        self.add_distance =  interval ## eg interpoalte every 4 meter
        for i in self.road_network['geometry']:
            points = []
            while distance < 1:
                
                points.append(i.interpolate(distance,normalized = True))

                distance += self.add_distance ## add more
            distance = 0
            
            list_of_points = [Point(x) for x in points]

            line = LineString(list_of_points)
            lines.append(line)
        df = pd.DataFrame(lines)
        self.road_network['geometry']= df[0]
        # if outputfile:
            # self.road_network.to_file(r"roads_higher_resolution {} .shp".format(interval))
    def simplify(self):
        self.road_network.geometry = self.road_network.simplify(0.05,True)
        self.road_network.geometry =[loads(dumps(geom, rounding_precision=10))  for geom in self.road_network.geometry]
        self.road_network.to_file("simplified.shp",crs = 'EPSG:4326')
        self.input_road_network("simplified.shp")
    def create_driveways(self, Paths_to_addresses_shapefile,outputfile = True):
        self.points = Paths_to_addresses_shapefile
        if not isinstance(Paths_to_addresses_shapefile,str) and not isinstance(Paths_to_addresses_shapefile,list):
            raise ValueError("you must pass a string or an address str")
        
        lines = self.road_network
        new_lines = []
        for i in self.points:
            if isinstance(Paths_to_addresses_shapefile,str):
                i = self.points
            points = gp.read_file(i)
            points.geometry =[loads(dumps(geom, rounding_precision=40)) for geom in points.geometry]
            shortest_lines = {}

            shortest = lines['geometry'][0].distance(points ['geometry'][0])
            driveways = []
            for i in points ['geometry']:
                # shortest_lines = {}
                shortest = lines['geometry'][0].distance(i)
                for m in lines ['geometry'][1:]:
            
                        
                    if shortest > m.distance(i):
                        p2 = m.interpolate(m.project(i))
                        shortest = m.distance(i)
                        shortest_line = [p2,i]
                        

                driveways.append(shortest_line)
            
            for m in driveways:
                new_lines.append(LineString(m))
                
                    
        df = pd.DataFrame(new_lines)

        gpd = gp.GeoDataFrame(geometry = df[0],crs = 'EPSG:4326')
        self.driveways = gpd
        
        if outputfile:
            gpd.to_file(r"src\main\resources\fortworth\driveways.shp")
    
    def input_road_network(self,new_road_network):
        self.road_network = gp.read_file(new_road_network)
                


        
    def connect_components(self,outputfile = True):#works! adds driveways to grid
        lines = self.road_network
      
        points = self.driveways 

        df =[i for i in lines.geometry]+ [i for i in points.geometry]
        df = pd.DataFrame(df)
        new_lines = gp.GeoDataFrame(geometry = df[0],crs = 'EPSG:4326')
        new_lines.geometry = [loads(dumps(geom, rounding_precision=10)) for geom in new_lines.geometry]
        lines_dissolved = new_lines.unary_union
        x = [i for i in lines_dissolved]
        
        df = pd.DataFrame(x)

        gpd = gp.GeoDataFrame(geometry = df[0],crs = 'EPSG:4326')
        self.road_network = gpd
        if outputfile:
            gpd.to_file(r"src\main\resources\fortworth\driveways_with_road_network_completed.shp")
    
    # def snap_points(self,point_layer):
    #     self.snapped_network = []
    #     roads = self.road_network.geometry.unary_union
    #     for i in point_layer.geometry:
    #             if not i.touches(roads):
    #                 self.snapped_network.append(shapely.ops.snap(i,roads, 0.00001))
    #     df = pd.DataFrame(self.snapped_network)
    #     gpd = gp.GeoDataFrame(geometry = df[0],crs = 'EPSG:4326')
    #     gpd.to_file(r"src\main\resources\fortworth\test.shp")

    # def snap_points_parallel(self,args):
    #     num_section = args[0]
    #     job_section = args[1]
    #     lines = self.road_network
    #     # lines = 
    #     points = self.road_network
    #     points2 = np.array_split(points ,num_section)[job_section - 1]
    #     self.snapped_network = []
    #     for i in self.driveways.geometry:
    #         for m in self.road_network.geometry:
    #             self.snapped_network.append(shapely.ops.snap(i,m, 0.00001))
    #     df = pd.DataFrame(self.snapped_network)
    #     gpd = gp.GeoDataFrame(geometry = df[0],crs = 'EPSG:4326')
       
    #     gpd.to_file(r"src\main\resources\fortworth\test.shp")

    def __find_line__(self,args):
        import geopandas as gp
        from shapely.ops import nearest_points,snap
        import numpy as np
    
        num_section = args[0]
        job_section = args[1]
        lines = self.driveways        # lines = 
        points = self.road_network

        points2 = np.array_split(points ,num_section)[job_section - 1]

        shortest_lines = {}

     
        driveways = []
        res = points
        lines2_union = lines.geometry.unary_union
        res.geometry = points.geometry.apply(lambda x: snap(x, lines2_union, 1))
        return res
'''
        
