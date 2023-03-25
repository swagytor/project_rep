import functions


def main():
    """Запускает функции выбора режима сложности и тестирования,
    после чего выводит ранг, в зависимости от
    количества правильных ответов
"""
    print('Привет! Давай сыграем в игру "Угадай перевод"')
    # объявляем уровень сложности с помощью функции select_mode()
    difficult_mode = functions.select_mode()

    # получаем количество правильных ответов с помощью функции testing()
    correct_count = functions.testing(difficult_mode)

    print()

    user_rank = functions.resulting_levels(correct_count)
    # выводим ранг с помощью функции resulting_levels()
    print(f'Ваш ранг:\n{user_rank}')


if __name__ == '__main__':
    main()
