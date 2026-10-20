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

def template():
    key_for_student_info, key_for_grades = actions.student_data_fields()
    fields = []
    fields.extend(key_for_student_info)
    fields.extend(key_for_grades)
    with open('import_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fields)
        writer.writeheader()

def import_data(students):
    key_for_student_info, key_for_grades = actions.student_data_fields()
    try: 
        with open('import_data.csv', 'r', newline= '', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in key_for_grades:
                    row[key] = float(row[key])
                students.append(row)
    except FileNotFoundError as ex:
        print(f'File not found {ex}')
