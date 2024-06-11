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
import logging
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
#logging.basicConfig(level=logging.DEBUG)
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

##################################################################### USEFUL FUNCTIONS TO NAVIGATE THROUGH FILES


country_neighbours=open_json_file('country_neighbours.json')
countries_info=country_csv_to_dict('countries_info.csv') 
convert_in_latN_and_longE(countries_info)

class MapWindow(EntryWindow):
    MapWindow_Name = "Map Window"
    HEIGHT = 700
    WIDTH = 1200

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
        self.max_time = self.convert_time_hours()
        self.max_distance = self.get_dist_from_time_and_transport(self.max_time)
        self.reachable_countries = self.compute_reachable_countries()
       
        
        self.display_info = None
        self.create_widgets1()
    
        
    def create_widgets1(self):
            # Configure grid layout for the main window
            
            location = geolocator.geocode(self.entry_position)
            
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
            
            self.name = ct.CTkLabel(master=self.frame_right, text=f"Name:{self.entry_name}", bg_color = "#7FB3D5", corner_radius = 20,  font=("Arial", 14, "bold"))
            self.name.grid(row=0, column=0, sticky="we", padx=20, pady=12)
    
            self.position = ct.CTkLabel(master=self.frame_right, text=f"Position:{self.entry_position}",bg_color = "#7FB3D5", corner_radius = 20,  font=("Arial", 14, "bold"))
            self.position.grid(row=0, column=1, sticky="we", padx=20, pady=12)
            
            self.time = ct.CTkLabel(master=self.frame_right, text=f"Time:{self.h}h {self.min}min",bg_color = "#7FB3D5", corner_radius = 20,  font=("Arial", 14, "bold"))
            self.time.grid(row=0, column=2, sticky="we", padx=20, pady=12)
    
            self.button_quit = ct.CTkButton(master=self.frame_right, text="Quit", width=70, command=self.quit)
            self.button_quit.grid(row=0, column=3, sticky="e", padx=(10, 10), pady=12)
    
            # Configure the left frame grid
            self.frame_left.grid_rowconfigure(0, weight=0)
            self.frame_left.grid_rowconfigure(1, weight=1)
            self.frame_left.grid_columnconfigure(0, weight=1)
    
            # Create upper and lower frames within the left frame
            self.frame_left_up = ct.CTkFrame(master=self.frame_left, width=250, corner_radius=0, fg_color=None, border_color = "#E74C3C")
            self.frame_left_up.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
            
            self.info_frame = ct.CTkFrame(self.frame_left, width=250, height=400)
            self.info_frame.grid(row=1, column = 0,padx=0, pady=0, sticky="nsew")
            self.info_frame.grid_columnconfigure(0, weight=0)
            
            self.country_name_label = ct.CTkLabel(self.info_frame, text="Country:", font=("Arial", 16, "bold"))
            self.country_name_label.grid(row=0, column=0, sticky="nsew", padx=0, pady=20)
    
            self.capital_label = ct.CTkLabel(self.info_frame, text="Capital:", font=("Arial", 16, "bold"))
            self.capital_label.grid(row=1, column=0, sticky="nsew", padx=0, pady=10)
    
            # Menu for additional information
            self.info_menu = ct.CTkTextbox(self.info_frame, height=100)
            self.info_menu.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=0, pady=5)
    
            # Path display
            self.path_label = ct.CTkLabel(self.info_frame, text="Path:", font=("Arial", 14, "bold"))
            self.path_label.grid(row=3, column=0, sticky="nsew", padx=0, pady=10)
    
            self.path_text = ct.CTkTextbox(self.info_frame, height=50)
            self.path_text.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=0, pady=5)
    
            #configure text area
            #self.text_area = ct.CTkTextbox(master=self.frame_left, width=250, corner_radius=0, fg_color="#E74C3C")
            #self.text_area.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
            
            # Add widgets to the upper and lower frames
            label_up = ct.CTkLabel(master=self.frame_left_up, text="Settings", font=("Arial", 14))
            label_up.grid(row = 0, column =0, padx=(10, 10), pady=(10, 10))
            
          
            self.reach_country = ct.CTkLabel(self.frame_left_up, text="Reachable countries:", anchor="w")
            self.reach_country.grid(row=1, column=0, padx=(20, 20), pady=(20, 0))
           
            self.country = ct.CTkOptionMenu(self.frame_left_up, values = [self.countries_info[code][0] for code in self.reachable_countries], command = self.display_info_from_menu)
            self.country.grid (row= 2, column = 0, padx=(10, 10), pady=(10, 0))
            
            self.map_label = ct.CTkLabel(self.frame_left_up, text="Tile Server:", anchor="w")
            self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
            self.map_option_menu = ct.CTkOptionMenu(self.frame_left_up, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                           command=self.change_map)
            self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

            self.appearance_mode_label = ct.CTkLabel(self.frame_left_up, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
            self.appearance_mode_optionemenu = ct.CTkOptionMenu(self.frame_left_up, values=["Light", "Dark", "System"],
                                                                           command=self.change_appearance_mode)
            self.appearance_mode_optionemenu.grid(row = 6, column=0, padx=(20, 20), pady=(10, 20))
            
            self.add_marker()
            self.map_option_menu.set("OpenStreetMap")
            self.appearance_mode_optionemenu.set("Dark")
            
            if location:
               # logging.debug(f"Setting map position to {location.latitude}, {location.longitude}")
                self.map_widget.set_position(location.latitude, location.longitude)
                self.map_widget.set_zoom(5)
    

    
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
    
    def distance_countries(self, country_1, country_2):
        def convert_to_float(coord):
            coord = str(coord)
            if 'N' in coord or 'E' in coord:
                return float(coord[:-1])
            elif 'S' in coord or 'W' in coord:
                return -float(coord[:-1])
            return float(coord)

        latA, longA = self.countries_info[country_1][2], self.countries_info[country_1][3]
        latB, longB = self.countries_info[country_2][2], self.countries_info[country_2][3]
    
        latA, longA = convert_to_float(latA), convert_to_float(longA)
        latB, longB = convert_to_float(latB), convert_to_float(longB)
    
        city_A_coordinates = (latA, longA)
        city_B_coordinates = (latB, longB)
        dist = geodesic(city_A_coordinates, city_B_coordinates).kilometers
    
        return dist

    
    def compute_reachable_countries(self):
        reachable_country =[]
        time_hours = self.convert_time_hours()
        position = self.get_country_code_from_address(self.entry_position)
        dist=self.get_dist_from_time_and_transport(time_hours)
        distance_countries=0
        if self.choice_air.get()==1 :
            for country_code in self.countries_info.keys() :
                distance_countries = self.distance_countries(position,country_code)
                if distance_countries < dist and distance_countries!=0 :
                    #country = countries_info[country_code][0] pour avoir les country en code pour être coherent avec earth
                    reachable_country.append(country_code)
                    print(reachable_country)
                    
        elif self.choice_earth.get()==1:
            reachable_country , total_path, path = self.create_bfs(position)
            print(reachable_country)
            
            
        """elif self.choice_earth.get()==1 :
            for country_code in self.countries_info.keys() :
                path_list = self.get_path_btw_countries(position, country_code)
                print(path_list)
                if path_list :
                    for element in path_list :
                        distance_countries +=self.distance_countries(position, country_code)
                        if distance_countries < dist :
                            print(element)
                            country_name = self.countries_info[element][0]
                            reachable_country.append(f'{country_name}')
                    distance_countries=0   """
        return reachable_country
    
    def add_marker (self) :
        for country in self.reachable_countries :
            country_code=self.get_country_code_from_address(country)
            lat = self.countries_info[country_code][2]
            lon = self.countries_info[country_code][3]
            #logging.debug(f"Adding marker at {lat}, {lon}")
            self.map_widget.set_marker(lat,lon)
            
    """def create_bfs_1 (self,start):
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
                        
        return dico_prec"""
    
    def create_bfs(self, start):
        queue = [(start, 0)]
        predecessors = {start: start}
        distances = {start: 0}
        reachable_countries = set()
        paths = []
    
        while queue:
            current_country, current_distance = queue.pop(0)
            reachable_countries.add(current_country)
    
            if predecessors[current_country] is not None:
                current_lat, current_lon = self.countries_info[current_country][2], self.countries_info[current_country][3]
                parent_lat, parent_lon = self.countries_info[predecessors[current_country]][2], self.countries_info[predecessors[current_country]][3]
                paths.append(((parent_lat, parent_lon), (current_lat, current_lon)))
    
            neighbours = self.country_neighbours.get(current_country, [])
            for neighbour_info in neighbours:
                neighbour = neighbour_info[1]
                distance = self.distance_countries(current_country, neighbour)
                new_distance = current_distance + distance
    
                if neighbour not in distances or new_distance < distances[neighbour]:
                    if new_distance <= self.max_distance:
                        queue.append((neighbour, new_distance))
                        predecessors[neighbour] = current_country
                        distances[neighbour] = new_distance

    
        """print("BFS Reachable Countries: ", reachable_countries) #debugging
        print("BFS Predecessors: ", predecessors)
        print("BFS Paths: ", paths)
        print(f"Current Country: {current_country}")
        print(f"Total Distance: {current_distance + distance}")
        print(f"Path List: {paths}")"""

        return list(reachable_countries), predecessors, paths


    def create_bfs_paths(self, path_to_country):
        paths = []
    
        # Generate paths only for the provided path_to_country
        for i in range(len(path_to_country) - 1):
            start_country = path_to_country[i]
            next_country = path_to_country[i + 1]
            start_lat, start_lon = self.countries_info[start_country][2], self.countries_info[start_country][3]
            end_lat, end_lon = self.countries_info[next_country][2], self.countries_info[next_country][3]
            paths.append(((start_lat, start_lon), (end_lat, end_lon)))
    
        # Create paths on the map using the filtered path data
        for path in paths:
            path_list = [path[0], path[1]]
            path_obj = self.map_widget.set_path(path_list)
            path_obj.set_position_list(path_list)


    # Return the BFS results
       # return reachable_countries, predecessors


    """def is_reachable (self, start, end):
        ans = 10
        reach, tree, path = self.create_bfs(start)
        if end in tree:
            ans = True
        else:
            ans = False
        return ans, tree"""
    
    def reconstruct_path(self, start, end, predecessors):
        path = []
        step = end
        while step != start:  # Change here to avoid adding start multiple times
            path.append(step)
            step = predecessors.get(step)
        path.append(start)  # Add start at the end to complete the path
        path.reverse()  # Reverse the path to get it from start to end
        print(f"Reconstructed Path from {start} to {end}: {path}")  # Debugging output
        return path
    
    """def get_path_btw_countries (self, start,end):
        reachable, tree = self.is_reachable(start,end)
        if reachable:
            path = self.shortest_path(end, tree)
            return path
        else:
            return False"""
        
    def shortest_path(self,v, parents):
        path = []
        while v is not None:
            path.append(v)
            v = parents[v]
        return path[::-1]
        
    def change_appearance_mode(self, new_appearance_mode: str):
        ct.set_appearance_mode(new_appearance_mode)
    
    
    def display_info_countries(self, event):
       location = geolocator.reverse((event[0], event[1]))
       try:
           country_code = location.raw['address']['country_code'].upper()
       except:
           country_code = None
       if country_code:
           country_information = self.countries_info.get(country_code, "No information available")
           self.clear_info_display()  # Clear previous info
           if country_information != "No information available":
                self.country_name_label.configure(text=f"Country: {country_information[0]}")
                self.capital_label.configure(text=f"Capital: {country_information[1]}")

                self.info_menu.delete("1.0", "end")
                self.info_menu.insert("1.0", f"Population: {country_information[4]}\nYearly Change: {country_information[5]}\nLand Area: {country_information[7]}\nDensity: {country_information[8]}\nMedian Age: {country_information[11]}")
                if country_code in self.reachable_countries and self.choice_earth.get() == 1:
                   start = self.get_country_code_from_address(self.entry_position)
                   reachable_countries, predecessors, path = self.create_bfs(start)
                   path_to_country = self.reconstruct_path(start, country_code, predecessors)
                   path_details = " -> ".join([self.countries_info[code][0] for code in path_to_country])
                   self.path_text.delete("1.0", "end")
                   self.path_text.insert("1.0", f"{path_details}")
           else:
                self.country_name_label.configure(text="No information available")
       else:
            self.country_name_label.configure(text="Country not found")
            
            
    def display_info_from_menu(self, selection):
    # Reverse lookup country abbreviation from the full-length name
        country_code = next((key for key, value in self.countries_info.items() if value[0] == selection), None)
        if country_code:
            country_information = self.countries_info.get(country_code, "No information available")
            self.clear_info_display()
            if country_information != "No information available":
                self.clear_info_display()  # Clear previous info
                self.country_name_label.configure(text=f"Country: {country_information[0]}")
                self.capital_label.configure(text=f"Capital: {country_information[1]}")

                self.info_menu.delete("1.0", "end")
                self.info_menu.insert("1.0", f"Population: {country_information[4]}\nYearly Change: {country_information[5]}\nLand Area: {country_information[7]}\nDensity: {country_information[8]}\nMedian Age: {country_information[11]}")
                if country_code in self.reachable_countries and self.choice_earth.get() == 1:
                    start = self.get_country_code_from_address(self.entry_position)
                    reachable_countries, predecessors,_= self.create_bfs(start)
                    path_to_country = self.reconstruct_path(start, country_code, predecessors)
                    path_details = " -> ".join([self.countries_info[code][0] for code in path_to_country])
                    self.path_text.delete("1.0", "end")
                    self.path_text.insert("1.0", f"{path_details}")
                    
                    self.clear_path()
                    self.create_bfs_paths(path_to_country)
                    location = geolocator.geocode(countries_info[country_code][0])
                    self.map_widget.set_position(location.latitude, location.longitude)
                
            else:
                self.country_name_label.configure(text="No information available")
        else:
            self.country_name_label.configure(text="Country not found")
            
    def clear_info_display(self):
        
        self.country_name_label.configure(text="Country:")
        self.capital_label.configure(text="Capital:")
        self.info_menu.delete("1.0", "end")
        self.path_text.delete("1.0", "end")

    def clear_path(self):
        self.map_widget.delete_all_path()

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


