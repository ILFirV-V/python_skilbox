#9

def annuity_payment(n, i):
    k = pow(i + 1, n)
    return i * k / (k - 1)


def print_info(period, credit_sum, percent, repayment_loan_body):
    print(f"\nПериод: {period}")
    print(f"Остаток долга на начало периода: {round(credit_sum, 2)}")
    print(f"Выплачено процентов: {round(credit_sum * percent, 2)}")
    print(f"Выплачено тела кредита: {round(repayment_loan_body, 2)}")


credit_sum = float(input("Введите сумму кредита: "))
years = int(input("На сколько лет выдан? "))
percent = float(input("Сколько процентов годовых? ")) / 100

annuity_payment_amount = credit_sum * annuity_payment(years, percent)
for j in range(1, 4):
    repayment_loan_body = annuity_payment_amount - credit_sum * percent
    print_info(j, credit_sum, percent, repayment_loan_body)
    credit_sum = credit_sum - repayment_loan_body

print(f"\nОстаток долга: {round(credit_sum, 2)}\n")
print("==============================\n")

years_extended = int(input("На сколько лет продляется договор? "))
change_percent = float(input("Увеличение ставки до: ")) / 100
years = years_extended + years - 3

annuity_payment_amount = credit_sum * annuity_payment(years, change_percent)
for j in range(1, years + 1):
    repayment_loan_body = annuity_payment_amount - credit_sum * change_percent
    print_info(j, credit_sum, change_percent, repayment_loan_body)
    credit_sum = credit_sum - repayment_loan_body

print(f"\nОстаток долга: {round(credit_sum, 2)}")