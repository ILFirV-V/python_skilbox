#4

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек:", guests)
    action = input("Гость пришёл или ушёл? ").lower()
    if action == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if action == "пришёл":
        if len(guests) >= 6:
            print(f"Прости, {name}, но мест нет.")
        else:
            print(f"Привет, {name}!")
            guests.append(name)
    if action == "ушёл":
        print(f"Пока, {name}!")
        guests.remove(name)

