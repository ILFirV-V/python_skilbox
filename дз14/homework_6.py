#6
import math


def check_coordinate(x, y, r):
    return math.sqrt(x * x + y * y) < r


print("Введите координаты монетки: ")
coordinate_x = float(input("X: "))
coordinate_y = float(input("Y: "))
area = int(input("Введите радиус: "))
text = "Монетка где-то рядом" if check_coordinate(coordinate_x, coordinate_y, area) else "Монетки в области нет"
print(text)
