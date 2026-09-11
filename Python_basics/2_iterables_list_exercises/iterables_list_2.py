# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Chocolate milk"


for index in range(len(my_string), 0, -1):
    print(my_string[index - 1])