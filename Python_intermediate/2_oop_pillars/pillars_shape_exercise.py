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
        print(f"The perimeter is {perimeter}m")

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        print(f'The area is {area}m2')

try:
    wheel = Shape()
except TypeError as error:
    print(f'{error}')

wheel = Circle(3)
wheel.calculate_area()
wheel.calculate_perimeter()


