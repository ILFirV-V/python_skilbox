list_first = [1, 5, 3]
list_second = [1, 5, 1, 5]
list_third = [1, 3, 1, 5, 3, 3]
list_first.extend(list_second)
count_5 = list_first.count(5)
for i in range(count_5):
    list_first.remove(5)
list_first.extend(list_third)
count_3 = list_first.count(3)
print("Кол-во цифр 5 при первом объединении:", count_5)
print("Кол-во цифр 3 при втором объединении:", count_3)
print("Итоговый список:", list_first)