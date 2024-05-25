# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:50:37 2024

@author: ifyes
"""
import json
with open(country_neighbours.json, 'r') as file:
    all_countries = json.load(file)

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

# Get the path from FI to FR
path = get_path_btw_countries("FI", "FR", all_countries)
print("Path from FI to FR :", path)
