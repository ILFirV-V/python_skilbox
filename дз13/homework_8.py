#8

def get_factorial_number(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


def get_degree_number(x, count):
    result_number = 1
    for i in range(1, count + 1):
        result_number = result_number * x
    return result_number


precision = float(input("Введите точность: "))
x = int(input("Введите x: "))
ceil = 1
result = 0
n = 0

while abs(ceil) > precision:
    ceil = get_degree_number(-1, n) * (get_degree_number(x, 2 * n) / get_factorial_number(2 * n))
    result += ceil
    n += 1
print("Сумма ряда =", result)
