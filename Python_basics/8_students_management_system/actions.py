def add_student_info(students):
    student_formulary = {}
    #EDIT HERE THE FIELDS YOU WANT FOR THE STUDENTS
    keys_for_formulary = ['Complete Name', 'Group', 'Spanish Note', 'English Note', 'Social Studies Note', 'Science Note']

    for i in range(len(keys_for_formulary)):
        answer = input(f'{keys_for_formulary[i]}: ')
        student_formulary[keys_for_formulary[i]] = answer

    students.append(student_formulary)

    print(f' You registered: {student_formulary} \n\n')

def print_all_students(students):
    print(students)