from random import randint


def bubble_sort(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def selection_sort(array):
    len_array = len(array)
    for i in range(len_array):
        for j in range(i + 1, len_array):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]



N = int(input("Введите количество чисел в массиве: "))
array = []
for i in range(N):
    array.append(randint(1, 99))
print("Изначальный список:", array)
selection_sort(array)
print("Отсортированный список:", array)