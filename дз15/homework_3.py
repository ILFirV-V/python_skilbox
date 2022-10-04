#3

n = int(input("Количество клеток: "))
cell_array = []
for i in range(n):
    cell_array.append(int(input(f"Введите эффективность {i + 1} клетки: ")))
print("Весь массив клеток:", cell_array)

invalid_values = ""

for i in range(n):
    print(f"Ранг {i + 1} клетки: {i}. Эффективность {i + 1} клетки: {cell_array[i]}. ")
    if cell_array[i] < i:
        invalid_values += f"{cell_array[i]} "
print("Неподходящие значения:", invalid_values)