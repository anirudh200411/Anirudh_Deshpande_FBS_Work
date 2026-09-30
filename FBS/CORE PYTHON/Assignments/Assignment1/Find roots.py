import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b * b - 4 * a * c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    root = -b / (2 * a)
    print("Both roots are equal =", root)

else:
    print("Roots are imaginary")