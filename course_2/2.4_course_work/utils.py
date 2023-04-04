import requests
from basicword import BasicWord
from random import choice


def load_random_word(path: str) -> BasicWord:
    """
    Загружает одно случайное слово из JSON-BIN,
    и объявляем его в качестве объекта класса BasicWord
    :param path: URL-адрес JSON-BIN
    :return: объект класса BasicWord
    """
    response = requests.get(path).json()

    original_word, acceptable_words = choice(response).values()

    game = BasicWord(original_word, set(acceptable_words))

    return game


def get_valid_name() -> str:
    """
    Возвращает корректное имя игрока
    :return: Имя игрока
    """
    while True:
        user_name = input('Скажи, как я могу к тебе обращаться?: ')
        if user_name.isalpha() and len(user_name) <= 10:
            return user_name.title()
        # выводим ошибку ввода имени красным текстом
        print('\033[31m' + 'Некорректное имя пользователя!')
        print('\033[39m' + 'В имени не должно быть цифр и символов\n'
                           'И длина имени не должна превышать 10 символов\n')


def get_shortest_length(word_list: list):
    """
    Возвращаем самое короткое загаданное слово списка
    :param word_list: список загаданных слов
    :return: Самое короткое загаданное слово списка
    """
    shortest_length = min(word_list, key=len)
    return shortest_length
