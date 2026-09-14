print("Welcome, give me 3 different number and I'll help you find the biggest one")
number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))
number_3 = int(input("Third number: "))

if number_1 > number_2 and number_1 > number_3:
    print(f"the biggest number is {number_1}")
elif number_2 > number_3:
    print(f"the biggest number is {number_2}")    
else:
    print(f"the biggest number is {number_3}")
#