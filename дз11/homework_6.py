#6

bottomLine = int(input("нижняя граница температуры: "))
upperLine = int(input("верхняя граница температуры: "))
step = int(input("шаг: "))
print("C    F")
for i in range(bottomLine, upperLine + 1, step):
    print(f"{i}    {round(i*1.8) + 32}")
    if i < upperLine < i + step:
        print(f"{upperLine}    {round(upperLine*1.8) + 32}")
