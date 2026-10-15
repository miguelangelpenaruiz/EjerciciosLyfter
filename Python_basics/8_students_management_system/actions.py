def add_student_info(students):
    student_questionary = {}
    #EDIT HERE THE FIELDS YOU WANT FOR THE STUDENTS
    keys_for_student_info = ['complete_name', 'section']
    keys_for_grades = ['spanish_grade', 'english_grade', 'social_studies_grade', 'science_grade']

    for field in keys_for_student_info:
        answer = input(f'{format_label(field)}: ')
        student_questionary[field] = answer

    for field in keys_for_grades:
        while True:
            try:
                answer = float(input(f'{format_label(field)}: '))
                if 0 <= answer <= 100:
                    student_questionary[field] = answer
                    break
                else:
                    print("Invalid grade, a valid grade is between 0 and 100")
            except ValueError as ex:
                print('You must write a float number for a grade')

    students.append(student_questionary)
    print(f' You registered: {student_questionary} \n\n')

def print_all_students(students):
    if students == []:
        print('Empty List')
    else:
        print(f'Student Records:')
        for record in students:
            for key,value in record.items():
                print(f'{format_label(key)}: {value}')
            print('\n')

def format_label(key):
    return key.replace("_", " ").title()