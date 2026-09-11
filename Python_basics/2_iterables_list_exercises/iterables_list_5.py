# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

print("Welcome, give me 10 numbers please")
my_list = []
for i in range(10):
    num = int(input(f"Write number {i + 1}: "))
    my_list.append(num)

print(my_list)
num_max = max(my_list)

print(f"The highest number is: {num_max}")