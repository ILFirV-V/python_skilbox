#6

def get_unique_letters(word):
    count = 0
    for i in word:
        if word.count(i) == 1:
            count += 1
    return count

# def get_unique_letters2(word):
#     result_count = 0
#     for i in word:
#         count = 0
#         for j in word:
#             if j == i:
#                 count += 1
#             if count > 1:
#                 break
#         if count == 1:
#             result_count += 1
#     return result_count


word = input("Введите слово: ")
print("Количество уникальных букв:", get_unique_letters(word))