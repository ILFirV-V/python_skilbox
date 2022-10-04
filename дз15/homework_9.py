#9
import math


def get_is_palindrome(inputString):
    work_string = inputString.strip()
    length = len(work_string)
    for i in range(math.floor(length / 2)):
        if work_string[i] != work_string[length - 1 - i]:
            return False
    return True


word = input("Введите слово: ")
print(f"Слово" + (' ' if get_is_palindrome(word) else ' не ') + "является палиндромом")