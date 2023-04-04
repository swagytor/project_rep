import requests


def get_data_from_json(path: str) -> dict:
    """
    возвращает данные с сайта path
    """
    response = requests.get(path).json()
    return response


def print_statistics(list_of_points: list, lenght_of_game: int):
    """
    выводит результаты викторины
    """
    # объявляем сколько отвечено верно и сколько всего очков заработано
    correct_count = len(list_of_points)
    summary_points = sum(list_of_points)

    print(f'Вот и всё!\n'
          f'Отвечено {correct_count} вопроса из {lenght_of_game}\n'
          f'Набрано баллов: {summary_points}')
