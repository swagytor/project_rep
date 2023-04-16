import requests
from python_tools.dynamic_border import dynamic_border


def get_data(json_url):
    response = requests.get(json_url).json()

    return response


def validate_selected_mode(modes):
    # просим пользователя ввести уровень сложности
    user_select = input('Выберите уровень сложности: ').lower().strip()

    # если введённого уровня сложности нет в словаре modes
    while user_select not in modes:
        print('Нет такого уровня сложности\n'
              'Пожалуйста, повторите попытку')
        user_select = input('Выберите уровень сложности: ').lower().strip()

    return user_select


def select_mode(modes):
    """Возвращает словарь слов и ответов,
    в зависимости от выбранного уровня сложности
"""
    # выводим доступные режимы сложности в рамках, с помощью функции dynamic_border()
    print(f'Есть {len(modes)} режима сложности:')
    for mode in modes:
        dynamic_border(mode.upper())

    mode_select = validate_selected_mode(modes)

    print(f'Выбран уровень сложности "{mode_select}", мы предложим 5 слов, подберите к ним перевод.')

    # после успешного выбора сложности, возвращаем словарь слов и переводов
    return modes[mode_select]


def testing(words_dict):
    """Проводит тестирование,
    и возвращает количество правильных ответов
"""
    # объявляем счётчики текущего уровня, правильных ответов
    correct = 0
    level_count = 1

    # создаём словарь, куда будем заносить ответы пользователя
    answers = {}

    input('Нажмите Enter, чтобы начать\n')

    # совершаем итерацию по словарю
    for word, translate in words_dict.items():
        # выводим номер текущего уровня
        print(f'Уровень {level_count}')

        # выводим слово на английском и информацию по правильному ответу
        print(f'{word}, {len(translate)} букв, начинается на {translate[0]}')

        user_answer = input('Введите перевод: ').lower().strip()

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
        input('Нажмите Enter, чтобы перейти на следующий уровень\n')
        level_count += 1

    # после окончания итераций выводим верно и неверно отвеченные слова
    print('Правильно отвечены слова:')
    [print(word) for word, is_correct in answers.items() if is_correct is True]

    print()

    print('Неправильно отвечены слова:')
    [print(word) for word, is_correct in answers.items() if is_correct is False]

    # возвращаем количество правильных ответов
    return correct
