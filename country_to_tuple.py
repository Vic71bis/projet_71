def country_to_tuple(countries_info, country):
    abreviations = list(countries_info.keys())
    
    i = 0
    while i < len(abreviations):
        abr = abreviations[i]
        country_abr = countries_info[abr][0]
        if country_abr == country:
            lat = countries_info[abr][2]
            long = countries_info[abr][3]
            tup = lat, long
            i = len(abreviations)
        else:
            i +=1
    return tup
    
