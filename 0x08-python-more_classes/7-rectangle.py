#!/usr/bin/python3
'''module'''


class Rectangle:
    '''define class'''

    number_of_instances = 0
    '''int number'''

    print_symbol = '#'
    '''type print_symbol'''

    def __init__(self, width=0, height=0):
        '''Constructor
        
        Args:
        	width: of rectangle
            height: of rectangle'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Property
        
        Raises:
        	TypeError: if is not integer
            ValueErrorJ: if is less than 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if  not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return"""
        if not self.width or not self.height:
          return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height) [:-1]

    def __repr__(self):
        '''returns'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''print message'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
