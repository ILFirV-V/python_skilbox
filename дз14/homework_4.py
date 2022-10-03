#4

def get_reverse_number(number):
    number = str(number)
    new_number = ""
    for i in range(len(number)-1, -1, -1):
        if new_number != "" or number[i] != "0":
            new_number += number[i]
    return new_number


number_1 = input("Введите первое число: ").split(".")
number_2 = input("Введите второе число: ").split(".")
reverse_number_1 = get_reverse_number(number_1[0]) + "." + get_reverse_number(number_1[1])
reverse_number_2 = get_reverse_number(number_2[0]) + "." + get_reverse_number(number_2[1])
print(f"Первое число наоборот: {reverse_number_1} \nВторое число наоборот: {reverse_number_2}")
sum_numbers = float(reverse_number_1) + float(reverse_number_2)
print(f"Сумма: {sum_numbers}")