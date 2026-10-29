import actions
import data

def menu(students):
    while True:
        print('A) Add a new student')
        print('B) Show list information of all students')
        print('C) Top 3 students with the better notes')
        print('D) Average score for each student')
        print('E) Make a system backup: Export all data into a CSV file')
        print('F) Restore the system data: Import all data from a CSV file')
        print('G) Erase a student from the system')
        print('H) Show failed students')
        print('X) Exit (Make sure you made a data backup)')
        option = input('Choose an option: ').strip().upper()
        match option:
            case "A":
                print("Let's add a student into the system:\n")
                actions.add_student_info(students)
                print('\n')
            case "B":
                actions.print_all_students(students)
                print('\n\n')
            case "C":
                print('\n')
                actions.top_3_students(students)
                print('\n')
            case "D":
                actions.average_each_student(students,True)
                print('\n')
            case "E":
                print('')
                data.system_backup(students)
            case "F":
                data.import_data(students)
            case "G":
                actions.erase_student(students)
                print('')
            case "H":
                actions.failed_students(students)
                print('\n')
            case "X":
                break
            case _:
                print('Invalid answer! Please make sure you to write a valid option (A-H or X for exit)')