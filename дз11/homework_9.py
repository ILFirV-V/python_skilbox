#9
import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a != 0:
    d = b**2 - 4 * a * b
    if d == 0:
        print(f"x = {-b / (2 * a)}")
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1 = {round(min(x1, x2), 2)} , x2 = {round(max(x1, x2), 2)}")