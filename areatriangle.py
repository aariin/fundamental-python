"""
program to count area of a triangle
"""
base = 10
height = 6
area_triangle = base * height/2
print(f'a triangle with base ={base} and height = {height} has area {area_triangle}')

" we will create function using def my_function(fname)"
def areatriangle(base, height):
    areatriangle = base * height/2
    return areatriangle

print(f' The area of triangle using function, is = {areatriangle(30,10)}')
"""
make a package:
right click: new python package
name: geometric
there is a new file called __init__.py, the different between usual directory 
and package directory is, package directory has __init__.py file.
- Make a new file under geometric directory (new- python file, using lowcase)
- copy function

- make new file under project, let's say main.py to call package

"""

"""
from geometric.triangle import areatriangle 
"or"

import
"""
