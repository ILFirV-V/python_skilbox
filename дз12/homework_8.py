#8

def greatest_common_divisor(a, b):
    result = 1
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result

first_number = int(input("первое число: "))
second_number = int(input("второе число: "))
print(f"НОД чисел {first_number} и {second_number} = {greatest_common_divisor(first_number, second_number)}")
