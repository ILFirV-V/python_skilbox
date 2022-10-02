#1

# for i in range(0, 6):
#     for j in range(0, 12, 2):
#         print(i + j, end='\t')
#     print()

#2

# n = int(input("Введите число: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(i + 1, end=' ')
#     print()

#3

# x = int(input("Введите ширину: "))
# y = int(input("Введите высоту: "))
#
# for i in range(y):
#     for j in range(x):
#         if j == 0 or j == x - 1:
#             print('|', end='')
#         elif i == 0 or i == y - 1:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()

#4

# x = 6
# y = 6
#
# for i in range(y):
#     for j in range(x):
#         if j == i or (j + i + 1) == x:
#             print("^", end='')
#         else:
#             print(' ', end='')
#     print()

#5

# count = int(input("Введите кол-во чисел: "))
# result_sum = 0
# for i in range(count):
#     number = int(input("Введите число: "))
#     for j in range(2, number // 2 + 1):
#         if number % j == 0:
#             break
#     else:
#         result_sum += 1
# print(result_sum)

#6

# n = int(input("число N: "))
# result_sum = 0
# for i in range(1, n + 1):
#     result_multiplication = 1
#     for j in range(1, i + 1):
#         result_multiplication *= j
#     result_sum += result_multiplication
# print("сумма факториалов:", result_sum)

#7

# n = int(input("число N: "))
# max_sum_number = 0
# result_number = 0
# for i in range(n):
#     number = input("Введите число: ")
#     sum_number = 0
#     for j in number:
#         sum_number += int(j)
#     if max_sum_number < sum_number:
#         max_sum_number = sum_number
#         result_number = number
# print("Число:", result_number, "Суммуа его цифр:", max_sum_number)

#8

# pyramid_height = int(input("Высота пирамиды: "))
# count = 1 + (pyramid_height - 1) * 2
# for i in range(pyramid_height):
#     for j in range(count):
#         if (count // 2) - i <= j <= (count // 2) + i:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()

#9

# pyramid_height = int(input("Высота пирамиды: "))
# number = 1
# for i in range(pyramid_height):
#     print(end = "   " * (pyramid_height - i - 1))
#     for j in range(i + 1):
#         print(number, end = "    ")
#         number += 2
#     print()

#10

height = int(input("Глубина: "))
width = height * 2
for i in range(height):
    for j in range(width // 2, 0, -1):
        if j < height - i:
            print(".", end = "")
        else:
            print(j, end = "")
    for j in range(1, width // 2 + 1):
        if j < height - i:
            print(".", end = "")
        else:
            print(j, end = "")
    print()