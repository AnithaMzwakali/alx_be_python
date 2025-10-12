import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """
        This method should be overridden by all subclasses.
        Raises NotImplementedError if not implemented.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle (π × r²)."""
        return math.pi * (self.radius ** 2)
