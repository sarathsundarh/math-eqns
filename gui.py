import tkinter as tk
from tkinter import *
from tkinter import OptionMenu
import mymath
from tkinter import ttk


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

#SETTING UP THE OPTIONS
var.set("Circle")
options = OptionMenu(area,var,"Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder")
options.pack()
subButton = Button(area,text="Submit",command = render)
subButton.pack()



#FINAL PACKS 
tabs.pack(expand=1, fill="both")
master.mainloop()