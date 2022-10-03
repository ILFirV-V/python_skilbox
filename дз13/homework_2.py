#2

def max_3(number_1, number_2, number_3):
    return max(max(number_1, number_2), max(number_2, number_3))


number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
number_3 = float(input("Введите третье число: "))

print(max_3(number_1, number_2, number_3))