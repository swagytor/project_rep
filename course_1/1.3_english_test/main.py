import functions
import constant
from validators.validator import get_valid_name


def main():
    # выводим приветствие и просим пользователя представиться
    print('Привет! Предлагаю проверить свои знания английского!')

    # объявляем имя пользователя с помощью функции get_valid_name()
    user_name = get_valid_name()
    print(f'Приятно познакомиться, {user_name}!')

    # просим пользователя набрать команду "ready"
    user_command = input('Набери "ready", чтобы начать тестирование! ').lower().strip()

    # если пользователь набрал команду "ready", начинаем тестирование
    if user_command == 'ready':

        list_of_question = functions.get_quiz_list(constant.JSON_URL)

        # объявляем общее количество баллов и верных ответов с помощью функции testing()
        user_score, correct_count = functions.testing(list_of_question)

        # вычисляем процент правильных ответов
        percent = int(user_score / (len(list_of_question) * 3) * 100)

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
