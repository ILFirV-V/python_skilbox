#10

def get_cipher(string, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_string = ''
    for i in char_list:
        new_string += i
    return new_string


text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()
print(get_cipher(text, shift))