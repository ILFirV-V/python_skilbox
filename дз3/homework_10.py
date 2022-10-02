#10

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = str(a) + " " + str(b)
b = a.split()[0]
a = a.split()[1]
print(a, b)