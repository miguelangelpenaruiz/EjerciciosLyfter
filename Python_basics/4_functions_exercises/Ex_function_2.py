# Experimente con el concepto de scope:
#   Intente acceder a una variable definida dentro de una función desde afuera.
#   Intente acceder a una variable global desde una función y cambiar su valor.

def my_first_function():
    inside_variable = 22

# print(inside_variable) <----- ERROR

my_global_variable = 21


def my_second_function():
    global my_global_variable # sin este me daba error
    my_global_variable = my_global_variable + 999

my_second_function()
print(my_global_variable)
