#!/usr/bin/python3
"""
Add __str__ method in a class.
"""


class Rectangle:
    """
    Class that defines a rectangle.
    Attributes:
        width(int): width of a rectangle - private attribute.
        height(int): height of a rectangle - private attribute.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property that retrieves width"""
        return self.__width

    @property
    def height(self):
        """Property that retrieves height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter that sets the value of width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Property setter that sets the value of height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Public instance method that returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Standard method that prints the rectangle with character #"""

        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        i = 1
        while i <= self.__height:
            rectangle += "#" * self.__width
            if i < self.__height:
                rectangle += '\n'
            i += 1
        return 
