#1

euro_price = round(float(input("Введите сумму: ")), 2)
dollar_price = round(1.25 * euro_price, 2)
ruble_price = round(60.87 * dollar_price, 2)
print("сумма в рублях: ", ruble_price)

