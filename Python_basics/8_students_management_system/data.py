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
    key_for_student_info, key_for_grades = actions.student_data_fields()
    try: 
        with open(BACKUP_FILE, 'r', newline= '', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in key_for_grades:
                    row[key] = float(row[key])
                students.append(row)
        return True
    except FileNotFoundError as ex:
        print(f'File not found {ex}')
        return False



