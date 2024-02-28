from RN import *

def main():
    a = RN("../../output_file/gdansk/roads.shp")
    folder = 0
    while(True):
        folder = input("To select 'source_file' folder, enter 1\nTo select 'output_file' folder, enter 2\nPlease select: ")
        if(folder=="1" or folder=="2"):
            break
        else:
            print("Incorrect entry. Please try again.")
    fileName = input("Enter file name. Do not include file extention such as '.shp': ")
    if(folder=="1"):    
        a.move_points_to_road_network(["../../source_file/gdansk/"+fileName+".shp"])
    else:
        a.move_points_to_road_network(["../../output_file/gdansk/"+fileName+".shp"])

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)