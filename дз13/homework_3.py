#3

def get_reverse_number(number):
    number = str(number)
    new_number = ""
    for i in range(len(number)-1, -1, -1):
        if new_number != "" or number[i] != "0":
            new_number += number[i]
    return new_number


number_1 = input("Введите первое число: ")
number_2 = input("Введите второе число: ")
reverse_number_1 = get_reverse_number(number_1)
reverse_number_2 = get_reverse_number(number_2)
print(f"Первое число наоборот: {reverse_number_1} \nВторое число наоборот: {reverse_number_2}")
sum_numbers = int(reverse_number_1) + int(reverse_number_2)
print(f"Сумма: {sum_numbers} \nСумма наоборот:{get_reverse_number(sum_numbers)}")
