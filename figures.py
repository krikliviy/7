from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def dimension(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def square(self):
        pass
    
    @abstractmethod
    def squareSurface(self):
        pass
    
    @abstractmethod
    def squareBase(self):
        pass
    
    @abstractmethod
    def height(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass

# Двумерные фигуры
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def dimension(self):
        return 2
        
    def perimeter(self):
        return self.a + self.b + self.c
        
    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        
    def squareSurface(self):
        return None
        
    def squareBase(self):
        return None
        
    def height(self):
        return None
        
    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def dimension(self):
        return 2
        
    def perimeter(self):
        return 2 * (self.a + self.b)
        
    def square(self):
        return self.a * self.b
        
    def squareSurface(self):
        return None
        
    def squareBase(self):
        return None
        
    def height(self):
        return None
        
    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a  # верхнее основание
        self.b = b  # нижнее основание
        self.c = c  # левая боковая сторона
        self.d = d  # правая боковая сторона
        
    def dimension(self):
        return 2
        
    def perimeter(self):
        return self.a + self.b + self.c + self.d
        
    def square(self):
        h = self.height()
        return (self.a + self.b) * h / 2
        
    def squareSurface(self):
        return None
        
    def squareBase(self):
        return None
        
    def height(self):
        # Высота трапеции через стороны
        x = (self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2
        y = 2 * (self.b - self.a)
        h = math.sqrt(self.c ** 2 - (x / y) ** 2)
        return h
        
    def volume(self):
        return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        
    def dimension(self):
        return 2
        
    def perimeter(self):
        return 2 * (self.a + self.b)
        
    def square(self):
        return self.a * self.h
        
    def squareSurface(self):
        return None
        
    def squareBase(self):
        return None
        
    def height(self):
        return self.h
        
    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r
        
    def dimension(self):
        return 2
        
    def perimeter(self):
        return 2 * math.pi * self.r
        
    def square(self):
        return math.pi * self.r ** 2
        
    def squareSurface(self):
        return None
        
    def squareBase(self):
        return None
        
    def height(self):
        return None
        
    def volume(self):
        return self.square()

# Трехмерные фигуры
class Ball(Figure):
    def __init__(self, r):
        self.r = r
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        return 4 * math.pi * self.r ** 2
        
    def squareBase(self):
        return None
        
    def height(self):
        return None
        
    def volume(self):
        return (4/3) * math.pi * self.r ** 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)  # правильный треугольник
        self.h = h
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        # Площадь боковой поверхности правильной треугольной пирамиды
        apothem = math.sqrt(self.h ** 2 + (self.a / (2 * math.sqrt(3))) ** 2)
        return 3 * self.a * apothem / 2
        
    def squareBase(self):
        return super().square()
        
    def height(self):
        return self.h
        
    def volume(self):
        return self.squareBase() * self.h / 3

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        # Площадь боковой поверхности правильной четырехугольной пирамиды
        apothem = math.sqrt(self.h ** 2 + (self.a / 2) ** 2)
        return 2 * (self.a + self.b) * apothem
        
    def squareBase(self):
        return super().square()
        
    def height(self):
        return self.h
        
    def volume(self):
        return self.squareBase() * self.h / 3

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        return 2 * (self.a * self.c + self.b * self.c)
        
    def squareBase(self):
        return super().square()
        
    def height(self):
        return self.c
        
    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)  # образующая
        return math.pi * self.r * l
        
    def squareBase(self):
        return super().square()
        
    def height(self):
        return self.h
        
    def volume(self):
        return self.squareBase() * self.h / 3

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h
        
    def dimension(self):
        return 3
        
    def perimeter(self):
        return None
        
    def square(self):
        return None
        
    def squareSurface(self):
        return self.perimeter() * self.h
        
    def squareBase(self):
        return super().square()
        
    def height(self):
        return self.h
        
    def volume(self):
        return self.squareBase() * self.h 
