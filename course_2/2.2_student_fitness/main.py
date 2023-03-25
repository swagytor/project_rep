import functions


def main():
    students_data = functions.load_students('data/students.json')
    professions_data = functions.load_professions('data/professions.json')

    input_student_pk = input('Пожалуйста, введите номер студента: ')
    while not input_student_pk.isdigit():
        print('Номер студента не должен содержать буквы и символы!')
        input_student_pk = input('Пожалуйста, введите номер студента: ')

    print()

    student_info = functions.get_student_by_pk(students_data, int(input_student_pk))

    student_full_name = student_info['full_name']
    student_skills = set(student_info['skills'])

    print(f'Студент {student_full_name}\n'
          f'Знает: {", ".join(student_skills)}\n'
          f'Выберите специальность для оценки знаний студента {student_full_name}:')

    input_profession = input().title()

    profession_info = functions.get_profession_by_title(professions_data, input_profession)

    profession_skills = set(profession_info['skills'])

    student_fitness = functions.check_fitness(student_skills, profession_skills)

    print(f'Пригодность: {student_fitness["fit_percent"]}%\n'
          f'{student_full_name} знает {", ".join(student_fitness["has"])}\n'
          f'{student_full_name} не знает {", ".join(student_fitness["lacks"])}')


if __name__ == '__main__':
    main()

