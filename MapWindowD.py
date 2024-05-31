# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:46:40 2024

@author: Utilisateur
"""
from tkintermapview import TkinterMapView
import customtkinter as ct
from pathlib import Path
from EntryWindowD import EntryWindow

class MapWindow(EntryWindow):
    MapWindow_Name = "Map Window"
    HEIGHT = 700
    WIDTH = 1000
    
    def __init__(self, entry_name, entry_position,h, minutes, *args, **kwargs):
        # Initialize EntryWindow without creating widgets
        super().__init__(create_widget=False, *args, **kwargs)
        self.geometry(f"{MapWindow.WIDTH}x{MapWindow.HEIGHT}")
        self.minsize(MapWindow.WIDTH, MapWindow.HEIGHT)
        self.title(MapWindow.MapWindow_Name)
        self.protocol("WM_DELETE_WINDOW", self.quitter)
        self.bind("<Command-q>", self.quitter)
        self.h = h
        self.min = minutes
        self.entry_name = entry_name
        self.entry_position = entry_position
        self.reachable_country = ["Germany", "Italy"]
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
    
            self.frame_left_down = ct.CTkFrame(master=self.frame_left, width=250, corner_radius=0, fg_color="#E74C3C")
            self.frame_left_down.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
    
            # Add widgets to the upper and lower frames
            label_up = ct.CTkLabel(master=self.frame_left_up, text="Settings", font=("Arial", 12))
            label_up.grid(row = 0, column =0, padx=(10, 10), pady=(10, 10))
    
            label_down = ct.CTkLabel(master=self.frame_left_down, text="Frame for info", font=("Arial", 12))
            label_down.grid(row = 0, column =0, padx=(10, 10), pady=(10, 10))
            
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
            
            
            #self.map_option_menu.set("OpenStreetMap")
            #self.appearance_mode_optionemenu.set("Dark")
            #self.map_widget.set_address("Berlin")
    

    
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            
    def change_appearance_mode(self, new_appearance_mode: str):
        ct.set_appearance_mode(new_appearance_mode)
    
    def quitter(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    entry_window = EntryWindow()
    entry_window.start()
    if entry_window.window_closed:
        second_window = MapWindow(entry_name = entry_window.entry_name, entry_position = entry_window.entry_position, h = entry_window.time_for_travelling_hour, minutes= entry_window.time_for_travelling_min)
        second_window.start()


