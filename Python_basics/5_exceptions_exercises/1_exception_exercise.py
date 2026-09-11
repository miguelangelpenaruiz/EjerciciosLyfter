def main():
    first_number = ask_number()
    menu(first_number)
    
def ask_number():
    while True:
        try:
            input_number = int(input('Write number: '))
            return input_number
        except ValueError:
            print('You did not wrote a integer number!!!! \n')

def menu(first_number):
    print(f'Your actual first number is: {first_number}')
    print(f'Select the operation you want to do')
    try:
        selected_option = str(input('a. Add \nb. Difference \nc. Multiplication \nd. Division \ne. Erase result \n Your selection: '))
        if selected_option != 'a' and selected_option != 'b' and selected_option != 'c' and selected_option != 'd' and selected_option != 'e':
            raise ValueError
    except ValueError:
        print('You did not choose a validated option!!! \n')
        return menu(first_number)
    if selected_option == 'a':
        result_operation = add(first_number)
    elif selected_option == 'b':
        result_operation = difference(first_number)
    elif selected_option == 'c':
        result_operation = multiplication(first_number)
    elif selected_option == 'd':
        result_operation = division(first_number)
    elif selected_option == 'e':
        result_operation = erase_result()
    print(f'The result is {result_operation} \n')
    menu(result_operation)

def add(first_number):
    print(f'{first_number} + ')
    second_number = ask_number()
    result_operation = first_number + second_number
    return result_operation

def difference(first_number):
    print(f'{first_number} - ')
    second_number = ask_number()
    result_operation = first_number - second_number
    return result_operation

def multiplication(first_number):
    print(f'{first_number} * ')
    second_number = ask_number()
    result_operation = first_number * second_number
    return result_operation

def division(first_number):
    print(f'{first_number} / ')
    second_number = ask_number()
    try:
        result_operation = first_number / second_number
    except ZeroDivisionError as ex:
        print('You cannot divided CERO !!!')
        return first_number
    return result_operation

def erase_result():
    return 0

try:
    main()
except Exception as ex:
    print(f'There is a general error \n {ex}')