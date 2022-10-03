#6

start = float(input('Введите начальную амплитуду: '))
end = float(input('Введите амплитуду остановки: '))

count = 0
step = 8.4 / 100

while start > end:
    start -= start * step
    count += 1

print('Маятник считается остановившимся через', count, 'колебаний')


