import actions

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
            case "B":
                print('\n')
                actions.print_all_students(students)
                print('\n\n')
            case "C":
                print('\n')
                actions.top_3_students(students)
            case "D":
                print('')
            case "E":
                print('')
            case "F":
                print('')
            case "G":
                print('')
            case "H":
                print('')
            case "X":
                break
            case _:
                print('Invalid answer! Please make sure you to write a valid option (A-H)')