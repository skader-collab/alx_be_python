import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

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
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2

# Example usage:
if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    circle = Circle(7)
    
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Circle Area: {circle.area()}")

