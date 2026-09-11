# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [1,2,3,4,5]

# buscar por posición lista[#] y si le pones el =, sustituye y TE REGRESA EL VALOR
# buscar por valor lista.index(#) y no le puedes poner un = para sustituir

#------------------------------------------------------------------FIRST TRY WITHOUT HELP
# my_list[-1] = my_list[0]
# my_list[0] = my_list[-1] 

# print(my_list)

#------------------------------------------------------------------SECOND TRY

# my_new_list = [my_list[-1] = my_list[0], my_list[1] = my_list[-1] ]
# print(my_new_list)

#---------------------------------------------------------------------THIRD TRY
# Al parecer existe asignaciones multiples separadas por comas


my_list[-1], my_list[0] = my_list[0], my_list[-1] 

print(my_list)