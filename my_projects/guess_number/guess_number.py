import utils


def main():
    """
    Основное тело программы
    """
    print(
        'Привет!\n'
        'Добро пожаловать в "Числовую Угадайку"!\n'
        'Как я могу к тебе обращаться?')

    # объявляем имя пользователя с помощью функции get_user_name()
    user_name = utils.get_user_name()

    print(f'Приятно познакомиться, {user_name}!\n'
          'Давай же начнём нашу игру!')

    # объявляем результат игры с помощью функции guess_number()
    game_result = utils.guess_number()

    print(f'{user_name}, ваше количество попыток состовляет: {game_result} попыток')

    # записываем в список топ игроков
    loaded_data = utils.load_result()

    print('Загружаем ваш результат в список рекордов')

    # добавляем в список топ игроков текущий результат
    loaded_data.append([user_name, game_result])
    # сортируем список от наменьшего количества попыток
    updated_data = sorted(loaded_data, key=lambda x: int(x[1]))
    # загружаем в файл новый топ игроков
    utils.update_result(updated_data)

    print('Список рекордов был обновлён')

    print('Спасибо, что играли в "числовую угадайку"! Еще увидимся...')


if __name__ == '__main__':
    main()
