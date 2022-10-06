#8

n = int(input("Количество палок: "))
k = int(input("Количество бросков: "))
sticks = ["|"] * n
for i in range(k):
    left = int(input(f"Бросок {i + 1}. Сбиты палки с номера "))
    right = int(input("по номер "))
    sticks = ["." if (left <= i + 1 <= right or sticks[i] == ".") else "|" for i in range(n)]
print("Результат:", *sticks)