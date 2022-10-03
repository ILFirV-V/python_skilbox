#7

print("Введите местоположение коня: ")
x = int(float(input("x: ")) * 10) % 10
y = int(float(input("y: ")) * 10) % 10
print("Введите местоположение точки на доске: ")
x_point = int(float(input("x: ")) * 10) % 10
y_point = int(float(input("y: ")) * 10) % 10
print(f"Конь в клетке ({x}, {y}). Точка в клетке ({x_point}, {y_point}).")
if abs(x - x_point) == 2 and abs(y - y_point) == 1 or abs(x - x_point) == 1 and abs(y - y_point) == 2:
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")