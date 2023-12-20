#!/usr/bin/python3
"""Square"""


class Square:
    """Define"""

    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square"""
        return self.__size ** 2
