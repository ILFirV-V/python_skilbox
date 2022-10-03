def sum_number(number):
    number = str(abs(number))
    sum_number = 0
    for i in range(len(number)):
        sum_number += int(number[i])
    return sum_number


def len_number(number):
    return len(str(abs(number)))


number = int(input("Введите число: "))
sum_number = sum_number(number)
print("Сумма чисел:", sum_number)
len_number = len_number(number)
print("Количество цифр в числе:", len_number)
print("Разность суммы и количества цифр:", sum_number - len_number)