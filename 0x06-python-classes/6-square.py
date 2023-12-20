#!/usr/bin/python3
"""Square"""


class Square:
	"""Define a Square"""

	def __init__(self, size=0, position=(0, 0)):
		"""Initialize square
		Args:
			size (int): The size of the new Square
			position (int, int): The position of the new square
		"""
		self.size = size
		self.position = position

	@property
	def size(self):
		"""get set current size of square"""
		return self.__size

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@property
	def position(self):
		"""get set current position of square"""
		return self.__position

	@position.setter
	def position(self, value):
		if (not isinstance(value, tuple) or
	  			len(value) != 2 or
				not all(isinstance(num, int) for num in value) or
				not all(num >= 0 for num in value)):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		"""print current area of square"""
		return self.__size * self.__size

	def my_print(self):
		"""print square with # character"""
		if self._size == 0:
			print("")
			return

		[print("") for i in range(0, self.__position[1])]
		for i in range(0, self.__size):
			[print(" ", end="") for i in range(0, self.__position[0])]
			[print("#", end="") for a in range(0, self.__size)]
			print("")
