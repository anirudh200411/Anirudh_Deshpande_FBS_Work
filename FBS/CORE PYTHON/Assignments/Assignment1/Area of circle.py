# Program to find area and circumference of a circle

import math

r = float(input("Enter radius of circle: "))

area = math.pi * r * r
circumference = 2 * math.pi * r

print("Area of circle =", area)
print("Circumference of circle =", circumference)