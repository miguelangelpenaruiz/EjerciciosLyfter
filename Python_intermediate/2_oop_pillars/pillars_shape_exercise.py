from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()

    def calculate_perimeter(self, radius):
        perimeter = (radius*2)*math.pi
        print(f"The perimeter is {perimeter}m")
        return super().calculate_perimeter()

    def calculate_area(self, radius):
        area = (math.pi*radius) ** 2
        print(f'The area is {area}m2')
        return super().calculate_area()

try:
    wheel = Shape()
except Exception:
    print(f'{Exception}')

wheel = Circle()
wheel.calculate_area(3)
wheel.calculate_perimeter(3)


