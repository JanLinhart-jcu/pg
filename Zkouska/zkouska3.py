import math

class Shape:

    def __init__(self, shape_name=None):
        self.shape_name = shape_name # Nastavení názvu tvaru shape_name
    
    def __str__(self):
        return f'{self.shape_name} shape with area {self.area()}' # Definuje jak se zobrazí při použití print

    def area(self):
        return 0.0 # základní metoda area, defaultně vrací 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle") # zavolá konstruktor rodičovské třídy a předá název tvaru "Rectangle"
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 1) # Metoda area počítá plochu obdélníku a zaokrouhluje výsledek na jedno desetinné místo.

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # zavolá konstruktor rodičovské třídy a předá název tvaru "Circle"
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 1) # Metoda area počítá plochu kruhu pomocí vzorce π * r^2

    def __str__(self):
        return f'{self.shape_name} with a radius of {self.radius} has an area of {self.area()}' # řetězec popisující parametry tvaru

from unittest.mock import patch, MagicMock, mock_open

# Unit testy
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20.0
    assert str(rect) == "Rectangle shape with area 20.0"

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
    assert str(circle) == "Circle with a radius of 3 has an area of 28.3"

if __name__ == "__main__":
    shape = Shape()
    print(shape)
    rect = Rectangle(4, 5)
    print(rect)
    circle = Circle(3)
    print(circle)
