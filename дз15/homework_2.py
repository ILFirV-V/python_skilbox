array_participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
array_participants_first_day = []
for i in range(0, len(array_participants), 2):
    array_participants_first_day.append(array_participants[i])
print("Первый день:", array_participants_first_day)