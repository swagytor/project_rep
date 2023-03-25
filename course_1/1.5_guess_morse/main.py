import functions


def main():
    """
    Основное тело программы
    """
    # создаём список загадываемых слов, которые будут выводиться в тесте
    list_of_words = ['snake', 'python', 'code', 'bit', 'list', 'soul',
                     'next', 'apple', 'car', 'study', 'lesson', 'hacker']

    print('Привет!\nСегодня мы потренируемся расшифровывать азбуку Морзе')
    input('Нажмите Enter и начнем: ')
    # запускаем функцию guessing_words(), указывая список загадываемых слов list_of_words
    answers_list = functions.guessing_words(list_of_words)

    functions.print_statistics(answers_list)


if __name__ == '__main__':
    main()
