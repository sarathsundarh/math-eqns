import tkinter as tk
from tkinter import *
from tkinter import OptionMenu
import mymath
from tkinter import ttk
from threading import *

#MAIN STUFF
areachoice = ["Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder"]
volumechoice = ["Sphere","Cone","Cubiod","Sphere"]
master = tk.Tk()
master.title("My Math")
var = StringVar(master)

#ADDING TABS
tabs = ttk.Notebook(master)
area = ttk.Frame(tabs)
volume = ttk.Frame(tabs)
tabs.add(area,text="Area")
tabs.add(volume,text="Volume")

#ALL THE DIFFERENT AREAS
square_entry = Entry(area,textvariable="Side Length a")

#ALL THE BUTTON FUNCTIONS
def areaRender():
 while True:
    if var.get()=="Square":
        square_entry.pack()    

#SETTING UP THE OPTIONS
var.set("Circle")
options = OptionMenu(area,var,"Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder")
options.pack()

#FINAL PACKS 
tabs.pack(expand=1, fill="both")
master.mainloop()