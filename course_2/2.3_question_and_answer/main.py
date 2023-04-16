import utils
from question import Question
from random import shuffle

# объявляем константу, которая ссылается на внешний ресурс с вопросами
URL_TO_JSON_BIN = 'https://api.npoint.io/384b56bc7ab906f053b6'


NUMBER_OF_QUESTIONS = 5

# объявляем переменную, которая содержит загруженные данные с внешнего ресурса
question_data = utils.get_data_from_json(URL_TO_JSON_BIN)

# объявляем список, который содержит экземпляры класса Question
list_of_objects = [Question(**kwargs) for kwargs in question_data]

shuffle(list_of_objects)

for level, question in enumerate(list_of_objects, 1):
    print('Игра начинается!')

    if level > NUMBER_OF_QUESTIONS:
        break

    # выводим информацию вопроса с помощью метода экземпляра
    print(f'Вопрос {level}:')
    print(question.build_question())
    user_answer = input('Введите ваш ответ: ').lower().strip()

    # выставляем обновлённые значения у свойств экземпляра класса question
    setattr(question, 'is_asked', True)
    setattr(question, 'user_answer', question.is_correct(user_answer))

    # зависимости от правильности ответа, отправляем пользователю сообщение
    if question.is_correct(user_answer):
        print(question.build_positive_feedback())
    else:
        print(question.build_negative_feedback())

    print()

# посчитываем очки каждого объекта класса
all_points = [obj.get_points() for obj in list_of_objects if obj.user_answer]

# выведем статистику викторины
utils.print_statistics(all_points, NUMBER_OF_QUESTIONS)
