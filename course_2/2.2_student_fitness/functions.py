import json


def load_students(json_file):
    with open(json_file, encoding='utf-8') as file:
        data = json.load(file)

    return data


def load_professions(json_file):
    with open(json_file, encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_student_by_pk(data, student_pk):
    for student_dict in data:
        if student_dict['pk'] == student_pk:
            return student_dict
    print('У нас нет такого студента')
    exit()


def get_profession_by_title(data, profession_title):
    for profession_dict in data:
        if profession_dict['title'] == profession_title:
            return profession_dict
    print('У нас нет такой специальности')
    exit()


def check_fitness(student_skills, profession_skills):
    fitness_dict = dict()

    fitness_dict['has'] = list(student_skills.intersection(profession_skills))
    fitness_dict['lacks'] = list(profession_skills.difference(student_skills))
    fitness_dict['fit_percent'] = int(len(fitness_dict['has']) / len(profession_skills) * 100)

    return fitness_dict