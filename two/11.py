#  length of a parabola segment

from math import sqrt, log
b = float(input("Input base: "))
h = float(input("Input height: "))
l = float(input("Input length: "))


L = sqrt(4*h**2 + b**2) + (sqrt(b)/2*h) * log((2*h + sqrt(4*h**2 + b**2))/b) 
# log in python
