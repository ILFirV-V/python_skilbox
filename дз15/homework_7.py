#7

def get_weight_container():
    weight_container = int(input("Введите вес контейнера: "))
    if weight_container > 200:
        print("Введите вес контейнера <= 200")
        weight_container = get_weight_container()
    return weight_container


count = int(input("Количество контейнеров: "))
containers = []
for i in range(count):
    containers.append(get_weight_container())
new_container = int(input("Введите вес нового контейнера: "))
for i in range(count):
    if containers[i] <= new_container:
        print("Номер, который получит новый контейнер:", (i + 1))
        break