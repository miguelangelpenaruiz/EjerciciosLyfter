# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
# Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def find_prime_number(number_to_check):
    number_floor = 0
    if number_to_check <= 1:
        return False
    if number_to_check == 2:
        return True
    if number_to_check == 3:
        return True
    if number_to_check % 2 == 0:
        return False
    elif number_to_check % 3 == 0:
        return False
    else:
        number_floor = int(number_to_check ** 0.5)
        for index in range(5, number_floor + 1, 6):
            if number_to_check % index == 0:
                return False
            if number_to_check % (index + 2) == 0:
                return False
        return True

def return_prime_numbers(list_to_check):
    new_list = []
    for index in range(len(list_to_check)):
        if find_prime_number(list_to_check[index]) == True:
            new_list.append(list_to_check[index])
    return new_list
        
def main():
    # print(find_prime_number(-1))
    list_to_check = [12,34,7,6,12,1,0,9,13]
    print(return_prime_numbers(list_to_check))

main()
#