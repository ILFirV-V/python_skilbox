# 1
# n = int(input("Введите до какого числа идти: "))
# i = 0
# while i != n:
#     i += 1
#     print(i**3)

#2
# name = input("Введите имя должника: ")
# duty = int(input("Введите сумму долга: "))
# print(name, "ваша задолженность составляет", duty, "рублей")
# sum = 0
# while duty > sum:
#     sum = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
#     if duty > sum:
#         print("Маловато,", name,"Давайте ещё раз.")
#     else:
#         print("Отлично,", name, '!', "Вы погасили долг. Спасибо!")

#3
# number = input("Введите число: ")
# print(len(number))

# number = int(input("Введите число: "))
# len = 0
# while number > 0:
#     number //= 10
#     len += 1
# print(len)

#4
# months = 0
# while True:
#     days = int(input())
#     if days == 0:
#         print(months)
#         break
#     if days % 2 == 0:
#         months += 1

#5
#a = int(input())
# i, s1, s2 = 0, 0, 0
# b1 = a // 1000
# b2 = a % 1000
# while i < 6:
#     s1 += b1 % 10
#     s2 += b2 % 10
#     b1 //= 10
#     b2 //= 10
#     i += 1
# print(b2 == b1)

#6
# positive = 0
# negative = 0
# while True:
#     number = input("Введите число: ")
#     if number == "0":
#         print("Кол-во положительных чисел:", positive)
#         print("Кол-во отрицательных чисел:", negative)
#         break
#     if number[0] == '-':
#         negative += 1
#     else:
#         positive += 1

#7
# print("Начался 8-часовой рабочий день")
# go_store = False
# completed_tasks = 0
# i = 0
# while i != 8:
#     i += 1
#     print(i, "-й час")
#     tasks = int(input("Сколько задач решит Максим?"))
#     completed_tasks += tasks
#     answer = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): ")) == 1
#     go_store = True if go_store else answer
# print("Рабочий день закончился. Всего выполнено задач: ", completed_tasks)
# if go_store:
#     print("Нужно зайти в магазин.")

#8

# X = int(input("Вклад в банке: "))
# P = int(input("Ежегодно он увеличивается на (процентов): "))
# Y = int(input("До какой суммы копить: "))
# i = 0
# while X < Y:
#     i += 1
#     X += X * P // 100
# print(i)

# 9

# number = int(input("загадали число: "))
# count = 0
# while True:
#     count += 1
#     entered_number = int(input("Введите число: "))
#     if entered_number > number:
#         print("Число больше, чем нужно. Попробуйте ещё раз!")
#     elif entered_number < number:
#         print("Число меньше, чем нужно. Попробуйте ещё раз!")
#     else:
#         print("Вы угадали! Число попыток:", count)

#10

number = int(input("загадали число: "))
count = 0
low = 0
high = 100
mid = 50
while True:
    count += 1
    mid = (low + high) // 2
    answer = int(input(f"Твоё число равно(1), больше(2) или меньше(3), чем число {mid}?"))
    if answer == 1:
        print("Ваше число", mid, "количество попыток", count)
        break
    elif answer == 2:
        low = mid + 1
    else:
        high = mid - 1


