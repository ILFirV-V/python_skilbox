#4

text = input('экспоненциальная форма числа: ')
parts = text.split('e')

print("мантисса:", parts[0])
print("порядок этого числа:", parts[1])
