#6
import random


n = int(input("Количество чисел в списке: "))
list_numbers = [random.randint(0, 2) for _ in range(n)]
print("Список до сжатия:", list_numbers)
new_list_numbers = [i for i in list_numbers if i != 0]
add_new_list_numbers = [0 for _ in range(len(list_numbers) - len(new_list_numbers))]
print("Список после сжатия:", new_list_numbers)