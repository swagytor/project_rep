import utils


def main():
    """
    Основное тело программы
    """
    # объявляем имя пользователя с помощью функции get_a_username()
    user_name = utils.get_a_username()
    print(f'Приятно познакомиться, {user_name}!\nДавай начнём игру!')
    print()

    # объявляем список вопросов с помощью функции get_list_of_words()
    question_list = utils.get_list_of_words('data/words.txt')

    # объявляем количество очков за игру с помощью функции guess_the_word()
    game_score = utils.guess_the_word(question_list)

    # выводим результат игры
    print(f'{user_name} набирает {game_score} очков.')

    # записываем результат игры с помощью функции record_the_result()
    utils.record_the_result(user_name, game_score)

    # получаем статистику сыгранных игр и рекорд игры с помощью функции get_statistics()
    counter_of_games, max_score = utils.get_statistics()

    print()

    # выводим статистику
    print(f'Количество игр: {counter_of_games}\nМаксимальный рекорд: {max_score}')


if __name__ == '__main__':
    main()
