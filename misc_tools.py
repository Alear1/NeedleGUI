#August Lear
#Jan 2022

#Collection of useful tools


def strip_regex(input_string):
    #Takes a string with regex elements like \n \r and returns a clean string with those removed
    output_string = input_string

    for char in enumerate(output_string, index=0):
        if char == "\\":
            output_string = output_string


def extract_az_el_from_string(input_string):
    #Extracts target or position AZ and EL values from input string of form "AZ123.4 EL56.7"
    ind_begin = input_string.find("Z") + 1
    ind_end = input_string.find(" ")
    az = float(input_string[ind_begin:ind_end])

    input_string = input_string[ind_end+1:]
    ind_begin = input_string.find("L") + 1
    ind_end = input_string.find(" ")
    el = float(input_string[ind_begin:])

    
    return (az, el)

print(extract_az_el_from_string("AZ123.4 EL56.7"))