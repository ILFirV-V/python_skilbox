#6

def add_number_in_list(name_list, count):
    list_numbers = []
    for i in range(count):
        list_numbers.append(int(input(f"Введите {i + 1}-е число для {name_list} списка: ")))
    return list_numbers


first_list = add_number_in_list("первого", 3)
second_list = add_number_in_list("первого", 7)
print("Первый список:", first_list)
print("Второй список:", second_list)
first_list.extend(second_list)
first_list = list(set(first_list))
print(f"Новый первый список с уникальными элементами: {first_list}")

