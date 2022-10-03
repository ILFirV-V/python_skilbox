#5

def count_letters(text, k, n):
    count_number = 0
    count_string = 0
    for i in text:
        if i == k:
            count_string += 1
        if i == str(n):
            count_number += 1
    print(f"Количество цифр {n}: {count_number} \nКоличество букв {k}: {count_string}")

text = input("Введите текст: ")
number = input("Какую цифру ищем? ")
string = input("Какую букву ищем? ")
count_letters(text, string, number)
