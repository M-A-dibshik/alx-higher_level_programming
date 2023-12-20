#!/usr/bin/python3
"""Square"""


class Square:
    """Define"""

    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    @property
    def size(self):
        """property for length of a side of square

        Raises:
                TypeError: if size is not integer
                ValueError: is size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Args of this square

        Return:
                The size square
        """
        return self.__size**2

    def my_print(self):
        """print square"""
        for a in range(self.size):
            for b in range(self.size):
                print("#", end="\n" if b is self.size - 1 and a != b else "")
        print()
