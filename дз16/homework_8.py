#8

people_count = int(input("Кол-во человек: "))
people = list(range(1, people_count + 1))
number_out = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number_out}-й человек")
dropped_out = 0
for i in range(people_count - 1):
    print("\nТекущий круг людей", people)
    start = dropped_out % len(people)
    dropped_out = (start + number_out - 1) % len(people)
    print("Начало счёта с номера", people[start])
    print("Выбывает человек под номером", people[dropped_out])
    people.remove(people[dropped_out])

print("\nОстался человек под номером", *people)