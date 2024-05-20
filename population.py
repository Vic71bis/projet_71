# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:04:17 2024

@author: ifyes
"""
import csv

# Initialize an empty list to hold the rows as dictionaries
pop_data_list = []

# Open the CSV file for reading
with open('population_by_country_2020.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for row in csv_reader:
        # Append the row to the list
        pop_data_list.append(row)


# Initialize an empty list to hold the rows as dictionaries
coun_data = []

# Open the CSV file for reading
with open('countries_capitals.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for row in csv_reader:
        #print(row)
        
        for i, data in row.items():
            #print(data)
        
        # Append the row to the list
            coun_data.append(data)
            
            if i not in coun_data :
                coun_data.append(i)

def add_pop_area_to_data (pop_data_list, coun_data):
    infos = []
    for country in pop_data_list:
        name = country['Country (or dependency)']
        #print(name)
        for country_info in coun_data :
            #print(country_info)
            if name in country_info:
                country_info = country_info + ";" + country['Population (2020)'] + ";" + country['Land Area (KmÂ²)']
                #infos.append(country_info)
                #print(country_info)
                infos.append(country_info)
    return infos




            


