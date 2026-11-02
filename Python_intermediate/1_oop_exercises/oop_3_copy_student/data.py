import csv
import actions
import os
import student_class

BASE_DIR = os.path.dirname(__file__)
BACKUP_FILE = os.path.join(BASE_DIR, 'backup.csv')

def system_backup(students):
    fields = list(student_class.Student.fields_students)
    if not students:
        print('List Empty')
    else:
        try:
            with open(BACKUP_FILE, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fields)
                writer.writeheader()

                students_as_dicts = []

                for student in students:
                    students_as_dicts.append(student.to_dict()) 
                writer.writerows(students_as_dicts)

            print('Data exported to backup.csv')
        except FileNotFoundError as ex:
            print(f'File not found {ex}')

def import_data(students):
    try:
        with open(BACKUP_FILE, 'r', newline= '', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            counter = 0
            rows_skipped = 0
            students.clear()
            for row in reader:
                value_complete_name = row[list(student_class.Student.fields_students)[0]]
                value_section = row[list(student_class.Student.fields_students)[1]]
                if actions.student_exists(value_complete_name, value_section, students):
                    continue
                else:
                    try:
                        new_student = student_class.Student(row)
                        students.append(new_student)
                        counter += 1
                    except (ValueError, KeyError):
                        rows_skipped += 1
            print(f'\n {counter} students restored \n')
            if rows_skipped == 1:
                print(f'{rows_skipped} row skipped due to invalid grades')
            elif rows_skipped > 1:
                print(f'{rows_skipped} rows skipped due to invalid grades')
    except FileNotFoundError:
        print(f'\n No backup found. Export your data first (option E).')





