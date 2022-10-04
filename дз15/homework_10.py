from random import randint


def bubble_sort(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


N = int(input("Введите количество чисел в массиве: "))
array = []
for i in range(N):
    array.append(randint(1, 99))
print("Изначальный список:", array)
bubble_sort(array)
print("Отсортированный список:", array)