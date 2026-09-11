approved_grades = 0
failed_grades = 0
approved_average = 0
failed_average = 0
total_average = 0

total_grades = int(input("Whats the total number of grades you have? "))

for i in range(total_grades):
    grade = int(input(f"Write your grade {i + 1}: "))
    if grade < 70:
        failed_grades += 1
        failed_average += grade
    else:
        approved_grades += 1
        approved_average += grade
    total_average += grade



total_average = total_average / total_grades

print(f"The total approved grades is {approved_grades}")
if approved_grades > 0:
    approved_average = approved_average / approved_grades
    print(f"This is the average for the approved grades {approved_average}")
else:
    print("There are not approved grades")
print(f"This is the total failed grades {failed_grades}")
if failed_grades > 0:
    failed_average = failed_average / failed_grades
    print(f"The failed grades average is {failed_average}")
else:
    print("There are not failed grades")
print(f"This is the total average {total_average}")
