#8

hours = int(input("Введите отработанные часы: "))
loan_balance = int(input("Введите остаток по кредиту: "))
spend_food = int(input("Введите траты на еду: "))
salary = (200 * hours / 2**3) + hours
if salary >= loan_balance + spend_food:
    print("Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать!")