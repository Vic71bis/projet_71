# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:02:04 2024

@author: Utilisateur
"""

import tkinter as tk
import tkintermapview
from geopy.geocoders import Nominatim
import csv
from random import randint
import json
import time 
import datetime
from pathlib import Path
locator = Nominatim(user_agent='myGeocoder')

class MapWindow ():
    
    def __init__ (self):
        
        self.cwd = Path(__file__).parent
        self.root_tk = tk.Tk()
        self.root_tk.geometry(f"{1500}x{700}")
        self.root_tk.title("map_window.py")
        self.coordinates = (self.cwd / 'POSITION-2.csv').resolve()
        self.tile_1 = "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga"
        self.tile_2 = "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png "
        
        self.color_2 ='#CBF1F0'
        self.color_1 = '#FFEF9F'
        
        self.var1 = tk.IntVar ()
        self.var2 = tk.IntVar ()
        self.var3 = tk.IntVar ()
        
        self.dic_transport = {}
        
        self.location = []
        self.quit = ()
        self.time_user = []
        
        self.create_widget()
        

        #start up functions to add if needed#
        
        #self.data_csv = self.csv_to_dict()

        #def intro_window (if we choose to call it here)
        
    def create_widget(self):
        # Left side frames
        self.frame_left_up = tk.Frame(self.root_tk, width=300, bg=self.color_1)
        self.frame_left_up.grid(row=0, column=0, sticky ='nsew')  # Sticky makes the frame fill the cell
        self.root_tk.grid_rowconfigure(0, weight=0)
        
        self.frame_left_down = tk.Frame(self.root_tk, width=300, bg=self.color_2)
        self.frame_left_down.grid(row=1, column=0, sticky ='nsew')  # Sticky makes the frame fill the cell
        self.root_tk.grid_rowconfigure(1, weight=0)

        # Right side frame
        self.frame_right = tk.Frame(self.root_tk, width=1200, height=700)
        self.frame_right.grid(row=0, column=1, rowspan=2, sticky="nsew")  
        self.root_tk.grid_columnconfigure(1, weight=1)  # Allow frame_right to expand horizontally
     
        self.map_widget = tkintermapview.TkinterMapView(self.frame_right, width=1200, height=700, corner_radius=10)
        self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        
        #self.map_widget.add_left_click_map_command(self.click)#
        self.map_widget.pack()
        
        #creation of the buttons
        
        self.label_1 = tk.Label(self.frame_left_up, text = 'User situation and preferences', font = 'Arial 17 bold', fg='black', bg = self.color_1)
        self.label_1.pack(fill='x')
        
        self.label_2 = tk.Label(self.frame_left_up, text = f"Location of user: {self.location}", font = 'Arial 12', fg = 'black', bg = self.color_1, pady = 10)
        self.label_2.pack(anchor= 'w')
        
        self.label_3 = tk.Label(self.frame_left_up, text = f"Time allocated to travel: {self.time_user}", font = 'Arial 12', fg = 'black', bg = self.color_1, pady =20)
        self.label_3.pack(anchor ='w')
       
        self.label_4 = tk.Label(self.frame_left_up, text='Mean of transport', font='Arial 12 bold', fg='black', background='#F5CBA7', pady=10)
        self.label_4.pack(anchor='center')
        
        self.check_b1 = tk.Checkbutton(self.frame_left_up, text='Plane', variable=self.var1, pady=5, bg = self.color_1 )
        self.check_b1.pack(fill='x')
        
        self.check_b2 = tk.Checkbutton(self.frame_left_up, text='Boat', variable=self.var2, pady=5, bg = self.color_1 )
        self.check_b2.pack(fill='x')
        
        self.check_b3 = tk.Checkbutton(self.frame_left_up, text='Car', variable=self.var3, pady= 5, bg = self.color_1 )
        self.check_b3.pack(fill='x')

        self.button1 = tk.Button (self.frame_left_up, text ='Reset choices', font = 'Arial 10 bold', fg = 'black', borderwidth = 2, relief = 'solid', pady = 5 )
        self.button1.pack(anchor = 'ne')
    
        self.label_5 = tk.Label (self.frame_left_down, text = 'Country information', font = 'Arial 17 bold', fg = 'black', bg = self.color_2)
        self.label_5.pack(anchor = 'n')
        
        self.frame_1 = tk.Frame(self.frame_left_down, width = 300, height = 300)
        self.frame_1.pack()
            
        self.button_quit = tk.Button (self.frame_left_down, text = 'Quit', command =self.quit, bg = 'red', font = 'Arial 10 bold', fg = 'black', borderwidth =2, relief = 'solid', padx =5, pady = 5 )
        self.button_quit.pack(anchor = 'se') 
        

        
if __name__ == '__main__':
    MapWindow1 = MapWindow()
    MapWindow1.root_tk.after(100, lambda: print("Frame left up height:", MapWindow1.frame_left_up.winfo_height()))
    MapWindow1.root_tk.after(100, lambda: print("Frame left down height:", MapWindow1.frame_left_down.winfo_height()))
    MapWindow1.root_tk.mainloop()

        
        
        
        
        