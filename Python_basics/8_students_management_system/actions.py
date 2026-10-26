
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

def print_all_students(students):
    if students == []:
        print('Empty List')
    else:
        print(f'\n Student Records: \n')
        for record in students:
            print_student(record)
            print('\n')

def print_student(student):
    for key,value in student.items():
        print(f'{format_label(key)}: {value}')

def format_label(key):
    return key.replace("_", " ").title()

def average_each_student(students,switch):
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
        if switch == True:
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

def top_3_students(students):
    print('Top 3 Best Student \n')
    top_first = sorted(students, key=average_grade, reverse=True)
    if len(top_first) > 3:
        counter = 0
        for record in top_first:
            if average_grade(record) >= average_grade(top_first[2]):
                counter +=1
                if counter == 4:
                    print('\n Tie Students: ')
                
                print('\n')
                print_student(record)
                print(f'Average: {average_grade(record)}')
    else:
        average_each_student(top_first, False)

def erase_student(students):
    keys_for_student_info, keys_for_grades = student_data_fields()
    answer_name = input(f'Which student you want to erase? Write {format_label(keys_for_student_info[0])} ')
    answer_section = input(f'In which section belong? Write {format_label(keys_for_student_info[1])} ')

    student = student_exists(answer_name,answer_section,students)

    if student:
        print('Delete confirmation')
        print_student(student)
        answer_validation = input(f'Do you confirm you want to delete: (Y/N)').upper()
        if answer_validation == "Y":
            students.remove(student)
            print('Student deleted')
        else:
            print('Deletion cancelled')
    else:
        print("That name and section doesn't exist, try again")

def failed_students(students):
    print('')
    print('Failed Students: \n')
    counter = 0
    for record in students:
        failed_subjects = {}
        for key,value in record.items():
            if isinstance (value,float):
                if value < 60:
                    failed_subjects[key] = value
        if failed_subjects:
            counter += 1
            print(f"\n{record['complete_name']} ({record['section']})")
            for subject, grade in failed_subjects.items():
                print(f'  {format_label(subject)}: {grade}')
    if counter == 0:
        print('No failed students')

def student_exists(name, section, students):
    keys_for_student_info, keys_for_grades = student_data_fields()
    for record in students:
        if record[keys_for_student_info[0]] == name and record[keys_for_student_info[1]] == section:
            return record
    return None
    
