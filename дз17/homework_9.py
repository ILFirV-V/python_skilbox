#9

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


new_list = [number for interior_list in nice_list for innermost_list in interior_list for number in innermost_list]
print("Ответ:", new_list)
