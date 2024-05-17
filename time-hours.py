# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:04:17 2024

@author: ifyes
"""

def convert_time (hours, minutes):
    """
    Parameters
    ----------
    hours : string

    minutes : string


    Returns
    -------
    time in hours

    """
    h = int(hours)
    m = int(minutes)/60
    tot_time = h + m
    
    return tot_time
    