#August Lear & also Kieron von Buchstab sometimes
#Jan 2022

#Collection of useful tools

from numpy import linspace,sin,cos,pi

def strip_regex(input_string):
    #Takes a string with regex elements like \n \r and returns a clean string with those removed
    output_string = input_string

    while "\\" in output_string:
        i = output_string.find("\\")
        output_string = output_string[0 : i :] + output_string[i+1 : :]
        #strObj = strObj[0 : index : ] + strObj[index + 1 : :]
    return output_string

def extract_az_el_from_string(input_string):
    #Extracts target or position AZ and EL values from input string of form "AZ123.4 EL56.7"
    ind_begin = input_string.find("Z") + 1
    ind_end = input_string.find(" ")
    az = float(input_string[ind_begin:ind_end])

    input_string = input_string[ind_end+1:]
    ind_begin = input_string.find("L") + 1
    ind_end = input_string.find(" ")
    el = float(input_string[ind_begin:])

    return [az, el]

def add_coords(coord_1, coord_2):
    # Takes a set of coordinates and returns sum of them together in az and el. 
    # ex: coord_1 = [350, 5], coord_2 = [35, -10]   | output = [25, 0]
    out_coord = [None, None]
    # try:
    #First calculate az:
    if coord_1[0] + coord_2[0] > 360:
        out_coord[0] = coord_1[0] + coord_2[0] - 360
    elif coord_1[0] + coord_2[0] < 0:
        out_coord[0] = coord_1[0] + coord_2[0] + 360
    else:
        out_coord[0] = coord_1[0] + coord_2[0]
    
    #Calculate el:
    if coord_1[1] + coord_2[1] > 90:
        out_coord[1] = 90
    elif coord_1[1] + coord_2[1] < 0:
        out_coord[1] = 0
    else:
        out_coord[1] = coord_1[1] + coord_2[1]

    return out_coord
    # except:
    #     print("ERROR: coordinates could not be added")
    #     return [0, 0]

def add_three_coords(coord_1, coord_2, coord_3):
    # Takes a set of coordinates and returns sum of them together in az and el. 
    # ex: coord_1 = [350, 5], coord_2 = [35, -10]   | output = [25, 0]
    out_coord = [None, None]
    try:
        #First calculate az:
        if (coord_1[0] + coord_2[0] + coord_3[0])  > 360:
            out_coord[0] = coord_1[0] + coord_2[0] + coord_3[0] - 360
        elif (coord_1[0] + coord_2[0] + coord_3[0]) < 0:
            out_coord[0] = coord_1[0] + coord_2[0] + coord_3[0]+ 360
        else:
            out_coord[0] = coord_1[0] + coord_2[0] + coord_3[0]
        
        #Calculate el:
        if (coord_1[1] + coord_2[1] + coord_3[1]) > 90:
            out_coord[1] = 90
        elif (coord_1[1] + coord_2[1] + coord_3[1]) < 0:
            out_coord[1] = 0
        else:
            out_coord[1] = coord_1[1] + coord_2[1] + coord_3[1]

        return out_coord
    except:
        print("ERROR: coordinates could not be added")
        return [0, 0]

def generate_ss_coords(resolution, angular_spacing):
    end = 90 #How many circles you want
    increment = 1/resolution
    spacing = 0.00362528*angular_spacing #Distance between each line

    factor = linspace(0,end*spacing,round(end/increment)); 
    az_val = 360*factor*sin(2*pi*factor/spacing) #Fun math!
    el_val = 360*factor*cos(2*pi*factor/spacing)
    coords = []

    for i in range(len(az_val)):
        coord = [az_val[i], el_val[i]]
        coords.append(coord)
        
    return coords
