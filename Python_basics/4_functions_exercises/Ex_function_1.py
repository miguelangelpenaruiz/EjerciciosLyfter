# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_in_first_function():
    print('First Function Print')
    print_in_my_second_function()

def print_in_my_second_function():
    print('Second Function Print')

print_in_first_function()