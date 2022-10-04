#8

scoreboard = []
count = int(input("Сколько будет элементов табло: "))
for i in range(count):
    scoreboard.append(input("Введите элемент табло: "))
shift = int(input("Сдвиг: "))
print("Изначальный список: ", scoreboard)
new_scoreboard = scoreboard[-shift:] + scoreboard[:-shift]
print("Сдвинутый список: ", new_scoreboard)