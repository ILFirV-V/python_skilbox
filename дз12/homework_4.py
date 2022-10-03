# 4
def get_reverse_number(number):
    new_number = ""
    for i in range(len(number)-1, -1, -1):
        if new_number != "" or number[i] != "0":
            new_number += number[i]
    return new_number


while True:
    number = input("Введите число: ")
    if number == "0":
        print("Программа завершена!")
        break
    reverse_number = get_reverse_number(number)
    print("Число наоборот:", reverse_number)