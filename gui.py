import tkinter as tk
from tkinter import *
from tkinter import OptionMenu
import mymath
from tkinter import ttk
from threading import *

#MAIN STUFF
areachoice = ["Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder"]
volumechoice = ["Sphere","Cone","Cube","Cuboid","Sphere"]
master = tk.Tk()
master.title("My Math")
var = StringVar(master)
varVol = StringVar(master)

#ADDING TABS
tabs = ttk.Notebook(master)
area = ttk.Frame(tabs)
volume = ttk.Frame(tabs)
tabs.add(area,text="Area")
tabs.add(volume,text="Volume")

#LABELS FOR AREA
a_area_Label = Label(area,text="Enter Side Length:")
b_area_Label = Label(area,text="Enter Breadth:")
h_area_Label = Label(area,text="Enter Height:")
l_area_Label = Label(area,text="Enter Length:")
r_area_Label = Label(area,text="Enter Radius:")
sl_area_Label = Label(area,text="Enter Slant Height:")
final_result_area = Label(area,text="")

#LABELS FOR AREA
a_vol_Label = Label(volume,text="Enter Side Length:")
final_result_vol = Label(volume,text="")

#ALL THE DIFFERENT ENTRIES FOR AREA
square_entry = Entry(area)
circle_entry = Entry(area)
rectangle_entry1 = Entry(area)
rectangle_entry2 = Entry(area)
cuboid_entry1 = Entry(area)
cuboid_entry2 = Entry(area)
cuboid_entry3 = Entry(area)
sphere_entry = Entry(area)
cone_entry1 = Entry(area)
cone_entry2 = Entry(area)
cylinder_entry1 = Entry(area)
cylinder_entry2 = Entry(area)

#ALL THE DIFFERENT ENTRIES FOR VOLUME
cube_entry = Entry(volume)
vcuboid_entry1 = Entry(volume)

def areacalculate():
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
    elif var.get()=="Cone":
        r = int(cone_entry1.get())
        sl = int(cone_entry2.get())
        arearesult(mymath.surface_area_cone(r,sl))
    elif var.get()=="Cylinder":
        r = int(cylinder_entry1.get())
        h = int(cylinder_entry2.get())
        arearesult(mymath.surface_area_cylinder(r,h))
    
def volcalculate():
    if varVol.get()=="Cube":
        a = int(cube_entry.get())
        volresult(mymath.volume_cube(a))

subButtonArea = Button(area,text="Submit",command=areacalculate)
subButtonVol = Button(volume,text="Submit",command=volcalculate)
all_pack_forgets_area = [subButtonArea,final_result_area,a_area_Label,r_area_Label,square_entry,circle_entry,rectangle_entry1,rectangle_entry2,
                    b_area_Label,h_area_Label,l_area_Label,cuboid_entry1,cuboid_entry2,cuboid_entry3,sphere_entry,cone_entry1,
                    cone_entry2,sl_area_Label,cylinder_entry1,cylinder_entry2]
all_entry_delete_area = [square_entry,circle_entry,rectangle_entry1,rectangle_entry2,cuboid_entry1,cuboid_entry2,cuboid_entry3,
                    sphere_entry,cone_entry1,cone_entry2,cylinder_entry1,cylinder_entry2]

all_entry_delete_vol = [cube_entry,vcuboid_entry1]
all_pack_forgets_vol = [a_vol_Label,subButtonVol]

#ALL THE BUTTON FUNCTIONS
def areaRender():
    for i in all_entry_delete_area:
        i.delete(0,"end")
    for i in all_pack_forgets_area:
        i.pack_forget()
    if var.get()=="Square":
        a_area_Label.pack()
        square_entry.pack()   
    elif var.get()=="Circle":
        r_area_Label.pack()
        circle_entry.pack()
    elif var.get()=="Rectangle":
        b_area_Label.pack()
        rectangle_entry1.pack()
        h_area_Label.pack()
        rectangle_entry2.pack()
    elif var.get()=="Cuboid":
        l_area_Label.pack()
        cuboid_entry1.pack()
        b_area_Label.pack()
        cuboid_entry2.pack()
        h_area_Label.pack()
        cuboid_entry3.pack()
    elif var.get()=="Sphere":
        r_area_Label.pack()
        sphere_entry.pack()
    elif var.get()=="Cone":
        r_area_Label.pack()
        cone_entry1.pack()
        sl_area_Label.pack()
        cone_entry2.pack()
    elif var.get()=="Cylinder":
        r_area_Label.pack()
        cylinder_entry1.pack()
        h_area_Label.pack()
        cylinder_entry2.pack()
    subButtonArea.pack()

def volRender():
    for i in all_entry_delete_vol:
        i.delete(0,"end")
    for i in all_pack_forgets_vol:
        i.pack_forget()
    if varVol.get()=="Cube":
        a_vol_Label.pack()
        cube_entry.pack()
    subButtonVol.pack()

def arearesult(a):
    final_result_area.config(text="Area="+str(a))
    final_result_area.pack()

def volresult(a):
    final_result_vol.config(text="Volume="+str(a))
    final_result_vol.pack()

#SETTING UP THE OPTIONS FOR AREA
var.set("Circle")
areaoptions = OptionMenu(area,var,"Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder")
areaoptions.pack()

goButtonArea = Button(area,text="Go",command=areaRender)
goButtonArea.pack()

#SETTING UP THE OPTIONS FOR VOLUME
varVol.set("Sphere")
voloptions = OptionMenu(volume,varVol,"Sphere","Cube","Cone","Cuboid","Sphere")
voloptions.pack()

goButtonVol = Button(volume,text="Go",command=volRender)
goButtonVol.pack()

#FINAL PACKS 
tabs.pack(expand=1, fill="both")
master.mainloop()