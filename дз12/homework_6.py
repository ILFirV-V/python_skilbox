#6

def check_coordinate(x, y):
    is_beside = False
    if abs(x) <= 1 and abs(y) <= 1:
        is_beside = True
    return is_beside

x = float(input("x: "))
y = float(input("y: "))
if check_coordinate(x, y):
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")
