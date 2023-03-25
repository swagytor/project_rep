import functions


def main():
    # объявляем имя пользователя с помощью функции greetings()
    user_name = functions.greetings()
    print(f'Приятно познакомиться, {user_name}!')

    # просим пользователя набрать команду "ready"
    user_command = input('Набери "ready", чтобы начать тестирование! ')

    # если пользователь набрал команду "ready", начинаем тестирование
    if user_command.lower() == 'ready':

        tests_list = functions.get_quiz_list('tests.json')

        # объявляем общее количество баллов и верных ответов с помощью функции testing()
        user_score, correct_count = functions.testing(tests_list)

        # вычисляем процент правильных ответов
        percent = int(user_score / (len(tests_list) * 3) * 100)

        # объявляем окончание тестирования и его результаты
        print(
            f'Вот и всё, {user_name}!',
            f'Вы ответили на {correct_count} вопроса из 3 верно.',
            f'Вы заработали {user_score} баллов!',
            f'Это {percent}% результата.',
            'До новых встреч!',
            sep='\n')

    # если пользователь не набрал команду "ready"
    else:
        print(f'{user_name}, кажется ты не хочешь играть.\nОчень жаль:(')


if __name__ == '__main__':
    main()
