import csv
import actions

def system_backup(students):
    key_for_student_info, key_for_grades = actions.student_data_fields()
    fields = []
    fields.extend(key_for_student_info)
    fields.extend(key_for_grades)
    if not students:
        print('List Empty')
    else:
        try:
            with open('Python_basics/8_students_management_system/backup.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fields)
                writer.writeheader()
                writer.writerows(students)
            print('Data exported to backup.csv')
        except FileNotFoundError as ex:
            print(f'File not found {ex}')