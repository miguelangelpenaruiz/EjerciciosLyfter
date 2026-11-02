import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi * self.radius ** 2
        return area


test = Circle(2)
print(f'The area of the circle is: {test.get_area()}')