from random import choice


def get_random_word(words):
    """
    Получает рандомное слово из списка words
    """
    word = choice(words)
    return word


def morse_encode(word):
    """
    Принимает слово,
    и возвращает зашифрованное слово в виде кода Морзе
    """
    # создаём словарь кода Морзе для зашифровки
    morse_encode_dict = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }

    # по ключу каждой итерируемой буквы слова, добавляем в списочное выражение
    # значение словаря, и преобразуем в строку с помощью метода .join()
    encoding_word = ' '.join([morse_encode_dict[letter] for letter in word])

    # возвращаем зашифрованное слово
    return encoding_word


def guessing_words(words):
    """
    Проводит тестирование,
    принимая список слов list_of_words,
    и возвращая список ответов answers
    """
    # объявляем список answers, в который будем добавлять ответы пользователя
    answers = []
    # объявляем количество вопросов
    number_of_questions = 5

    for question_number in range(1, number_of_questions + 1):
        # используем функцию choice(), которая возвращает рандомное слово из списка words
        random_word = get_random_word(words)
        # выводим номер вопроса и рандомное слово в виде кода морзе, с помощью функции morse_encode()
        print(f'Слово {question_number}: {morse_encode(random_word)}')

        # просим пользователя ввести ответ
        user_answer = input('Введите зашифрованное слово: ').lower()

        # делаем проверку ответа пользователя
        if user_answer == random_word:
            print(f'Верно, {random_word.capitalize()}!')
        else:
            print(f'Неверно, {random_word.capitalize()}!')
        # добавляем ответ в виде булевого значения в список answers
        answers.append(user_answer == random_word)

        # если вопрос не последний
        if question_number != number_of_questions:
            print('Переходим к следующему вопросу')
        print()

    # возвращаем список ответов пользователя
    return answers


def print_statistics(list_of_answers):
    """
    Принимает список ответов в виде булевых значений,
    и выводит статистику
    """
    print('Тест подошёл к концу, вот твоя статистика:',
          f'Всего вопросов: {len(list_of_answers)}',
          f'Отвечено верно: {list_of_answers.count(True)}',
          f'Отвечено неверно: {list_of_answers.count(False)}',
          sep='\n')