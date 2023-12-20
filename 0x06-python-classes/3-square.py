#!/usr/bin/python3
"""Square"""


class Square:
    """Define"""

    def __init__(self, size=0):
        """Constr

        Args:
            size: length os side of square

        Raises:
                TypeError: if size not integer
                ValueError: if size less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square

        Return:
                size square
        """
        return self.__size ** 2
