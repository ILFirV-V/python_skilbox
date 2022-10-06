#1

text = input("Введите текст: ")
vowels = set("ауоеияюёэы")
result = [f"{x}" for x in text if x in vowels ]
print("Список гласных букв:", result)
print("Длина списка:", len(result))