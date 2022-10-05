#5

violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83]
]


def get_time(song):
    for i in violator_songs:
        if i[0] == song:
            return i[1]


count = int(input("Сколько песен выбрать? "))
time = 0.0
for i in range(count):
    name = input(f"Название {i + 1}-й песни: ").strip()
    time += get_time(name)
print(f"Общее время звучания песен: {round(time, 2)} минуты")

