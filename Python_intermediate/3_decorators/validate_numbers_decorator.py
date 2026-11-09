# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def validate_parameters_numbers(func):
    def wrapper(*args, **kwargs):
        all_parameters = list(args) + list(kwargs.values())
        for parameter in all_parameters:
            if not isinstance(parameter, (int, float)):
                raise TypeError(f'The parameter: {parameter} type: {type(parameter).__name__} is invalid, must be an int or float number')
        result = func(*args, **kwargs)
        return result
    return wrapper

@validate_parameters_numbers
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 5))
    print(add(2.5, 1))
    print(add(2, b=3))
    try:
        add(2, "4")
    except TypeError as error:
        print(error)
    try:
        add(2, b="3")
    except TypeError as error:
        print(error)