print("Welcome, to know your age range please answer the following questions")
name = input("Name: \n")
last_name = input("Last Name: \n")
age = int(input("Age: \n"))

if age <= 2:
    print(f"{name} {last_name} you're a baby")
elif age <= 9:
    print(f"{name} {last_name} you're a child")
elif age <= 12:
    print(f"{name} {last_name} you're a preteen")
elif age <= 17:
    print(f"{name} {last_name} you're a teenager")
elif age <= 29:
    print(f"{name} {last_name} you're a young adult")
elif age <= 59:
    print(f"{name} {last_name} you're a adult")
elif age >= 60:
    print(f"{name} {last_name} you're a senior")
#