# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41

# buscar por posición lista[#] y si le pones el =, sustituye y TE REGRESA EL VALOR 
# buscar por valor lista.index(#) y no le puedes poner un = para sustituir

def get_total_sum(some_list):
    total_sum = 0
    for index in range(len(some_list)):
        total_sum += some_list[index]
    return total_sum
def main():
    my_list_of_numbers = [5,2,3]
    print(f'{my_list_of_numbers} -> {get_total_sum(my_list_of_numbers)}')

main()

#
