import tkinter as tk
import mymath
from tkinter import ttk

areachoice = ["Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder"]
volumechoice = ["Sphere","Cone","Cubiod","Sphere"]

master = tk.Tk()
master.title("My Math")

tabs = ttk.Notebook(master)
area = ttk.Frame(tabs)
volume = ttk.Frame(tabs)

tabs.add(area,text="Area")
tabs.add(volume,text="Volume")



tabs.pack(expand=1, fill="both")
master.mainloop()