#5

text = input("Введите строку: ")
a = [i for i, x in enumerate(text) if x == 'h']
result = text[a[0] + 1:a[-1]][::-1]
print("Развёрнутая последовательность между первым и последним h:", result)