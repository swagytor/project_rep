import requests
from python_tools.func_timer import func_timer


def get_quiz_list(json_url):
    response = requests.get(json_url).json()

    return response


@func_timer
def testing(list_of_question):

    # объявляем счётчики верных ответов и баллов
    correct = 0
    score = 0

    # выводим сообщение о начале тестирования
    print('Давай тогда начнём тестирование.\nВот твой первый вопрос:')

    # совершаем итерацию по списку вопросов для тестирования
    for test in list_of_question:
        # объявляем количество попыток, который будет возобновляться каждую итерацию
        attempts_left = 3

        # выводим вопрос и варианты ответа
        print(test['question'], end='\n  ')
        print('\n  '.join(test['answer_choices']))
        print('У тебя есть 3 попытки на вопрос')

        # просим пользователя ввести свой ответ
        user_answer = input('Введите свой ответ: ')

        # пока ответ пользователя не будет правильным
        while user_answer != test['correct_answer']:
            # убавляем попытку в случае неправильного ответа
            attempts_left -= 1

            # если пользователь трижды ошибся, переходим к следующему вопросу
            if attempts_left == 0:
                print(
                    'Увы, но нет!',
                    'Попытки закончились',
                    f'Правильный ответ: {test["correct_answer"]}',
                    sep='\n')
                break

            print('Неправильно!\nПопробуй ещё раз')

            print()

            # выводим сколько попыток осталось у пользователя
            print(f'Осталось {attempts_left} попыток')

            user_answer = input('Введите свой ответ: ')

        #  зависимости от количества оставшихся попыток, выдаём баллы за правильный ответ
        if user_answer == test['correct_answer']:
            print('Правильно!\nПолучен:', attempts_left, 'балл' + ('' if attempts_left == 1 else 'а'))
            score += attempts_left
            correct += 1

        print()

        # если не последний вопрос в списке test_list
        if test != list_of_question[-1]:
            print('Переходим к следующему вопросу:')

    # возвращаем общее количество баллов и верных ответов
    return score, correct
