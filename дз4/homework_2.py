#2

score_Russian = int(input("Введите количество баллов по русскому языку: "))
score_math = int(input("Введите количество баллов по математике: "))
score_computer_science = int(input("Введите количество баллов по информатике: "))
if score_math + score_Russian + score_computer_science >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")