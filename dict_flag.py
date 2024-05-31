def dict_flag(countries_info, path):
    '''
    countries_info: dictionnary with key=abreviation, values=list of different infos about the country
    path: path to the directory in which the code is located
    
    creates a dictionary
    key = full country name
    value = path to picture of flag
    '''
    flags = {}
    for abreviation in countries_info:
        country_name = countries_info[abreviation][0]
        flag_path = path + "/" + abreviation + ".png"
        flags[country_name] = flag_path
    return flags