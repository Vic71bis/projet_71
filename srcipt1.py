# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:02:04 2024

@author: Utilisateur
"""
def csv_to_dict(csv_file):
    '''
    Parameters
    ----------
    csv_file : csv file

    Returns a dictionnary having the elements of the first column as a key, and the elements of the following columns as the value in the form of a list:
    data
    '''
    with open(csv_file, newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        data = {}
        for country_code, country, altitude, capital, lat, long in reader:
            if country_code not in data:
                data[country_code] = {}
                data[country_code]["name"] = country
                data[country_code]["capital"] = capital
                data[country_code]["latitude"] = lat
                data[country_code]["longitude"] = long
    return data


def convert_in_latN_and_longE(worldcountries):
    ''' 
    parameters: 
        worldcountries (dictionary with country information)

    returns:
        modified dictionary with latitude in N and longitude in E
    ''' 
    for country in worldcountries.keys():
        lat = worldcountries[country]["latitude"] 
        long = worldcountries[country]["longitude"]
        
        # Convertir la latitude de S à N
        if 'S' in lat:
            lat = -float(lat[:-1])  # Supprimer le caractère 'S' et changer le signe
        
        # Convertir la longitude de W à E
        if 'W' in long:
            long = -float(long[:-1])  # Supprimer le caractère 'W' et changer le signe

        # Supprimer 'N' de la latitude
        if 'N' in lat:
            lat = float(lat[:-1])  # Supprimer le caractère 'N' 

        # Supprimer 'E' de la longitude
        if 'E' in long:
            long = float(long[:-1])  # Supprimer le caractère 'E'

        # Mettre à jour les valeurs dans le dictionnaire
        worldcountries[country]["latitude"] = lat
        worldcountries[country]["longitude"] = long

    return worldcountries

#######################################################################"
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m/60 + s/3600
 
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd-d)*60
    m = int(x)
    s = (x-m)*60
    return d, m, s

def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd/180*pi
 
def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd/pi*180

def distance_capital(capital1, capital2, worldcountries):
    # Extract latitude and longitude coordinates of capital cities
    latA, longA = worldcountries[capital1]["latitude"], worldcountries[capital1]["longitude"]
    latB, longB = worldcountries[capital2]["latitude"], worldcountries[capital2]["longitude"]
    
    # Convert coordinates
    latA_dd = dms2dd(*latA)
    longA_dd = dms2dd(*longA)
    latB_dd = dms2dd(*latB)
    longB_dd = dms2dd(*longB)
    
    # Convert coordinates from DD to radians
    latA_rad = deg2rad(latA_dd)
    longA_rad = deg2rad(longA_dd)
    latB_rad = deg2rad(latB_dd)
    longB_rad = deg2rad(longB_dd)
    
    # Calculate distance between the two cities
    dist = distanceGPS(latA_rad, longA_rad, latB_rad, longB_rad)
    
    return dist
########################################################################################

def time_transport(distance, dict_transport):
    '''
    Parameters
    ----------
    distance : integer
        Distance between two capitals (in kms)
    
    dict_transport : dictionnary
        key: mean of transport
        value: their speed
        
    Returns a dictionnary having the mean of transport as key, and the corresponding to the time necessary to travel the distance indicated as the value
    '''
    dist = int(distance)
    travel_time = {}
    for transport, speed in dict_transport.items() : 
        travel_time[transport] = dist / speed

    return travel_time

def dict_transport_from_csv (csv_file):
     with open(csv_file, newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        dict_transport = {}
        for transport, speed in reader:
            dict_transport[transport] = speed
        return dict_transport

  
print("projet")
