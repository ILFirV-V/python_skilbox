#3

file_size = float(input("Укажите размер файла для скачивания: "))
speed = float(input("Какова скорость вашего соединения? "))
time = round(file_size / speed)
for i in range(1, time + 1):
    downloaded = i * speed if i * speed <= file_size else file_size
    print(f"Прошло {i} сек. Скачано {downloaded} из {file_size} Мб ({round(downloaded / file_size * 100)}%)")
