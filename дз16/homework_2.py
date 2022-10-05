#2

def bubble_sort(array, count):
    for i in range(count-1):
        for j in range(count-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


class_first = list(range(160, 177, 2))
class_second = list(range(162, 181, 3))

class_first.extend(class_second)

bubble_sort(class_first, len(class_first))
print("Отсортированный список учеников:", class_first)