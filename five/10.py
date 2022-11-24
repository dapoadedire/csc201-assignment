# Solve quardratic equation

import math

def solve(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("No real solutions")
    elif d == 0:
        x = -b / (2*a)
        print("One solution:", x)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Two solutions:", x1, x2)

def main():
    print("This program finds the real solutions to a quadratic equation")
    print("ax^2 + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    solve(a, b, c)

main()