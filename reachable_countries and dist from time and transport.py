# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:29:56 2024

@author: ifyes
"""
def get_dist_from_time_and_transport (time_hours):
    if self.choice_air.get() == 1:
        speed = 800
    if  self.choice_earth.get() == 1:
        speed = 95
    distance = speed*float(time_hours)
    return distance


def reachable_countries (user_country_abrev, distance, world_countries):
    possible_countries = []
    for country in world_countries:
        if distance <= distance_capital(country, user_country_abrev, world_countries):
            possible_countries.append(country)
    return possible_countries
    
