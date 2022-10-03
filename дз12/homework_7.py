#7
def min_number(a, b):
    # print("Минимальное число:", (a + b - abs(a - b)) // 2)
    print("Минимальное число:", (a < b) * a + (b < a) * b)

a = float(input("первое число: "))
b = float(input("второе число: "))
min_number(a, b)