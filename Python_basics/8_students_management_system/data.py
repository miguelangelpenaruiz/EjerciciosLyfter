import csv
import actions
import os

BASE_DIR = os.path.dirname(__file__)
BACKUP_FILE = os.path.join(BASE_DIR, 'backup.csv')

def system_backup(students):
    key_for_student_info, key_for_grades = actions.student_data_fields()
    fields = []
    fields.extend(key_for_student_info)
    fields.extend(key_for_grades)
    if not students:
        print('List Empty')
    else:
        try:
            with open(BACKUP_FILE, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fields)
                writer.writeheader()
                writer.writerows(students)
            print('Data exported to backup.csv')
        except FileNotFoundError as ex:
            print(f'File not found {ex}')

def import_data(students):
    keys_for_student_info, keys_for_grades = actions.student_data_fields()
    try:
        with open(BACKUP_FILE, 'r', newline= '', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            counter = 0
            rows_skipped = 0
            students.clear()
            for row in reader:
                value_complete_name = row[keys_for_student_info[0]]
                value_section = row[keys_for_student_info[1]]
                if actions.student_exists(value_complete_name, value_section, students):
                    continue
                else:
                    try:
                        for key in keys_for_grades:
                            row[key] = float(row[key])
                        counter += 1
                        students.append(row)
                    except ValueError:
                        rows_skipped += 1
            print(f'\n {counter} students restored \n')
            if rows_skipped == 1:
                print(f'{rows_skipped} row skipped due to invalid grades')
            elif rows_skipped > 1:
                print(f'{rows_skipped} row skipped due to invalid grades')
    except FileNotFoundError:
        print(f'\n No backup found. Export your data first (option E).')





