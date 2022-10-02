#10

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))
if first_number > second_number and first_number > third_number:
    print("число", first_number, "больше")
elif second_number > first_number and second_number > third_number:
    print("число", second_number, "больше")
else:
    print("число", third_number, "больше")