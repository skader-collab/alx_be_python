# polymorphism_demo.py
import math

class Shape:
    def area(self):
        raise NotImplementedError("area() method must be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Example usage (demonstrating polymorphism)
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Rectangle(3, 8),
        Circle(4)
    ]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.area()}")

