# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_parameters_d(func):
    def wrapper(*args, **kwargs):
        for parameters in args:
            print(parameters)
        for key, value in kwargs.items():
            print(f'{key} = {value}')
        result = func(*args,**kwargs)
        print(result)
        return result
    return wrapper


@print_parameters_d
def add(a, b):
    return a + b

total = add(2, b=3)
print(total * 10) 