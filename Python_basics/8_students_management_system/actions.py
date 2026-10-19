def student_data_fields():
    #EDIT HERE THE FIELDS YOU WANT FOR THE STUDENTS
    keys_for_student_info = ['complete_name', 'section']
    keys_for_grades = ['spanish_grade', 'english_grade', 'social_studies_grade', 'science_grade']    
    
    return keys_for_student_info, keys_for_grades

def add_student_info(students):
    student_questionary = {}

    keys_for_student_info, keys_for_grades = student_data_fields() 

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
            print_student(record)
            print('\n')

def print_student(student):
    for key,value in student.items():
        print(f'{format_label(key)}: {value}')

def format_label(key):
    return key.replace("_", " ").title()

def average_each_student(students):
    print('')

    if not students:
        print('List Empty')
    else:
        counter = 0
        sum_averages = 0
        for record in students:
            average = average_grade(record)
            print('\n') 
            print_student(record)
            print(f'Average: {average}') 
            counter +=1
            sum_averages = average + sum_averages
        print(f'\n General Average: {sum_averages/counter}')




def average_grade(student):
    counter = 0
    sum_grades = 0
    for key,value in student.items():
        if isinstance(value,float):
            counter += 1
            sum_grades = value + sum_grades
    average = sum_grades/counter
    return average

