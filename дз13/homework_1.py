#1


def get_degree_1(number):
    len = 0
    while number <= 1:
        number *= 10
        len -= 1
    return (len, number)


def get_degree_2(number):
    len = 0
    while number >= 10:
        number /= 10
        len += 1
    return (len, number)


number = float(input("Введите число: "))
len = 0
if number <= 1:
    result = get_degree_1(number)
    number = round(result[1], 1)
    len = result[0]
elif number >= 10:
    result = get_degree_2(number)
    number = result[1]
    len = result[0]
print(f"Формат плавающей точки: x = {number} * 10 ** {len}")