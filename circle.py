import math

class Circle(object):
    """ A basic shape class that represents a circle with attributes:
        radius
        diamater
        area """
    
    def __init__(self, radius=1):
        self._radius = radius
        self._area = math.pi * math.pow(radius, 2)
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('Radius cannot be negative')
        self.diamater = val * 2
        self._radius = val
        self._area = math.pi * math.pow(val, 2)
        return val

    @property
    def diamater(self):
        return self.radius * 2
    
    @diamater.setter
    def diamater(self, val):
        self._radius = val / 2
        self._area = math.pi * math.pow((val / 2), 2)
        return val
    
    @property
    def area(self):
        return self._area
    
    def __repr__(self):
        return (f'Radius: {self.radius} | Diamater: {self.diamater} | Area: {self.area:.2f}')

if __name__ == "__main__":
    test_circle = Circle(5)
    assert test_circle.radius == 5, 'The initial radius in incorrect'
    assert test_circle.diamater == 10, 'The initial diamater is incorrect'
    assert round(test_circle.area,2) == 78.54, 'The initial area is incorrect'
    test_circle.radius = 6
    assert test_circle.radius == 6, 'Radius after radius change in incorrect'
    assert test_circle.diamater == 12, 'Diamater after radius change is incorrect'
    assert round(test_circle.area, 2) == 113.10, 'Area after radius change in incorrect'
    test_circle.diamater = 20
    assert test_circle.radius == 10.0, 'Radius after diamater change is incorrect' 
    assert test_circle.diamater == 20.0, 'Radius after diamater change in incorrect'
    assert round(test_circle.area, 2) == 314.16, 'Area after diamater change incorrect'
    # test_circle.area = 5
    # assert test_circle.radius == 10.0, 'Radius changed after area update' 
    # assert test_circle.diamater == 20.0, 'Radius changed after area update'
    # assert round(test_circle.area, 2) == 314.16, 'Area succesfully changed'


