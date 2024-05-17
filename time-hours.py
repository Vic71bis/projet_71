# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:04:17 2024

@author: ifyes
"""

def convert_time_hours (hours, minutes):
    
    h = int(hours)
    m = int(minutes)/60
    tot_time = h + m
    
    return tot_time  # tot time in hours



def convert_time_h_min (hours):
    
    entire_hours = int(hours)
    min_in_hours = entire_hours - hours
    minutes = min_in_hours/60
    
    return entire_hours, minutes 
    
    
