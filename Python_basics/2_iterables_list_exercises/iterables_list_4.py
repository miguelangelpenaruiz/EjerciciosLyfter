# Cree un programa que elimine todos los números impares de una lista.

my_list = [1,2,3,4,5,6,7,8,9,10]

for index in range(len(my_list) -1,-1,-1):
    if my_list[index] % 2 != 0:
        my_list.pop(index)

print(my_list)