#1

# dayWeek = input("Введите день недели: ")
# day = 0
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# for i in days:
#     day += 1
#     if dayWeek == i:
#         print("Номер дня недели:", day)

#2

# result = 0
#
# for i in range(10):
#     result += 1 if input("крикнет слово: ") == "Карамба" else 0
# print(result)

#3

# text = input("Введите текст: ")
# result = 0
# count = 0
# for i in range(0, len(text)):
#     if text[i] == '*':
#         result = i + 1
#         count += 1
# if count == 1:
#     print("Символ ‘*’ стоит на позиции ", result)

#4

# ranks = int(input("рядов: "))
# seat = int(input("сидений: "))
# meters = int(input("метров между рядами: "))
# print("/n", "Сцена", "/n")
#
# for i in range(ranks):
#     print("=" * seat, "*" * meters, "=" * seat)

#5

# class Point:
#     x = 6
#     y = 19
#
# while True:
#     moving = input(f"Марсоход находится на позиции {Point.x}, {Point.y}, введите команду:")
#     Point.y += 1 if (moving.lower() == "w".lower() and Point.y < 20) \
#         else -1 if (moving.lower() == "s".lower() and Point.y > 0) else 0
#     Point.x += 1 if (moving.lower() == "d".lower() and Point.x < 15) \
#         else -1 if (moving.lower() == "a".lower() and Point.y > 0) else 0

#6

# cipher = input("Введите строку: ")
# maxS = 0
# temporaryBox = 0
# for i in cipher:
#     if i == "s":
#         temporaryBox += 1
#     elif temporaryBox > maxS:
#         maxS = temporaryBox
#         temporaryBox = 0
#
# print("Самая длинная последовательность:", maxS)

#7

# text = input("Введите текст: ")
# max_word = 0
# temporary_box = 0
# for i in text:
#     if i != " ":
#         temporary_box += 1
#     elif max_word < temporary_box:
#         max_word = temporary_box
#         temporary_box = 0
# print("Самое длинное слово, букв:", max_word)

#8

# footer_length = int(input("длина колонтитула: "))
# exclamation_length = int(input("количество восклицательных знаков: "))
# footer_length_1 = (footer_length - exclamation_length) / 2
# footer_length_2 = 0
# if footer_length_1.is_integer():
#     footer_length_1 = int(footer_length_1)
#     footer_length_2 = footer_length_1
# else:
#     footer_length_1 = (footer_length - exclamation_length) // 2
#     footer_length_2 = footer_length_1 + 1
#
# print('~' * footer_length_1 + '!' * exclamation_length + '~' * footer_length_2)

#9

# sum_milk = 0
# for i in range(1, 11):
#     is_free = input(f"Свободно(a) или занято(b) в стойле {i} : ") == "a"
#     if is_free:
#         sum_milk += i * 2
# print(sum_milk)

#10

# message = input("сообщение: ")
# result_1 = ""
# result_2 = ""
# for i in range(len(message)):
#     if i % 2 == 0:
#         result_1 += message[i]
#     else:
#         result_2 = message[i] + result_2
# print(result_1 + result_2)