# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def make_string_list(string_to_list):
    list_hyphens = []
    one_word = ''
    for index in range(len(string_to_list)):
        if string_to_list[index] != '-':
            one_word += string_to_list[index]
        else:
            list_hyphens.append(one_word)
            one_word = ''
            continue
    list_hyphens.append(one_word)
    return list_hyphens

# --------------------- SÍ FUNCIONA PERO NO ES BUBBLE SORT COMO ME PIDEN EN EL FEEDBACK

# def order_string_alphabetical(string_to_list):
#     for i in range(len(string_to_list)):
#         for index in range(len(string_to_list)):
#             if string_to_list[i] <= string_to_list[index]:
#                 string_to_list[index], string_to_list[i] = string_to_list[i], string_to_list[index]
#     return string_to_list


def order_string_alphabetical(string_to_list):
    for i in range(len(string_to_list)):
        for index in range(len(string_to_list)-1-i):
            if string_to_list[index] > string_to_list[index+1]:
                string_to_list[index], string_to_list[index+1] = string_to_list[index+1], string_to_list[index]
    return string_to_list

def make_list_string(list_to_string):
    one_word = ''
    for index in range(len(list_to_string)):
        one_word += '-'
        one_word += list_to_string[index]
    
    return one_word[1:]

def main():
    list_to_change = make_string_list('hello-how-are-you-i-am-miguel-and-you')
    print(list_to_change)
    print(order_string_alphabetical(list_to_change))
    result_list = order_string_alphabetical(list_to_change)
    print(make_list_string(result_list))


main()
