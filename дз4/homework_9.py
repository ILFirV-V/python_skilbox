#9

mileage = input("Введите пробег: ")
date = int(input("Введите сегодняшнее число: "))
sum = 0
for i in mileage:
    sum += int(i)
if sum > date:
    print("Сброс.")
    print("Пробег: 0")
else:
    print("Сегодня не сломался.")
    print("Пробег:", mileage)