#1

# experience = int(input("Введите количество опыта: "))
# level = 1
# if experience >= 1000:
#     level = 2
# elif experience >= 2500:
#     level = 3
# elif experience >= 5000:
#     level = 4
# print(level)

#2

# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))
# third_number = int(input("Введите третье число: "))
# if first_number > second_number and first_number > third_number:
#    print("число", first_number, "больше")
# elif second_number > first_number and second_number > third_number:
#    print("число", second_number, "больше")
# else:
#    print("число", third_number, "больше")

#3

# X = int(input("Введите x: "))
# if X > 0:
#     print(X - 12)
# elif X == 0:
#     print(5)
# elif X < 0:
#     print(X*X)

#4

# place = int(input("Введите место в списке поступающих: "))
# mark = int(input("Введите количество баллов за экзамены: "))
# if place <= 10:
#     print("Поздравляем, вы поступили!")
#     if mark >= 290:
#         print("Бонусом вам будет начисляться стипендия.")
#     else:
#         print("Но вам не хватило баллов для стипендии.")
# else:
#     print("К сожалению, вы не поступили.")

#5

# rating = int(input('Что получил по математике? '))
# if rating == 2 or rating == 3:
#     print('Плохо. Марш учиться!')
# if rating == 4 or rating == 5:
#     print('Молодец! Можешь отдохнуть.')

#6

# number = input("Введите двузначное число: ")
# if len(number) == 3 and number[0] == '-' or len(number) == 2 and number[0] != '-':
#     print("true")
# else:
#     print("false")

#7

# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))
# third_number = int(input("Введите третье число: "))
#
# if first_number == second_number and first_number == third_number:
#     print(3)
# elif first_number == second_number:
#     print(2)
# elif first_number == third_number:
#     print(2)
# elif second_number == third_number:
#     print(2)
# else:
#     print(0)

#8

# price = int(input("цена: "))
# square = int(input("площадь: "))
# if square >= 100 and price <= 10000000 or square >= 80 and price <= 7000000:
#     print("true")
# else:
#     print("false")

#9

# income = int(input("Доход: "))
# first_level_tax, second_level_tax, third_level_tax = 0, 0, 0
# if income > 50000:
#     third_level_tax = income - 50000
#     second_level_tax = 40000
#     first_level_tax = 10000
# elif income > 10000:
#     second_level_tax = income - 10000
#     first_level_tax = 10000
# else:
#     first_level_tax = income
# print("Налог:", 30/100 * third_level_tax + 20/100 * second_level_tax + 13/100 * first_level_tax)

#10

time = int(input("Время: "))
if 8 < time < 22 and time != 14 and time != 15 and time != 10 and time != 18:
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")