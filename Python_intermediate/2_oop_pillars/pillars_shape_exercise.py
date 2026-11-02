from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = (self.radius*2)*math.pi
        return perimeter

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

try:
    wheel = Shape()
except TypeError as error:
    print(f'{error}')

wheel = Circle(3)
print(f'The area of the wheel is {wheel.calculate_area()}m2')
print(f"The perimeter of the wheel is {wheel.calculate_perimeter()}m")


class Square(Shape):
    def __init__(self, side):
        self.side = side
        super().__init__()

    def calculate_perimeter(self):
        perimeter = self.side * 4
        return perimeter

    def calculate_area(self):
        area = self.side*self.side
        return area

notebook = Square(22)
print(f'The area of the notebook is {notebook.calculate_area()}cm2')
print(f"The perimeter of the notebook is {notebook.calculate_perimeter()}cm")

class Rectangle(Shape):
    def __init__(self, base, high):
        self.base = base
        self.high = high
        super().__init__()

    def calculate_area(self):
        area = self.base * self.high
        return area

    def calculate_perimeter(self):
        perimeter = (self.base*2)+(self.high*2)
        return perimeter

book = Rectangle(7,22)
print(f'The area of the book is {book.calculate_area()}cm2')
print(f"The perimeter of the book is {book.calculate_perimeter()}cm")