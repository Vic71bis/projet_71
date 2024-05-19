# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:55:11 2024

@author: diane
"""

import tkinter as tk
from MapWindow import MapWindow
from tkinter import Entry,Checkbutton,Radiobutton,Button

def convert_time_hours (hours, minutes):
    if type(hours)==int and type(minutes)==int :
        h = int(hours)
        m = int(minutes)/60
        tot_time = h + m
        return tot_time 
    else :
        print('The values are not numbers')

class EntryWindow (tk.Tk):
    '''Class who defines the entry window of the application, where the user has to give his name, position (where the user is),time to travel,option to change the map's color'''
    __slots__=['name','position','time_for_travelling','button_background','background_color','quit_window','following_window']
    
    def __init__(self, name, position, time_for_travelling_hour,time_for_travelling_min, quit_window,background_color,following_window, choice_air, choice_earth) :
        super().__init__()
        self.geometry("650x250")
                      
        self.title("Host Page")
        
        self.name=name
        self.position=position
        self.time_for_travelling_hour= time_for_travelling_hour
        self.time_for_travelling_min= time_for_travelling_min
        self.quit_window = quit_window
        self.following_window=following_window
        self.choice_air=tk.IntVar()
        self.choice_earth=tk.IntVar()
        self.background_color=tk.IntVar()
        
        self.configure(bg='#EEF0E5')
        
        self.create_widgets()
#means of transport, explanations, question "aller de là à là"
    def create_widgets(self):
        """
        Implement Entry to enter the name, the position, considered as string
        Implement Entry to enter the time the user has, considered as an integer
        Implement a Checkbutton, if the checkbutton is pressed, the background of the map is black
        Implement a Button to quit the application
        Implement a button to go to the next window that corresponds to the window with the Map and the solutions of travel
        Returns
        -------
        None.

        """
        name_label=tk.Label(self, text="Your name : ",bg='#B6C4B6',fg='#304D30')
        name_label.grid(row=0, column=0,padx=5, pady=5, sticky='w')
        self.name=tk.Entry(self)
        self.name.grid(row=0, column=0,padx=100, pady=5)
        

        
        position_label=tk.Label(self, text="Your position : ",bg='#B6C4B6', fg='#304D30')
        position_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.position =tk.Entry(self)
        self.position.grid(row=1, column=0, padx=100, pady=5)
        
        time_for_travelling_label= tk.Label(self, text="How much time do you have ?",bg='#B6C4B6', fg='#304D30')
        time_for_travelling_label.grid(row=2, column=0,padx=5, pady=5,sticky='w')
        
        time_for_travelling_label_hour= tk.Label(self, text=":h",bg='#B6C4B6', fg='#304D30')
        time_for_travelling_label_hour.grid(row=2, column=1, pady=5, sticky='nsew')

        self.time_for_travelling_hour= tk.Entry(self)
        self.time_for_travelling_hour.grid(row=2,column=0,pady=5, sticky='e')
        
        
        
        
        self.time_for_travelling_min= tk.Entry(self)
        self.time_for_travelling_min.grid(row=2, column=2, padx=5, pady=5,sticky='w')
        
        time_for_travelling_label_min= tk.Label(self, text=":min", bg='#B6C4B6', fg='#304D30')
        time_for_travelling_label_min.grid(row=2, column=2, pady=5, sticky='e')
        
        self.button_background=tk.Radiobutton(self, text='Dark Mode', variable= self.background_color,bg='#EEF0E5', fg='#163020')
        self.button_background.grid(row=3, columnspan=5, padx=10, pady=5,sticky='nsew')
        
        transport_air=tk.Checkbutton(self,text=' Plane', variable=self.choice_air,bg='#EEF0E5', fg='#163020')
        transport_air.grid(row=4, columnspan=5, padx=10, pady=5,sticky='nsew')
        
        transport_earth=tk.Checkbutton(self, text='Train/Car', variable = self.choice_earth,bg='#EEF0E5', fg='#163020')
        transport_earth.grid(row=5, columnspan=5, padx=10, pady=5,sticky='nsew')
        
        self.following_window=tk.Button(self, text='Next ->', bg='#163020',fg='#EEF0E5')
        self.following_window.bind('<Button-1>', self.get_to_next_window)
        self.following_window.grid(row=6,column=4, padx=50, pady=5, sticky='e')
        
        self.quit_window=tk.Button(self, text='Quit',bg='#163020',fg='#EEF0E5')
        self.quit_window.bind('<Button-1>', self.quitter)
        self.quit_window.grid(row=6, column=0, columnspan=4, padx = 10, sticky='w')
        
        
    def execute_choice(self,event):
        if self.choice.get()==1 :
            self.background_color= 'dark'
        else :
            self.background_color ='white'  
            
            
 # tot time in hours


    def quitter(self,event):
        self.destroy()
    
    def get_to_next_window(self,event):
        # Convert time to hours
        self.time_for_travelling_hour = convert_time_hours(int(self.time_for_travelling_hour.get()),int(self.time_for_travelling_min.get()))
        #close the current window
        self.destroy()


        #open the next window
        next_window = MapWindow
        next_window.mainloop()

        
    def beginning(self):
        self.mainloop()
if __name__=="__main__":
    entry_window=EntryWindow("","","","","","","","","")
    entry_window.beginning()