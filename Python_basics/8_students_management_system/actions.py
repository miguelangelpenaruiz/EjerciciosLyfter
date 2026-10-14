def add_student_info(students):
    student_questionary = {}
    #EDIT HERE THE FIELDS YOU WANT FOR THE STUDENTS
    keys_for_student_info = ['complete_name', 'section']
    keys_for_grades = ['spanish_grade', 'english_grade', 'social_studies_grade', 'science_grade']

    for field in range(len(keys_for_student_info)):
        answer = input(f'{keys_for_student_info[field]}: ')
        student_questionary[keys_for_student_info[field]] = answer

    for field in range(len(keys_for_grades)):
        answer = float(input((f'{keys_for_grades[field]}: ')))
        student_questionary[keys_for_grades[field]] = answer
    

    students.append(student_questionary)

    print(f' You registered: {student_questionary} \n\n')

def print_all_students(students):
    print(f'Student Records:')
    for record in students:
        for key,value in record.items():
            print(f'{key}: {value}')
        print('\n')