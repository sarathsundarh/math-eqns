import tkinter as tk
from tkinter import *
from tkinter import OptionMenu
import mymath
from tkinter import ttk
from threading import *
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont



#MAIN STUFF
areachoice = ["Circle","Square","Rectangle","Cuboid","Sphere","Cone","Cylinder"]
volumechoice = ["Sphere","Cone","Cube","Cuboid","Sphere"]
master = tk.Tk()
master.title("My Math")
var = StringVar(master)
varVol = StringVar(master)
canSq = tk.Canvas(master,width=300,height=300)
canCi = tk.Canvas(master)

sqLabel = tk.Label(master,text="Formula=s x s")
ciLabel = tk.Label(master,text="Formula=𝝅 x r x r")

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

#LABELS FOR VOLUME
a_vol_Label = Label(volume,text="Enter Side Length:")
r_vol_Label = Label(volume,text="Enter Radius:")
final_result_vol = Label(volume,text="")
l_vol_Label = Label(volume,text="Enter Length:")
b_vol_Label = Label(volume,text="Enter Breadth:")
h_vol_Label = Label(volume,text="Enter Height:")

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
vcuboid_entry2 = Entry(volume)
vcuboid_entry3 = Entry(volume)
vsphere_entry = Entry(volume)
vcone_entry1 = Entry(volume)
vcone_entry2 = Entry(volume)
vcylinder_entry1 = Entry(volume)
vcylinder_entry2 = Entry(volume)

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvasName.create_oval(x0, y0, x1, y1)

def areacalculate():
    if var.get()=="Square":
        a = int(square_entry.get())
        arearesult(mymath.area_square(a))
        canSq.create_rectangle(30, 30, 270, 270,outline="#fb0", fill="#fb0")
        canSq.pack()
        sqLabel.pack()
    elif var.get()=="Circle":
        r = int(circle_entry.get())
        arearesult(mymath.area_circle(r))
        create_circle(150,150,5,canCi)
        canCi.pack()
        #canCi.create_oval(150,)
        ciLabel.pack()
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
    elif varVol.get()=="Sphere":
        r = int(vsphere_entry.get())
        volresult(mymath.volume_sphere(r))
    elif varVol.get()=="Cuboid":
        l = int(vcuboid_entry1.get())
        b = int(vcuboid_entry2.get())
        h = int(vcuboid_entry3.get())
        volresult(mymath.volume_cuboid(l,b,h))
    elif varVol.get()=="Cone":
        r = int(vcone_entry1.get())
        h = int(vcone_entry2.get())
        volresult(mymath.volume_cone(r,h))
    elif varVol.get()=="Cylinder":
        r = int(vcylinder_entry1.get())
        h = int(vcylinder_entry2.get())
        volresult(mymath.volume_cylinder(r,h))

can = tk.Canvas()
subButtonArea = Button(area,text="Submit",command=areacalculate)
subButtonVol = Button(volume,text="Submit",command=volcalculate)
all_pack_forgets_area = [subButtonArea,final_result_area,a_area_Label,r_area_Label,square_entry,circle_entry,rectangle_entry1,rectangle_entry2,
                    b_area_Label,h_area_Label,l_area_Label,cuboid_entry1,cuboid_entry2,cuboid_entry3,sphere_entry,cone_entry1,canSq,canCi,
                    cone_entry2,sl_area_Label,cylinder_entry1,cylinder_entry2,ciLabel,sqLabel]
all_entry_delete_area = [square_entry,circle_entry,rectangle_entry1,rectangle_entry2,cuboid_entry1,cuboid_entry2,cuboid_entry3,
                    sphere_entry,cone_entry1,cone_entry2,cylinder_entry1,cylinder_entry2]

all_entry_delete_vol = [cube_entry,vsphere_entry,vcuboid_entry1,vcuboid_entry2,vcuboid_entry3,vcone_entry1,vcone_entry2,vcylinder_entry1,vcylinder_entry2]
all_pack_forgets_vol = [cube_entry,a_vol_Label,final_result_vol,subButtonVol,r_vol_Label,l_vol_Label,b_vol_Label,h_vol_Label,vcone_entry1,vcone_entry2,vsphere_entry,
                        vcuboid_entry1,vcuboid_entry2,vcuboid_entry3,vcylinder_entry1,vcylinder_entry2]

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
    elif varVol.get()=="Sphere":
        r_vol_Label.pack()
        vsphere_entry.pack()
    elif varVol.get()=="Cuboid":
        l_vol_Label.pack()
        vcuboid_entry1.pack()
        b_vol_Label.pack()
        vcuboid_entry2.pack()
        h_vol_Label.pack()
        vcuboid_entry3.pack()
    elif varVol.get()=="Cone":
        r_vol_Label.pack()
        vcone_entry1.pack()
        h_vol_Label.pack()
        vcone_entry2.pack()
    elif varVol.get()=="Cylinder":
        r_vol_Label.pack()
        vcylinder_entry1.pack()
        h_vol_Label.pack()
        vcylinder_entry2.pack()
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
voloptions = OptionMenu(volume,varVol,"Sphere","Cube","Cone","Cuboid","Cylinder")
voloptions.pack()

goButtonVol = Button(volume,text="Go",command=volRender)
goButtonVol.pack()

#FINAL PACKS 
tabs.pack(expand=1, fill="both")
master.mainloop()