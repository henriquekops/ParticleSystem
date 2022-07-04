#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from __future__ import annotations
from typing import Iterable
import os
from math import sqrt


class Vector2:

	def __init__(self, x:float = 0 , y:float = 0) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"Vector2(x={self.x}, y={self.y})"

	def __add__(self, other:Vector2):
		x = self.x + other.x
		y = self.y + other.y
		return Vector2(x, y)
	
	# TODO: change sub to actual subtraction and change current logic to a custom dist() method
	def __sub__(self, other:Vector2):
		# https://en.wikipedia.org/wiki/Euclidean_distance
		return sqrt(((other.x - self.x)**2) + (other.y - self.y)**2)

	def __mul__(self, factor:float):
		x = self.x * factor
		y = self.y * factor
		return Vector2(x, y)

	# TODO: overwrite __iter__
	# TODO: implement dot product
 

class Color:

	def __init__(self, r:float = 1 , g:float = 1, b:float = 1) -> None:
		self.r = r
		self.g = g
		self.b = b

	def __str__(self) -> str:
		return f"Color(r={self.r}, g={self.g}, b={self.b})"
	
	def __iter__(self) -> Iterable:
		return iter((self.r, self.g, self.b))


def fix_environment() -> None:
	try:
		del os.environ["DISPLAY"]
	except Exception:
		pass
