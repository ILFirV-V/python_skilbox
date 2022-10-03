#5

def get_smallest_divisor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i


number = int(input("Введите число: "))
print("Наименьший делитель, отличный от единицы:", get_smallest_divisor(number))
