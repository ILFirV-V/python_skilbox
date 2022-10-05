#7

def add_number_in_list(name_object_1, name_object_2, count):
    list_numbers = []
    for i in range(count):
        list_numbers.append(int(input(f"Введите размер {name_object_1} {i + 1}{name_object_2}: ")))
    return list_numbers


count_skates = int(input("Кол-во коньков: "))
list_skates = add_number_in_list("коньков", "-й пары", count_skates)
count_people = int(input("Кол-во людей: "))
list_people = add_number_in_list("ноги", "-го человека", count_people)
count = 0
for i in list_people:
    if i in list_skates:
        count += 1
        list_skates.remove(i)
print("Наибольшее кол-во людей, которые могут взять ролики:", count)