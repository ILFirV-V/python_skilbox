def sum_digits(number):
    sum_number = 0
    for i in str(number):
        sum_number += int(i)
    return sum_number


def max_number(number):
    max_num = 0
    for i in str(abs(number)):
        if int(i) > max_num:
            max_num = int(i)
    return max_num


def min_number(number):
    min_num = 100000
    for i in str(abs(number)):
        if int(i) < min_num:
            min_num = int(i)
    print(min_num)
    return min_num


def change_number():
    return int(input("Введите новое число: "))


def get_action():
    print("Menu: \n S - получить сумму цифр числа \n M - получить максимальную цифру \n m - получить минимальную цифру \
          \n C - поменять число \n E - выход")
    return input("Введите действие: ")


number = int(input("Введите число: "))
while True:
    if number == 0:
        break
    action = get_action()
    if action == "S":
        print("сумма цифр числа:", sum_digits(number))
    elif action == "M":
        print("максимальная цифра :", max_number(number))
    elif action == "m":
        print("минимальная цифра :", min_number(number))
    elif action == "C":
        number = change_number();
    elif action == "E":
        print("Выход")
        break
