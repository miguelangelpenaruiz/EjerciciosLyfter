# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['My','name','Miguel','Peña']
second_list = ['complete','is','Angel','Ruiz']

# FIRST TRY WITHOUT HELP

# for index, words1 in enumerate(first_list):
#     for words2 in (second_list):
#         print(f"Word {index + 1}: {words2}")
    
#     print(f"Word {index + 1}: {words1}")
#     index += 1

# SECOND TRY WITH A CLUE OF CLAUDE

for index in range(len(first_list)):
    print(f"Word {index + 1}: {first_list[index]}")
    print(f"Word {index + 2}: {second_list[index]}")



