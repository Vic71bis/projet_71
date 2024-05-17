#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:10:09 2024

@author: drombaut
"""

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
        if travel_time <= user_time:
            possible_countries.append(country)
    return possible_countries
        

    