# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_of_keys = ["k1",'k2','k3','k4','k5']
list_of_values = ['v1','v2','v3','v4','v5']

my_first_dictionary = {

}

for index in range(len(list_of_keys)):
    my_first_dictionary[list_of_keys[index]] = list_of_values[index]

print(my_first_dictionary)
#