# Cree una función que le dé la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”


#FIRST TRY--------------------------------------- I HAD TO RESOLVE IT WITH LIST

# def make_string_backwards(string_to_change):
#     my_new_string = []
#     for index in range(len(string_to_change),0,-1):
#         my_new_string.append(string_to_change[index-1])
#     return my_new_string


# my_string = 'Hello world'

# print(make_string_backwards(my_string))


#SECOND TRY ---------------------------------- CLAUDE REMINDED ME OF CONCATENATION TO JOIN STRINGS


def make_string_backwards(string_to_change):
    my_new_string = ''
    for index in range(len(string_to_change),0,-1):
        my_new_string += string_to_change[index-1]
    return my_new_string

def main():
    my_string = 'Hello world'
    print(make_string_backwards(my_string))

main()
