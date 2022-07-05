#!/usr/bin/python3
"""
Add str method to Square inherited class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
            Class Square inherited from Rectangle
            Attributes:
                size(int): size of a square - private attribute.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
