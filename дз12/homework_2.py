#2

def test():
    number = int(input("целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Введите другое число")
        test()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")

test()