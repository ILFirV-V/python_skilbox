#6

player_score = int(input("Кубик Кости: "))
owner_score = int(input("Кубик владельца: "))
if player_score >= owner_score:
    print(owner_score - player_score)
    print("Костя платит")
else:
    print(owner_score + player_score)
    print("Владелец платит")
print("Игра окончена")