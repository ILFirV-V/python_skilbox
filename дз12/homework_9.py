#9
import random


def rock_paper_scissors():
    actions = ['1', '2', '3']
    computer_action = random.choice(actions)
    action = input("выберите цифру (камень(1), бумага(2), ножницы(3): ")
    if action == computer_action:
        print("ничья")
    elif action == "1":
        if computer_action == "2":
            print("бумага кроет камень")
            print("поражение")
        elif computer_action == "3":
            print("камень бьёт ножницы")
            print("победа")
    elif action == "2":
        if computer_action == "1":
            print("бумага кроет камень")
            print("победа")
        elif computer_action == "3":
            print("ножницы режут бумагу")
            print("поражение")
    elif action == "3":
        if computer_action == "1":
            print("камень бьёт ножницы")
            print("поражение")
        elif computer_action == "2":
            print("ножницы режут бумагу")
            print("победа")
    mainMenu()

def guess_the_number():
    rnd_number = random.randint(1, 10)
    count = 0
    while True:
        count += 1
        entered_number = int(input("Введите число: "))
        if entered_number > rnd_number:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
        elif entered_number < rnd_number:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
        else:
            print("Вы угадали! Число попыток:", count)
            break
    mainMenu()


def mainMenu():
    print("Menu: \n 1 - игра: Камень, ножницы, бумага \n 2 - игра: Угадай число \n \
               \n E - выход")
    while True:
        action = input("Введите действие: ")
        if action == "1":
            rock_paper_scissors()
        elif action == "2":
            guess_the_number()
        elif action == "E" or action == "e":
            print("Выход")
            break

mainMenu()
