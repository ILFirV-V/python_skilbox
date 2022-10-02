#9

number = int(input("Введите число: "))
reverse_number = int(str(number % 10) + str((number % 100) // 10) + str((number % 1000) // 100) + str(number // 1000))
print(reverse_number)