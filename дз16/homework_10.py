#10

count = int(input("Кол-во чисел: "))
numbers = []
add_numbers = []
for i in range(count):
    numbers.append(int(input("Число: ")))
print("Последовательность:", numbers)
result_count = 0
while numbers != numbers[::-1]:
    numbers.insert(count, numbers[result_count])
    add_numbers.append(numbers[result_count])
    result_count += 1
print("Нужно приписать чисел:", result_count)
print("Сами числа:", add_numbers)