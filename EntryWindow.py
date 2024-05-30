# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:42:56 2024

@author: Utilisateur
"""


from tkintermapview import TkinterMapView
import customtkinter as ct
from pathlib import Path

ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("light")

    
class EntryWindow(ct.CTk):
    
    EntryWindow_Name = "Introduction Window"
    HEIGHT = 300
    WIDTH = 600
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry(str(EntryWindow.WIDTH) + "x" + str(EntryWindow.HEIGHT))
        self.minsize(EntryWindow.WIDTH, EntryWindow.HEIGHT)
        self.title(EntryWindow.EntryWindow_Name)
        
        self.protocol("WM_DELETE_WINDOW", self.quitter)
        self.bind("<Command-q>", self.quitter)
        #sets that the window doesn't rezise in height and width
        self.resizable (False,False)
       
        self.entry_name = None
        self.entry_position = None
        self.time_for_travelling_hour = None
        self.time_for_travelling_min = None

        self.choice_air = ct.IntVar()
        self.choice_earth = ct.IntVar()
        self.background_color = ct.IntVar()
        
        #sets if colums and row can expand
        
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
      
        
        
        self.create_widgets()
        
    def create_widgets(self):
            
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
            
            self.following_window=ct.CTkButton(self, text='Next ->',  fg_color = '#7FB3D5', corner_radius = 10)
            self.following_window.grid(row=4,column=0,  padx= (5,5), pady= (5,5))
            
            self.quit_window=ct.CTkButton(self, text='Quit', command = self.quitter,  fg_color = '#7FB3D5', corner_radius = 10)
            self.quit_window.grid(row=4, column=3, padx= (5,5), pady= (5,5))
            
            self.save = ct.CTkButton (self,text = "Save", command = self.store_user_input,  fg_color = '#7FB3D5', corner_radius = 10)
            self.save.grid (row = 4, column = 1, padx= (5,5), pady= (5,5) )
            
    def store_user_input(self):
             self.entry_name = self.entry_1.get()
             self.entry_position = self.entry_2.get()
             self.time_for_travelling_hour = self.entry3.get()
             self.time_for_travelling_min = self.entry4.get()
        
            
    def quitter (self, event=0):
            self.destroy()
            print (self.entry_name, self.entry_position)

    def start(self):
            self.mainloop()
            
if __name__=="__main__":
    entry_window=EntryWindow()
    entry_window.start()
    
