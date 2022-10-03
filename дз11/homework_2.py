#2

import math

count = int(input("Введите кол-во чисел: "))
for i in range(count):
    number = float(input("Введите число: "))
    number = math.ceil(number) if number >= 0.0 else math.floor(number)
    print(f"x = {number}", f"log(x) = {math.log(number)}" if number >= 0.0 else f"exp(x) = {math.exp(number)}")


