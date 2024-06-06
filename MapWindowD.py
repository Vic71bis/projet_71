# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:46:40 2024

@author: Utilisateur
"""
from tkintermapview import TkinterMapView
import customtkinter as ct
from pathlib import Path
from EntryWindowD import EntryWindow
import json
import csv
import math
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MapWindow") 
####################################################### INITIALIZING ALL THE CSV FILES NEEDED


def country_csv_to_dict (csv_file):
    eliminer_entete = True
    with open(csv_file, newline = "", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        data = {}
        if eliminer_entete:
            reader.__next__()
        for row in reader:
           country_abreviation, country, capital, lat, long, pop, yearly_change, net_change, density, land_area, migrants, fertility_rate, median_age, urban_pop, world_share = row
           data[country_abreviation] = [country,capital, lat, long, pop, yearly_change, net_change, density, land_area, migrants, fertility_rate, median_age, urban_pop, world_share]
    return data


def open_json_file (json_file) :
    with open(json_file, 'r') as file:
        new_file = json.load(file)
    return new_file
def convert_in_latN_and_longE(countries_info):
    ''' 
    parameters: 
        countries_info (dictionary with country information)

    returns:
        modified dictionary with latitude in N and longitude in E
    ''' 
    for country_abreviation in countries_info.keys():
        lat = countries_info[country_abreviation][2] 
        long = countries_info[country_abreviation][3]
        
        # Convertir la latitude de S à N
        if 'S' in lat:
            lat = -float(lat[:-1])  # Supprimer le caractère 'S' et changer le signe
        
        # Supprimer 'N' de la latitude
        elif 'N' in lat:
            lat = float(lat[:-1])  # Supprimer le caractère 'N' 
            
        # Convertir la longitude de W à E
        if 'W' in long:
            long = -float(long[:-1])  # Supprimer le caractère 'W' et changer le signe

        # Supprimer 'E' de la longitude
        elif 'E' in long:
            long = float(long[:-1])  # Supprimer le caractère 'E'

        # Mettre à jour les valeurs dans le dictionnaire
        countries_info[country_abreviation][2] = lat
        countries_info[country_abreviation][3] = long

    return countries_info
def convert_time_hours (hours, minutes):
    if type(hours)==int and type(minutes)==int :
        h = int(hours)
        m = int(minutes)/60
        tot_time = h + m
        return tot_time 
    else :
        print('The values are not numbers')
##################################################################### USEFUL FUNCTIONS TO NAVIGATE THROUGH FILES


country_neighbours=open_json_file('country_neighbours.json')

countries_info=country_csv_to_dict('countries_info.csv') 
convert_in_latN_and_longE(countries_info)

class MapWindow(EntryWindow):
    MapWindow_Name = "Map Window"
    HEIGHT = 700
    WIDTH = 1000

    def __init__(self, countries_info, country_neighbours, entry_name, entry_position,h, minutes,choice_earth, choice_air, *args, **kwargs):
        # Initialize EntryWindow without creating widgets
        super().__init__(create_widget=False, *args, **kwargs)
        self.geometry(f"{MapWindow.WIDTH}x{MapWindow.HEIGHT}")
        self.minsize(MapWindow.WIDTH, MapWindow.HEIGHT)
        self.title(MapWindow.MapWindow_Name)
        self.protocol("WM_DELETE_WINDOW", self.quitter)
        self.h = h
        self.min = minutes
        self.entry_name = entry_name
        self.entry_position =entry_position
        self.countries_info=countries_info
        self.choice_earth = choice_earth
        self.choice_air = choice_air
        self.country_neighbours = country_neighbours
        self.reachable_country = self.compute_reachable_countries()
        
        self.display_info = None
        self.create_widgets1()
    
        
    def create_widgets1(self):
            # Configure grid layout for the main window
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)
    
            # Create the left frame
            self.frame_left = ct.CTkFrame(master=self, width=250, corner_radius=0, fg_color=None)
            self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
    
            # Create the right frame
            self.frame_right = ct.CTkFrame(master=self, corner_radius=0)
            self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
    
            # Configure the right frame grid
            self.frame_right.grid_rowconfigure(0, weight=0)
            self.frame_right.grid_rowconfigure(1, weight=1)
            self.frame_right.grid_columnconfigure(0, weight=0)
            self.frame_right.grid_columnconfigure(1, weight=0)
            self.frame_right.grid_columnconfigure(2, weight=0)
            self.frame_right.grid_columnconfigure(3, weight=1)

            # Add widgets to the right frame
            self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
            self.map_widget.add_left_click_map_command(self.display_info_countries)
            self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=4, sticky="nsew", padx=(0, 0), pady=(0, 0))
            
            self.name = ct.CTkLabel(master=self.frame_right, text=f"Name:{self.entry_name}")
            self.name.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
    
            self.position = ct.CTkLabel(master=self.frame_right, text=f"Position:{self.entry_position}")
            self.position.grid(row=0, column=1, sticky="we", padx=(12, 0), pady=12)
            
            self.time = ct.CTkLabel(master=self.frame_right, text=f"Time:{self.h}h {self.min}min")
            self.time.grid(row=0, column=2, sticky="we", padx=(12, 0), pady=12)
    
            self.button_quit = ct.CTkButton(master=self.frame_right, text="Quit", width=70, command=self.quit)
            self.button_quit.grid(row=0, column=3, sticky="e", padx=(10, 10), pady=12)
    
            # Configure the left frame grid
            self.frame_left.grid_rowconfigure(0, weight=0)
            self.frame_left.grid_rowconfigure(1, weight=1)
            self.frame_left.grid_columnconfigure(0, weight=1)
    
            # Create upper and lower frames within the left frame
            self.frame_left_up = ct.CTkFrame(master=self.frame_left, width=250, corner_radius=0, fg_color=None)
            self.frame_left_up.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

            #configure text area
            self.text_area = ct.CTkTextbox(master=self.frame_left, width=250, corner_radius=0, fg_color="#E74C3C")
            self.text_area.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
            
            # Add widgets to the upper and lower frames
            label_up = ct.CTkLabel(master=self.frame_left_up, text="Settings", font=("Arial", 12))
            label_up.grid(row = 0, column =0, padx=(10, 10), pady=(10, 10))
           
           # self.reachable_country=self.reachable_countries()
            self.country = ct.CTkOptionMenu(self.frame_left_up, values = self.reachable_country, command = self.display_info)
            self.country.grid (row= 1, column = 0, padx=(10, 10), pady=(10, 0))
            
            self.map_label = ct.CTkLabel(self.frame_left_up, text="Tile Server:", anchor="w")
            self.map_label.grid(row=2, column=0, padx=(20, 20), pady=(20, 0))
            self.map_option_menu = ct.CTkOptionMenu(self.frame_left_up, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                           command=self.change_map)
            self.map_option_menu.grid(row=3, column=0, padx=(20, 20), pady=(10, 0))

            self.appearance_mode_label = ct.CTkLabel(self.frame_left_up, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=4, column=0, padx=(20, 20), pady=(20, 0))
            self.appearance_mode_optionemenu = ct.CTkOptionMenu(self.frame_left_up, values=["Light", "Dark", "System"],
                                                                           command=self.change_appearance_mode)
            self.appearance_mode_optionemenu.grid(row = 5, column=0, padx=(20, 20), pady=(10, 20))
            
            self.add_marker()
            #self.map_option_menu.set("OpenStreetMap")
            #self.appearance_mode_optionemenu.set("Dark")
    

    
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    
   
    def get_country_code_from_address(self, address):
        location = geolocator.geocode(address)
        coordinates =(location.latitude, location.longitude)
        reverse_location = geolocator.reverse(coordinates)
        country_code =reverse_location.raw['address']['country_code'].upper()
        return country_code
    
    
   
    def convert_time_hours (self):
       if type(self.h)==int and type(self.min)==int :
           tot_time = self.h + self.min/60
           return tot_time 
       else :
           print('The values are not numbers')
    
    def get_dist_from_time_and_transport (self,time_hours):
        distance_travel=0
        if self.choice_air.get() == 1:
            speed = 800   
        elif self.choice_earth.get() == 1:
            speed = 95
        distance_travel = speed *float(time_hours)
        return distance_travel
    
    def distance_countries(self,country_1,country_2):
        #country_abreviation_1 = self.get_country_code_from_address(country_1)
        #country_abreviation_2= self.get_country_code_from_address(country_2)
        # Extract latitude and longitude coordinates of capital cities
        latA, longA = self.countries_info[country_1][2], self.countries_info[country_1][3]
        latB, longB = self.countries_info[country_2][2], self.countries_info[country_2][3]

        city_A_coordinates = (latA,longA)
        city_B_coordinates = (latB,longB)
        # Calculate distance between the two cities
        dist = geodesic(city_A_coordinates, city_B_coordinates).kilometers
        
        return dist
    
    def compute_reachable_countries(self):
        reachable_country =[]
        position = self.get_country_code_from_address(self.entry_position)
        time_hours = self.convert_time_hours()
        dist=self.get_dist_from_time_and_transport(time_hours)
        distance_countries =0
        neighbours_list = self.country_neighbours.get(position)
        for country in neighbours_list :
            neighbour = country[1]
            distance_countries +=self.distance_countries(position, neighbour)
            if distance_countries < dist :
                reachable_country.append(f'{country[0]}')
            dist+= distance_countries
        
        return reachable_country
    
    def add_marker (self) :
        for country in self.reachable_country :
            country_code=self.get_country_code_from_address(country)
            lat = self.countries_info[country_code][2]
            lon = self.countries_info[country_code][3]
            self.map_widget.set_marker(lat,lon)
            
    def create_bfs (self,start):
        self.get_country_code_from_address(start)
        a_traiter = [start]
        dico_prec = {}
        dico_prec[start] = None
        treated = []
        
        while len(a_traiter) > 0:
            s = a_traiter.pop(0)
            treated.append(s)
            if s in self.country_neighbours:
                for si in self.country_neighbours[s]:
                    if si != []:
                        s_abrev = si[1]
                        if s_abrev not in treated and s_abrev not in a_traiter:
                            a_traiter.append(s_abrev)
                            dico_prec[s_abrev] = s
                        
        return dico_prec

    def is_reachable (self, start, end):
        ans = 10
        tree = self.create_bfs(start)
        if end in tree:
            ans = True
        else:
            ans = False
        return ans, tree
    
    def shortest_path(self,v, parents):
        path = []
        while v is not None:
            path.append(v)
            v = parents[v]
        return path[::-1]
    
    def get_path_btw_countries (self, start,end):
        reachable, tree = self.is_reachable(start,end)
        if reachable:
            path = self.shortest_path(end, tree)
            return path
        else:
            return False
        
    def change_appearance_mode(self, new_appearance_mode: str):
        ct.set_appearance_mode(new_appearance_mode)
    
    
   
    def display_info_countries(self,event): 
        location =geolocator.reverse((event[0], event[1]))
        try:
            country = location.raw['address']['country_code'].upper()
        except:
            country = None
        if country:
            country_information= self.countries_info.get(country, "No information available") 
            #if self.choice_earth.get ==1 :
                #travel = get_path_btw_countries(self.entry_position, country, all_countries)
                #self.text_area.insert('The traject by car is : {travel}')
            self.text_area.delete("1.0","end")  
            self.text_area.insert('1.0',f'Country :{country_information[0]}\n Capital ={country_information[1]}\n Population ={country_information[4]}\n Yearly_change ={country_information[5]} \n Land Area ={country_information[7]} \n Density = {country_information[8]} \n Median age : { country_information[10]} \n') # à ajouter des infos si on veut
            country_name = country_information[0]
            if country_name in self.reachable_country :
                start = self.get_country_code_from_address(self.entry_position)
                path_to_country = self.get_path_btw_countries(start,country)
                self.text_area.insert('10.0',f'The path is {path_to_country}')
        else: 
            self.text_area.insert("Country not found for the given coordinates")	 
        
    def quitter(self, event=0):
        self.destroy()
        
    def start(self):
        self.mainloop()
        
    
        
if __name__ == "__main__":
    entry_window = EntryWindow()
    entry_window.start()
    if entry_window.window_closed:
        second_window = MapWindow(countries_info, country_neighbours, entry_name = entry_window.entry_name, entry_position = entry_window.entry_position, h = entry_window.time_for_travelling_hour, minutes= entry_window.time_for_travelling_min, choice_earth = entry_window.choice_earth, choice_air = entry_window.choice_air)
        second_window.start()


