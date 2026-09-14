# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def calculate_upper_letters(string_to_calculate):
    number_upper = 0
    for index in range(len(string_to_calculate)):
        if string_to_calculate[index].isupper() == True:
            number_upper += 1
    return number_upper

def calculate_lower_letters(string_to_calculate):
    number_lower = 0
    for index in range(len(string_to_calculate)):
        if string_to_calculate[index].islower() == True:
            number_lower += 1
    return number_lower

def main():
    my_string = 'My name is Miguel Peña'

    number_lower = calculate_lower_letters(my_string)
    number_upper = calculate_upper_letters(my_string)

    print(f'Theres {number_upper} upper cases and {number_lower} lower cases')

main()
#