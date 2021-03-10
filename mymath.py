'''Basic Area and Volume functions.
Main Functions are:
area_rectangle()        -> arguments = breadth, height ; return = area of the rectangle. \n
area_circle()           -> arguments = radius; return = area of the circle.
area_square()           -> arguments = side; return = area of the square.
surface_area_cuboid()   -> arguments = length,breadth,height; return = total surface area of the cuboid.
surface_area_sphere()   -> arguments = radius; return = total surface area of the sphere.
'''


pi = 3.1415926535
def area_rectangle(b=0,h=0):
    '''Returns Area of Rectangle, breadth as first argument, height as the second argument.
    '''
    return b*h

def area_circle(r=0):
    '''Returns Area of Circle, takes only 1 argument, radius.
    '''
    return pi*r*r

def area_square(a=0):
    '''Returns Area of Square, takes only 1 argument, side.
    '''
    return a**2

def volume_cuboid(l=0,b=0,h=0):
    '''Returns Volume of Cuboid, length as first argument, breadth as the second argument, height as the third argument.
    '''
    return l*b*h

def volume_cube(a):
    '''Returns Volume of Cube, takes only 1 argument, side length.
    '''
    return a**3

def surface_area_cuboid(l=0,b=0,h=0):
    '''Returns Total surface area of cuboid, lenght as first argument, breadth as second argument, height as the third argument.
    '''
    return 2 * (l*b + b*h + h*l)

def volume_sphere(r=0):
    '''Returns Volume of Sphere, takes only 1 argument, radius.
    '''
    return 4/3 * pi * r**3

def surface_area_sphere(r=0):
    '''Returns Surface area of sphere, takes only 1 argument, radius.
    '''
    return 4*pi*r**2

def volume_cylinder(r=0,h=0):
    '''Returns Volume of cylinder, radius as first argument, height as the second argument.
    '''
    return pi * (r**2) * h 

def volume_cone(r,h):
    '''Returns volume of a cone, radius as first argument and height as the second argument.
    '''
    return (pi * (r**2) * h)/3

def surface_area_cone(r,l):
    '''Returns surface area of a cone, radius as first argument and slant height as the second argument.
    '''
    return pi*r*(r+l)

def surface_area_cylinder(r,h):
    '''Returns surface area of a cylinder, radius as first argument and height as the second argument.
    '''
    return 2*pi*r*h
