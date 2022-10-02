#5

minutes = int(input("Минуты: "))
whole_hours = minutes // 60
rest_hour = minutes % 60
minutes_an_hour = 60 - rest_hour
print("Целых часов:", whole_hours, "Остаток минут:", rest_hour, "Нужно еще минут:", minutes_an_hour)
