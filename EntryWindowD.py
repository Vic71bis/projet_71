# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:38:53 2024

@author: Utilisateur
"""


from tkintermapview import TkinterMapView
import customtkinter as ct
from pathlib import Path

import customtkinter as ct

ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("light")



##### Define all the widgets : the buttons, the areas to enter text
##### Positionning of the widgets

##### starting window where the user is giving its informations
class EntryWindow(ct.CTk): 
    EntryWindow_Name = "Introduction Window"
    HEIGHT = 300
    WIDTH = 600
    
    def __init__(self, create_widget=True, *args, **kwargs): 
        ###### create the window
        super().__init__(*args, **kwargs)
        self.geometry(f"{EntryWindow.WIDTH}x{EntryWindow.HEIGHT}")
        self.minsize(EntryWindow.WIDTH, EntryWindow.HEIGHT)
        self.title(EntryWindow.EntryWindow_Name)
        self.protocol("WM_DELETE_WINDOW", self.quitter)
        self.bind("<Command-q>", self.quitter)

        ##### Name, country, time_for_travelling (are the attributs of the class that the user will define while writing inside the Entry widgets)
        self.window_closed = False
        self.entry_name = None
        self.entry_position = None
        self.time_for_travelling_hour = None
        self.time_for_travelling_min = None

        ##### Choice of the transport : the user can choose either to travel by plane or by bus/car
        self.choice_air = ct.IntVar()
        self.choice_earth = ct.IntVar()
        self.background_color = ct.IntVar()
        
        if create_widget:
            self.create_widgets()

    def create_widgets(self):
        
            self.resizable(False, False)
        
            ##### create a grid to place the widgets
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)
            self.grid_columnconfigure(3, weight=1)
            self.grid_columnconfigure(4, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)
            self.grid_rowconfigure(2, weight=1)
            self.grid_rowconfigure(3, weight=1)
            self.grid_rowconfigure(4, weight =1)
           
            ####### Add the labels to the text entry widgets (name, position, time_for_travelling)
            name_label=ct.CTkLabel(self, text="Name : ",  fg_color = '#7FB3D5', corner_radius = 10, anchor = 'w')
            name_label.grid(row=0, column=0, padx= (5,5), pady= (5,5))
           
            self.entry_1=ct.CTkEntry(self)
            self.entry_1.grid(row=0, column=1,padx = (5,10), pady = (5,5))
               
            position_label=ct.CTkLabel(self, text="Your position :", fg_color = '#7FB3D5', corner_radius = 10, anchor = 'w')
            position_label.grid(row=1, column=0, padx= (5,5), pady= (5,5))
            self.entry_2 =ct.CTkEntry(self)
            self.entry_2.grid(row=1, column=1, padx= (5,5), pady= (5,5))
               
            time_for_travelling_label= ct.CTkLabel(self, text="How much time do you have? ", fg_color = '#7FB3D5', corner_radius = 10, anchor = 'w')
            time_for_travelling_label.grid(row=2, column=0, padx= (5,5), pady= (5,5))
            self.entry3= ct.CTkEntry(self)
            self.entry3.grid(row=2,column=1, padx= (5,5), pady= (5,5))
            self.entry4= ct.CTkEntry(self)
            self.entry4.grid(row=2, column=3,  padx= (5,5), pady= (5,5))
            
            h_label = ct.CTkLabel (self, text = ":h")
            h_label.grid(row =2, column = 2)
            min_label = ct.CTkLabel (self, text = ':min')
            min_label.grid (row = 2, column = 4)
            
            mean_transport=ct.CTkLabel (self, text ='How do you travel ?',  fg_color = '#7FB3D5', corner_radius = 10, anchor = 'w')
            mean_transport.grid (row = 3, column = 0 )
            transport_air=ct.CTkCheckBox(self, text=' Plane', variable=self.choice_air)
            transport_air.grid(row=3, column = 1,  padx= (5,5), pady= (5,5))
            transport_earth=ct.CTkCheckBox(self, text='Train/Car', variable = self.choice_earth)
            transport_earth.grid(row=3, column = 3,  padx= (5,5), pady= (5,5))

            ##### creation of the buttons Quit, Save and Next and place them in the window
            self.following_window=ct.CTkButton(self, text='Next ->',  fg_color = '#7FB3D5', corner_radius = 10)
            self.following_window.grid(row=4,column=0,  padx= (5,5), pady= (5,5))
            
            self.quit_window=ct.CTkButton(self, text='Quit', command = self.quitter,  fg_color = '#7FB3D5', corner_radius = 10)
            self.quit_window.grid(row=4, column=3, padx= (5,5), pady= (5,5))
            
            self.save = ct.CTkButton (self,text = "Save", command = self.store_user_input,  fg_color = '#7FB3D5', corner_radius = 10)
            self.save.grid (row = 4, column = 1, padx= (5,5), pady= (5,5) )


    
    def store_user_input(self):
            """ 
            The function stores the variables entered by the user in the attributs of the Entry Window class
            Parameters : 
                self

            Return : 
                None (but modifies the attributs of the class when running the function)
            """
        
             self.entry_name = self.entry_1.get()
             self.entry_position = self.entry_2.get()
             if check_error_entry_position (self, world_countries):
                 self.entry_position = self.entry_2.get()
             self.time_for_travelling_hour = self.entry3.get()
             self.time_for_travelling_min = self.entry4.get()

    
    def check_error_entry_position (self, world_countries):
        """ 
        Checks if the position entered by the user is inside the csv file we use after for the rest of the code
        Parameters : 
            self
            world_countries (a dico of all the countries available)
        Return : 
            error (boolean saying if the entrance if correct )
        """
            error = True
            for country in world_countries.values():
                if country[0] == self.entry_position:
                    error = False
            return error  


    
    #### closes the window 
    def quitter (self, event=0):
           self.window_closed = True
           self.destroy()
           print (self.entry_name, self.entry_position)

    
    ##### Opens the window
    def start(self):
        self.mainloop()


