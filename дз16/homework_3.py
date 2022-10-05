#3

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]


def get_shop_details():
    details = []
    for i in shop:
        details.append(i[0])
    return details


def get_price(detail):
    for i in shop:
        if i[0] == detail:
            return i[1]
    return 0


def buy_detail():
    buy_details = []
    price = 0
    while True:
        details = get_shop_details()
        detail = input("Какую деталь хотите купить? ").lower()
        if not details.__contains__(detail):
            print("Такой детали нет :(")
            print("Есть вот эти товары", shop)
        else:
            count = int(input("Введите кол-во деталей: "))
            price += get_price(detail) * count
            for i in range(count):
                buy_details.append(detail)
            print(detail, "ждет оплаты")
        action = input("Хотите купить еще что-то?(no для выхода) ").lower()
        if action == "no":
            print("Вы хотите купить:", buy_details, "общая цена:", price, "количество деталей:", len(buy_details))
            main()
            break
    return


def main():
    action = input("Введите 'choice' для выбора деталей \nВведите 'exit' для выхода\n").lower()
    if action == "choice":
        buy_detail()
    if action == "exit":
        print("Выход")
        return


main()