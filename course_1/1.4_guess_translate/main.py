import functions
import constant


def main():
    """Запускает функции выбора режима сложности и тестирования,
    после чего выводит ранг, в зависимости от
    количества правильных ответов
"""
    json_data = functions.get_data(constant.JSON_URL)

    modes = json_data['modes']

    levels_rank = json_data['ranking']

    print('Привет! Давай сыграем в игру "Угадай перевод"')
    # объявляем уровень сложности с помощью функции select_mode()
    difficult_mode = functions.select_mode(modes)

    # получаем количество правильных ответов с помощью функции testing()
    correct_count = functions.testing(difficult_mode)

    print()

    user_rank = levels_rank[str(correct_count)]
    print(f'Ваш ранг:\n{user_rank}')


if __name__ == '__main__':
    main()
