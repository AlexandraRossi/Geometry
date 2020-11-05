"""Geometry module provides classes to help determing geometric calculations"""
import math
class Circle:
    #constructor
    def __init__(self, radius: float):
        #Radius; all numbers in int form passed in will be converted to positive numbers
        self.radius = abs(radius)


    def __str__(self) -> str :
        return f"Circle with Radius {self.radius}"
    def area(self) -> float:
        #calculates area of circle with int; cannot be negative
        return math.pi * self.radius ** 2


    def circumference(self) -> float:
        #calculaes circumference, cannot be negative
        return math.pi * self.radius * 2


class Rectangle:
    #constructor
    def __init__(self, length: float, width: float):
        #constructs the rectangle with length and width as ints; all numbers passed in will be converted to positive numbers via absolute value
        self.width = abs(width)
        self.length = abs(length)

        pass
    def __str__(self) -> str :
        return f"rectangle with Radius {self.radius}"
    def area(self) -> float:
        #calculates area of rectangle; cannot be negative
        return math.pi * self.radius ** 2


    def perimeter(self) -> float:
        #calculates perimeter of rectangle, cannot be negative
        return (2 * width) + (2 * length)

