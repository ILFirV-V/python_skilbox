#1

# numbers = [114, 12, 14, 10605, 4907, 450]
# for i in numbers:
#     if i % 2 == 0 and i % 3 != 0:
#         print("Число подходит")
#     else:
#         print("Число не подходит")

#2


# result = 0
# for i in range(0, 10):
#     number = int(input("номер: "))
#     result += 1 if (number % 2 == 0 and number > 0) else 0
# print(result)

#3

# amount_salaries = 0
# for i in range(0, 12):
#     i += 1
#     amount_salaries += int(input(f"зарплата за {i} месяц: "))
# print("средняя зарплата: ", amount_salaries / 12)

#4

# result = 0
# for i in range(30, 36):
#     if int(input(f"Людей в {i}-м секторе: ")) <= 10:
#         print("Всё спокойно.")
#     else:
#         print("Нарушение! Слишком много людей в секторе!")
#         result += 1
# print("Количество нарушений: ", result)

#5

# number = int(input("Введите число: "))
# result = 1
# for i in range(1, number + 1):
#     result *= i
# print(f"Факториал числа {number} равен {result}")

#6

# count = int(input("количество учеников: "))
# number_student_grades = {
#   "3": 0,
#   "4": 0,
#   "5": 0
# }
# for i in range(1, count + 1):
#     grade = input(f"оценка {i} ученика: ")
#     number_student_grades[grade] += 1
# print("больше всего учеников с оценкой", max(number_student_grades.keys(), key=number_student_grades.get))

#7

# a = int(input("первое число: "))
# b = int(input("второе число: "))
# numbers = []
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         numbers.append(i)
# print("среднее арифметическое:", sum(numbers) / len(numbers))

#8

# for i in range(10, 100):
#     if ((i//10) * (i%10) * 3) == i:
#         print("подходящее число", i)

#9
#
# isIncreases = True
# previous_salary = 0
# for i in range(0, 10):
#     i += 1
#     salary = int(input(f"зарплата за {i} месяц: "))
#     if previous_salary > salary:
#         isIncreases = False
#     previous_salary = salary
# print("зарплата возрастает:", isIncreases)

#10

# n = int(input("Введите количество карточек: "))
# amount_cards = 0
# should_amount_cards = n
# for i in range(1, n):
#     should_amount_cards += i
#     amount_cards += int(input("Введите номер оставшейся карточки: "))
# print("Номер пропавшей карточки:", should_amount_cards - amount_cards)
