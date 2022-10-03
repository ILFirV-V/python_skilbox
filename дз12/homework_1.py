# 1

def summa_n(n):
    sum_numbers = 0
    for i in range(1, n + 1):
        sum_numbers += i
    print(f"сумма чисел от 1 до {n} равна {sum_numbers}")


summa_n(int(input("Введите число: ")))
