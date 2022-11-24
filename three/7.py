#  Using Heron's formula to calculate the area of a triangle

import math

a = input("Input value of side a: ")
b = input("Input value of side b: ")
c = input("Input value of side c: ")

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area of triangle is {area}")