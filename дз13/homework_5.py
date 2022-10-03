def get_len(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def check_len(len, must_count):
    if not(must_count != 3 and must_count == 4) and not(must_count == 3 and must_count != 4):
        print("ошибка")
        return False
    message = "В первом" if must_count == 3 else "Во втором"
    if len < must_count:
        print(f"{message} числе меньше {must_count} цифр.")
        return False
    return True


def get_change_number(number):
    len = (get_len(number))
    last_digit = number % 10
    first_digit = number // 10 ** (len - 1)
    between_digits = number % 10 ** (len - 1) // 10
    return last_digit * 10 ** (len - 1) + between_digits * 10 + first_digit


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
if check_len(get_len(first_number), 3) and check_len(get_len(second_number), 4):
    first_change_number = get_change_number(first_number)
    second_change_number = get_change_number(second_number)
    print('Изменённое первое число:', first_change_number)
    print('Изменённое второе число:', second_change_number)
    print('\nСумма чисел:', first_change_number + second_change_number)
