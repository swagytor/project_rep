import utils
from Question import Question
from random import shuffle

URL_TO_JSON_BIN = 'https://api.npoint.io/ea2cd07582bc624de34c'

question_data = utils.get_data_from_json(URL_TO_JSON_BIN)

list_of_objects = [Question(*item.values()) for item in question_data]

shuffle(list_of_objects)

for question in list_of_objects:
    print(question.build_question())
    user_input = input('Введите ваш ответ: ')
    setattr(question, 'is_asked', True)
    setattr(question, 'user_answer', question.is_correct(user_input))
    if question.is_correct(user_input):
        print(question.build_positive_feedback())
    else:
        print(question.build_negative_feedback())

all_points = [obj.get_points() for obj in list_of_objects if obj.user_answer]
number_of_questions = len(list_of_objects)

utils.print_statistics(all_points, number_of_questions)