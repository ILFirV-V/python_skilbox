#4

prices = input("Введите стоимость товаров через пробел: ")
array_price = prices.split()
sum = 0
for price in array_price:
    sum += int(price)
if sum > 10000:
    sum -= sum * 10 / 100
print(sum)



