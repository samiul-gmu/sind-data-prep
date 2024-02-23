# sind-data-prep

This repo has three folders: code, source_file, and output_file. All of these folders have multiple folders in them by the name of the locations, such as 'fortworth', 'gdansk', etc. The 'code' folder contains all the code files related to data preparation and cleaning grouped in the location folders. The 'source_file' folder contains all the source files (these files are provided from outside and not altered or generated by any of the codes from this repo). The 'output_file' contains files that are generated (or altered/modified) by the code files of this repo. Some of the output files are generated from source files only; others are generated from either a combination of source files and output files or output files alone. Meaning that an output file does not necessarily indicate a file that will be directly used in the simulation model. It can be a file which is used to create another output file.

Code files:
-----------
1. create_addresses_shapefiles.py

It takes addresses ('pre_addresses') shapefiles and adds the closest water towers and closest transformers of each of the households to create new address shapefiles. The names of the columns may not seem standard, but they are intentionally kept like this so that we can match the file names used in the model. Later, they can be changed (both here and in the model) to more standardized titles with complete words, all small caps, etc.

Path of the Input files:

../../source_file/gdansk/pre_addresses.shp
../../output_file/gdansk/drinking_water_moved.shp
../../output_file/gdansk/transformers_moved.shp


Path of the Generated file(s):

../../output_file/gdansk/addresses.shp

2. create_hospital_shapefiles.py

It takes hospital info in a CSV file and creates the appropriate shapefiles from it. The format of the source file can be seen here: source_file/gdansk/hospitals.csv

Path of the Input files:

../../source_file/gdansk/hospitals.csv


Path of the Generated file(s):

../../output_file/gdansk/hospitals.shp

3. move_resources_on_the_road_network.py and RN.py

'RN' is a helper file invoked when we call the 'move_resources_on_the_road_network' file. This file sets the road shapefiles first and then moves the contents of other files (based on the folder selection you make and the file name you provide) on the road network and generates a corresponding new file. For example, if we want to move households on the road network, we need both roads and household shapefiles. This code will move each household to the appropriate position on the road network and save that as a new file. The same code can be repurposed to move anything on the road network with valid latitude and longitude. It will append '_moved' at the end of the initial file name while saving the newly generated one.

Path of the Input files:

../../source_file/gdansk/roads.shp
../../[SELECTED FOLDER]/gdansk/[FILE NAME].shp


Path of the Generated file(s):

../../output_file/gdansk/[FILE NAME]_moved.shp

