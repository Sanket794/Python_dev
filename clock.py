# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:20:29 2024

@author: verma
"""
from tkinter import *
from tkinter .ttk import *
from time import strftime

root = Tk()

root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000,time)
    
label = Label(root,font =("1800"),foreground= "white", background = "black")
label.pack(anchor = "center")

time()

mainloop()