'''
Module add.py functions
def cube(c,e,RGB): # c = center, e = edge width
def cube2(c,e,b,RGB): # c = center, b = border width, e = edge width
def parametric(S,min_u,max_u,grid_u,min_v,max_v,grid_v,RGB): # S - parametric uv surface, grid - detail, RGB - color
def sphere(c,r,k,RGB): # c - center, r - radius, k - detail, RGB - color
def cylinder(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
def cylinder2(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
def cylinder3(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
def cone(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
def cone2(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
def off(mesh): # mesh - off file
'''
import add
import math

# Define the dimensions and color of the skateboard deck
deck_length = 20
deck_width = 10  # Increase the width
deck_height = 1
deck_color = [139, 69, 19]  # Brown

# Define the center of the skateboard deck
deck_center = [0, 0, 0]

# Create the skateboard deck
for i in range(-deck_length//2, deck_length//2):
    for j in range(-deck_width//2, deck_width//2):
        # Adjust the z-coordinate to create a curve
        z = deck_center[2] + (i / deck_length) ** 2
        # Swap the y and z coordinates
        add.cube([deck_center[0] + i, z, deck_center[2] + j], deck_height, deck_color)

# Write the model to an OFF file
add.off('modelis.off')