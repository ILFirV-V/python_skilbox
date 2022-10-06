#3
import random


first_list = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
second_list = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
print("Первая команда:", first_list)
print("Вторая команда:", second_list)
print("Победители тура:", [max(first_list[i], second_list[i]) for i in range(20)])