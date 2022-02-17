#August Lear
#Jan 2022

#Collection of useful tools


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

    return (az, el)