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

#LABELS
a_area_Label = Label(area,text="Enter Side Length:")
b_area_Label = Label(area,text="Enter Breadth:")
h_area_Label = Label(area,text="Enter Height:")
l_area_Label = Label(area,text="Enter Length:")
r_area_Label = Label(area,text="Enter Radius:")
final_result = Label(area,text="")

#ALL THE DIFFERENT AREAS
square_entry = Entry(area)
circle_entry = Entry(area)
rectangle_entry1 = Entry(area)
rectangle_entry2 = Entry(area)
cuboid_entry1 = Entry(area)
cuboid_entry2 = Entry(area)
cuboid_entry3 = Entry(area)
sphere_entry = Entry(area)

def calculate():
    if var.get()=="Square":
        a = int(square_entry.get())
        arearesult(mymath.area_square(a))
    elif var.get()=="Circle":
        r = int(circle_entry.get())
        arearesult(mymath.area_circle(r))
    elif var.get()=="Rectangle":
        b = int(rectangle_entry1.get())
        h = int(rectangle_entry2.get())
        arearesult(mymath.area_rectangle(b,h))
    elif var.get()=="Cuboid":
        l = int(cuboid_entry1.get())
        b = int(cuboid_entry2.get())
        h = int(cuboid_entry3.get())
        arearesult(mymath.surface_area_cuboid(l,b,h))
    elif var.get()=="Sphere":
        r = int(sphere_entry.get())
        arearesult(mymath.surface_area_sphere(r))

subButton = Button(area,text="Submit",command=calculate)
all_pack_forgets = [subButton,final_result,a_area_Label,r_area_Label,square_entry,circle_entry,rectangle_entry1,rectangle_entry2,
                    b_area_Label,h_area_Label,l_area_Label,cuboid_entry1,cuboid_entry2,cuboid_entry3,sphere_entry]

#ALL THE BUTTON FUNCTIONS
def areaRender():
    for i in all_pack_forgets:
        i.pack_forget()
    if var.get()=="Square":
        a_area_Label.pack()
        square_entry.pack()   
        subButton.pack() 
    elif var.get()=="Circle":
        r_area_Label.pack()
        circle_entry.pack()
        subButton.pack()
    elif var.get()=="Rectangle":
        b_area_Label.pack()
        rectangle_entry1.pack()
        h_area_Label.pack()
        rectangle_entry2.pack()
        subButton.pack()
    elif var.get()=="Cuboid":
        l_area_Label.pack()
        cuboid_entry1.pack()
        b_area_Label.pack()
        cuboid_entry2.pack()
        h_area_Label.pack()
        cuboid_entry3.pack()
        subButton.pack()
    elif var.get()=="Sphere":
        r_area_Label.pack()
        sphere_entry.pack()
        subButton.pack()

def arearesult(a):
    final_result.config(text="Area="+str(a))
    final_result.pack()



#SETTING UP THE OPTIONS
var.set("Circle")
options = OptionMenu(area,var,"Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder")
options.pack()

goButton = Button(area,text="Go",command=areaRender)
goButton.pack()



#FINAL PACKS 
tabs.pack(expand=1, fill="both")
master.mainloop()