# 1

# reserve = 100
# months = 0
# for i in range(reserve, -1, -4):
#     months += 1
#     print(f"Прошло месяцев: {months}. Осталось гречки: {i}")

# 2

# count = int(input("Введите количество должников: "))
# sum_credit = 0
# for i in range(0, count + 1, 5):
#     print("Должник с номером", i)
#     sum_credit += int(input("Сколько должны? "))
# print("Общая сумма долга:", sum_credit)

#3

# reverse_timer = int(input("сколько разогреваться?"))
# for i in range(reverse_timer - 1, -1, -1):
#     ready = True if input("хотите забрать еду?") == "1" else False
#     if ready:
#         print("Ваша еда готова, можете забрать")
#         break
#     if i == 0:
#         print("Ваша еда готова, осторожно горячo!")

#4

# start = int(input("Введите число: "))
# end = int(input("Введите число: "))
# step = int(input("Введите число: "))
# start_number = start
# while start_number % step != 0:
#     start_number += 1
# sum_numbers = 0
# for i in range(start_number, end + 1, step):
#     sum_numbers += i
# print(sum_numbers)

#5

# start = int(input("Введите начало отрезка: "))
# end = int(input("Введите конец отрезка: "))
# step = int(input("Введите шаг: "))
# for x in range(end, start - 1, step):
#     print(f"В точке {x} функция равна {x**3 + 2 * x**2 - 4 * x + 1}")

#6

# envelope = 12
# letter = int(input("размер письма: "))
# result = 0
# while letter > envelope:
#     result += 2
#     letter /= 2
# print("сложи", result)

#7

# educational_grant = int(input("Введите стипендию: "))
# expenses = int(input("Введите расходы на проживание: "))
# sum_expenses = 0
# sum_educational_grants = 0
# for i in range(0, 10):
#     sum_expenses += expenses
#     sum_educational_grants += educational_grant
#     expenses += expenses * 3 / 100
# print("У родителей необходимо попросить", "%.3f" % (sum_expenses - sum_educational_grants))

#8

# n = int(input("Введите n: "))
# s = 0
# for i in range(0, n + 1):
#     s += ((-1)**i) * (1/(2**i))
# print(s)

#9

# x = int(input("Введите x: "))
# numerator = 1
# denominator = 1
# for i in range(1, 7):
#     degree_two = 2**i
#     numerator *= (x - (degree_two - 1))
#     denominator *= (x - degree_two)
# print(numerator / denominator)

#10

x = int(input("Введите количество мальчиков: "))
y = int(input("Введите количество девочек: "))
q = abs(x - y)
result = ""
if (y > 2 * x) or (x > 2 * y):
    print("нет решения")
elif x > y:
    result += "BGB" * q + "BG" * (y - q)
else:
    result += "GBG" * q + "GB" * (x - q)
print(result)
