import os.path
from random import randint


def get_user_name() -> str:
    """
    Возвращает корректное имя пользователя
    """
    input_name = input('Введите ваше имя: ')
    # создаём правила на корректное имя пользователя
    while not (input_name.isalpha() and len(input_name) < 9):
        if len(input_name) > 8:
            print('Длина имени не должна превышать 8 символов!')

        if not input_name.isalpha():
            print('В имени не должно быть цифр и символов!')

        input_name = input('Введите ваше имя: ')

    return input_name.capitalize()


def get_number() -> int:
    """
    Возвращает корректное введённое число
    """
    input_number = input('Введите целое число от 1 до 100: ')

    while True:
        if input_number.isdigit() and 0 < int(input_number) < 101:
            return int(input_number)
        print('Число должно быть целым и не должно содержать символы!')
        input_number = input('Может быть все-таки введем целое число от 1 до 100?: ')


def guess_number() -> int:
    """
    Возвращает количество попыток в игре
    """
    # объявляем переменную с случайным числом от 1 до 100
    random_number = randint(1, 100)
    # объявляем счётчик попыток
    try_count = 1
    while True:
        # с помощью функции get_number() получаем, введённое пользователем, число
        user_answer = get_number()
        if user_answer == random_number:
            print('Вы угадали!Поздравляю!')
            return try_count
        elif user_answer < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Ваше число больше загаданного, попробуйте еще разок')
        # прибавляем счётчик попыток
        try_count += 1


def load_result():
    """
    Создаёт файл results.txt и возвращает загруженные данные из файла
    """
    # создаём файл results.txt, если его нет в папке
    if not os.path.isfile('results.txt'):
        with open('results.txt', 'w', encoding='utf-8'):
            pass

    # считываем данные с файла results.txt
    with open('results.txt', encoding='utf-8') as file:
        data = [row.split() for row in file.readlines()]

    return data


def update_result(upload_list):
    """
    Перезаписываем в файл results.txt обновлённые данные игр
    """
    with open('results.txt', 'w', encoding='utf-8') as output_file:
        for name, score in upload_list:
            print(name, score, sep='\t\t', file=output_file)
