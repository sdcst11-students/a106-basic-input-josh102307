#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

from math import pi
r = input("radius:")
r = int(r)
v=4.0/3.0*pi* r**3
print(f"the volume of the circle with a radius of {r} is {v}")