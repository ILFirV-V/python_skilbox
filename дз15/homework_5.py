#5

def menu(is_logged):
    if not is_logged:
        get_greeting()
    action = input("посмотреть список фильмов(S) \nпосмотреть список избранных фильмов(F) \nдобавить фильм в избранное(A) \n").upper()
    if action == "S":
        get_movies()
    if action == "F":
        get_favorites_movies()
    if action == "A":
        get_movies()
        count = int(input("Сколько фильмов хотите добавить? "))
        for i in range(count):
            favorite_movie = input("Какой из предложенных фильмов вам понравился? ")
            add_favorites_movies(favorite_movie)
    menu(True)

def get_greeting():
    action_start = input("Првиет \nчтобы зарегистрироваться введи R \nчтобы войти введи C \n").upper()
    if action_start == "R":
        name = input("Введи свое имя: ")
        print(name, "вы успешно зарегистрировались")
    elif action_start == "C":
        name = input("Введи свое имя: ")
        print(name, "мы рады вас снова видеть")


def get_movies():
    print("Наш список фильмов:", films)
    return films


def get_favorites_movies():
    print("Ваш список любимых фильмов:", favorites_movies)
    return favorites_movies


def add_favorites_movies(favorite_movie):
    if films.__contains__(favorite_movie) and not favorites_movies.__contains__(favorite_movie):
        favorites_movies.append(favorite_movie)
        print("Фильм успешно добавлен :)")
    elif favorites_movies.__contains__(favorite_movie):
        print("Он уже был добавлен до этого :)")
    else:
        print("Такого фильма нет :(")


films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
favorites_movies = []
menu(False)