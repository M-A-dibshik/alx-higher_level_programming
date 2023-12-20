#!/usr/bin/python3
"""Square"""


class Square:
    """Define"""

    def __init__(self, size=0):
        """Constr

        Args:
                size: length of a side of square
        """
        self.size = size

    @property
    def size(self):
        """property for the length of a side of square

        Raises:
                TypeError: if size is not integer
                ValueError: is size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.size = value

    def area(self):
        """Args of square

        Return:
                the size square
        """
        return self.__size ** 2
