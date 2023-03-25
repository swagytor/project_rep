from random import shuffle


def get_a_username() -> str:
    """
    Возвращает корректное имя пользователя
    """
    name = input('Введите ваше имя: ')

    # создаём проверку на отсутсвие символов и цифр
    while not name.isalpha() or len(name) >= 10:
        if len(name) >= 10:
            print('Имя не должно состоять более чем из 10 букв!')
        if not name.isalpha():
            print('Имя не должно содержать цифр и символов!')
        name = input('Введите ваше имя: ')

    return name.capitalize()


def get_list_of_words(file) -> list:
    """
    Возвращает список слов, считанных из file
    """
    # с помощью контекстного менеджера считываем данные из файла, и заносим в список
    with open(file, encoding='utf-8') as word_file:
        list_of_words = [line.rstrip() for line in word_file.readlines()]

    return list_of_words


def guess_the_word(word_list: list) -> int:
    """
    Проводит тестирование, и возвращает количество очков
    """
    points = 0
    # проходимся итерацией по списку word_list
    for index, word in enumerate(word_list, 1):

        print(f'Слово {index}')
        # выводим перешанное слово с помощью функции shuffle_word()
        print(shuffle_word(word))

        user_answer = input('Введите ваш ответ: ').lower()
        # делаем проверку на правильность ответа пользователя
        if user_answer == word:
            print('Верно! Вы получаете 10 очков.')
            points += 10
        else:
            print(f'Неверно! Верный ответ - {word}.')
        print()

    return points


def shuffle_word(word: str) -> str:
    """
    Возвращает перемешанное слово
    """
    # преобразуем строку word в список separated_word
    separated_word = list(word)

    # создаём защиту если перемешанное слово является загаданным
    while separated_word == list(word):
        # с помощью функции random.shuffle() перемешиваем список separated_word
        shuffle(separated_word)

    return ''.join(separated_word)


def record_the_result(name: str, score: int):
    """
    Записывает в файл history.txt имя и результат пользователя
    """
    with open('data/history.txt', 'a', encoding='utf-8') as output_file:
        print(name, score, sep='\t', file=output_file)


def get_statistics() -> tuple:
    """
    Возвращает из файла history.txt данные в виде количества игр и максмальном количестве очков
    """
    with open('data/history.txt', encoding='utf-8') as statistics:
        # с помощью дескриптора файла statistics, добавляем данные файла в список read_statistics
        read_statistics = statistics.read().split()

    # объявляем список statistic_list с количеством очков
    statistics_list = [int(score) for index, score in enumerate(read_statistics) if index % 2]
    # считаем количество игр и рекорд
    count_games = len(statistics_list)
    max_result = max(statistics_list)

    # возвращаем количество игр и рекорд
    return count_games, max_result
