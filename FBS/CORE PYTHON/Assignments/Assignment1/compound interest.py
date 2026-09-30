# Program to calculate Compound Interest

P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time (T): "))
R = float(input("Enter Rate of Interest (R): "))

CI = P * (1 + R / 100) ** T - P

print("Compound Interest =", CI)