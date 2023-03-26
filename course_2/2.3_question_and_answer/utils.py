import requests


def get_data_from_json(path):
    response = requests.get(path).json()
    return response

print(get_data_from_json('https://api.npoint.io/ea2cd07582bc624de34c'))

def print_statistics(list_of_points, lenght_of_game):
    correct_count = len(list_of_points)
    summary_points = sum(list_of_points)
    print(f'Вот и всё!\nОтвечено {correct_count} вопроса из {lenght_of_game}\nНабрано баллов: {summary_points}')
