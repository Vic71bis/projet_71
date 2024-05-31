# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:06:15 2024

@author: diane
"""

import json
import csv
import math
from geopy.distance import geodesic

####################################################### INITIALIZING ALL THE CSV FILES NEEDED
def transport_csv_to_dict(csv_file):
    '''
    Parameters
    ----------
    csv_file : csv file

    Returns a dictionnary having the elements of the first column as a key, and the elements of the following columns as the value in the form of a list:
    data
    '''
    eliminer_entete = True
    with open('csv_file', newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        data = {}
        if eliminer_entete:
            reader.__next__()
        for row in reader:
            transport, speed = row
            if transport not in data:
                data[transport] = speed
    return data

def country_csv_to_dict (csv_file):
    eliminer_entete = True
    with open(csv_file, newline = "") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        data = {}
        if eliminer_entete:
            reader.__next__()
        for row in reader:
            country_abreviation, country, capital, lat, long, pop, yearly_change, net_change, density, land_area, migrants, fertility_rate, median_age, urban_pop, world_share = row
            data[country_abreviation] = [country, capital, lat, long, pop, yearly_change, net_change, density, land_area, migrants, fertility_rate, median_age, urban_pop, world_share]
    return data


def open_json_file (json_file) :
    with open(json_file, 'r') as file:
        new_file = json.load(file)
    return new_file


all_countries=open_json_file('country_neighbours.json')
worldcountries=country_csv_to_dict('countries_info.csv')       
dict_transport = transport_csv_to_dict('transport_speed.csv')

##############################################################################
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

#######################################################################" GET DISTANCE BETWEEN THE TWO CITIES
def distance_capital(capital1, capital2, worldcountries):
    # Extract latitude and longitude coordinates of capital cities
    latA, longA = worldcountries[capital1]["latitude"], worldcountries[capital1]["longitude"]
    latB, longB = worldcountries[capital2]["latitude"], worldcountries[capital2]["longitude"]

    city_A_coordinates= (latA,longA)
    city_B_coordinates =(latB,longB)
    # Calculate distance between the two cities
    dist = geodesic(city_A_coordinates, city_B_coordinates).kilometers
    
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

########################################################## GRAPH TRAVERSAL #######################################################################

def create_bfs (start, all_countries):
    """
    Parameters
    ----------
    start : string (pays de depart)
        
    all_countries: dico avec neighbours
    

    Returns : dico_prec (tree des pays qu'on peut atteindre à partir du start)
    
    """
    a_traiter = [start]
    dico_prec = {}
    dico_prec[start] = None
    treated = []
    
    while len(a_traiter) > 0:
        s = a_traiter.pop(0)
        treated.append(s)
        if s in all_countries:
            for si in all_countries[s]:
                if si != []:
                    s_abrev = si[1]
                    if s_abrev not in treated and s_abrev not in a_traiter:
                        a_traiter.append(s_abrev)
                        dico_prec[s_abrev] = s
                    
    return dico_prec

def is_reachable_by_car (start, end, all_countries):
    ans = 10
    tree = create_bfs(start, all_countries)
    if end in tree:
        ans = True
    else:
        ans = False
    return ans, tree
    
def shortest_path(v, parents):
    path = []
    while v is not None:
        path.append(v)
        v = parents[v]
    return path[::-1]

        
def get_path_btw_countries (start, end, all_countries):
    reachable, tree = is_reachable_by_car(start, end, all_countries)
    if reachable:
        path = shortest_path(end, tree)
        return path
    else:
        return False
    
def reachable_countries(user_capital, user_time, world_countries, dict_transport):
    '''
    Select the countries where it’s possible to go 

    Parameters
    ----------
    user_capital : string
        String that corresponds to the actual location of the user.
    user_time : int
        Integer that represents the time the user has to travel.
    world_countries : dictionary
        Dictionary with countries as keys and their associated values (including coordinates)
    dict_transport : dictionary
        Dictionary with the mean of transport as key and their speed as value
        
    Returns
    -------
    possible_countries : list
        List grouping every country that can be reach from the user position. 

    '''
    possible_countries = []
    for country in world_countries:
        dist = distance_capital(user_capital, country, world_countries)
        travel_time = time_transport(dist, dict_transport)
        if travel_time <= user_time: # A demander aux filles car travel_time = dictionnaire et user_time juste une valeur
            possible_countries.append(country)
    return possible_countries
        
'''def dist_according_to_transport(dict_transport,user_time):
    if self.transport_air.get()== 1 :
        max_distance_to_travel = dict_transport['car']*user_time
    if self.transport_earth.get()==1 :
        max_distance_to_travel = dict_transport['plane']*user_time
    return max_distance_to_travel'''

def display_info_countries(self,world_countries) :
    if '''clic droit souris sur un pays de la carte tkinter :
        récupérer les coordonnés gps du pays sur lequel on a cliqué 
        transférer coordonnées gps en un pays
        récupérer les infos du pays dans le dictionnaire : world_countries
        frame du côté défini dans map_window.insert (toutes les infos du pays)
        
    if 