#7

start_year = int(input("Введите первый год: "))
end_year = int(input("Введите второй год: "))
for i in range(start_year, end_year):
    year = str(i)
    for j in range(4):
        if year.count(year[j]) == 3:
            print(year)
            break