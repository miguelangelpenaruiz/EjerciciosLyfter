from datetime import date

class User():
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return(
            today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )


def validate_legal_age(func):
    def wrapper(*args, **kwargs):
        all_parameters = list(args) + list(kwargs.values())
        for parameter in all_parameters:
            if isinstance(parameter, User) and parameter.age < 18:
                raise ValueError('The user is not adult')
        result = func(*args,**kwargs)
        return result
    return wrapper

@validate_legal_age
def buy_alcohol(user):
    return "Purchase approved"

if __name__ == "__main__":
    adult = User(date(1998, 3, 10))
    minor = User(date(2012, 6, 1))

    print(buy_alcohol(adult))
    print(buy_alcohol(user = adult))
    try:
        buy_alcohol(minor)
    except ValueError as error:
        print(error)          
