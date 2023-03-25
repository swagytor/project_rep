def resulting_levels(correct):
    """Выводит ранг пользователя,
    в зависимости от количества правильных ответов
"""
    levels = {
        0: "Нулевой",
        1: "Так себе",
        2: "Можно лучше",
        3: "Норм",
        4: "Хорошо",
        5: "Отлично",
    }

    return levels[correct]


def select_mode():
    """Возвращает словарь слов и ответов,
    в зависимости от выбранного уровня сложности
"""
    modes = {
        'easy_mode': {
            'cow': 'корова',
            'morning': 'утро',
            'sun': 'солнце',
            'friend': 'друг',
            'river': 'река'
        },
        'medium_mode': {
            'evening': 'вечер',
            'tale': 'рассказ',
            'guest': 'гость',
            'purchase': 'покупка',
            'justice': 'справедливость'
        },
        'hard_mode': {
            'opportunity': 'возможность',
            'devotion': 'преданность',
            'fortune': 'судьба',
            'addiction': 'зависимость',
            'amateur': 'любитель'
        }
    }
    # выводим доступные режимы сложности в рамках, с помощью функции dynamic_border()
    print('Есть три режима сложности')
    dynamic_border('EASY')
    dynamic_border('MEDIUM')
    dynamic_border('HARD')

    # просим пользователя ввести уровень сложности
    user_select = input('Выберите уровень сложности: ').lower() + '_mode'

    # если введённого уровня сложности нет в словаре modes
    while user_select not in modes:
        print('Нет такого уровня сложности\nПожалуйста, повторите попытку')
        user_select = input('Выберите уровень сложности: ').lower()

    print(f'Выбран уровень сложности "{user_select}", мы предложим 5 слов, подберите перевод.')

    # после успешного выбора сложности, возвращаем словарь слов и ответов
    return modes[user_select]


def dynamic_border(sentence):
    """Выводит уровни сложностей в рамках"""
    width = 22

    print('+-' + '-' * width + '-+')
    print('| {0:^{1}} |'.format(sentence, width))
    print('+-' + '-' * width + '-+')


def testing(words_dict):
    """Проводит тестирование,
    и возвращает количество правильных ответов
"""
    # объявляем счётчики текущего уровня, правильных ответов
    level_count = 1
    correct = 0

    # создаём словарь, куда будем заносить ответы пользователя
    answers = {}

    input('Нажмите Enter, чтобы начать')

    print()

    # совершаем итерацию по словарю
    for word, translate in words_dict.items():
        # выводим номер текущего уровня
        print(f'Уровень {level_count}')

        # выводим слово на английском и информацию по правильному ответу
        print(f'{word}, {len(translate)} букв, начинается на {translate[0]}')

        user_answer = input('Введите перевод: ').lower()

        # в случае правильного ответа прибавляем к счётчику correct
        if user_answer == translate:
            correct += 1
            print(f'Верно, {word.title()} - это {translate}.')
        else:
            print(f'Неверно, {word.title()} - это {translate}.')

        # добавляем в словарь answers результат ответа в булевом формате
        answers[word] = user_answer == translate

        print()

        # прибавляем к счётчику текущего уровня
        input('Нажмите Enter, чтобы перейти на следующий уровень')
        level_count += 1

        print()

    # после окончания итераций выводим верно и неверно отвеченные слова
    print('Правильно отвечены слова:')
    [print(word) for word, is_correct in answers.items() if is_correct is True]

    print()

    print('Неправильно отвечены слова:')
    [print(word) for word, is_correct in answers.items() if is_correct is False]

    # возвращаем количество правильных ответов
    return correct
