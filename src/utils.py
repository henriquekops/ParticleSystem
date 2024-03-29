#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from __future__ import annotations
from typing import Iterable
from math import sqrt
import os
import platform


class Object:

	def draw(self) -> None:
		pass


class Vector2:

	def __init__(self, x:float = 0 , y:float = 0) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"Vector2(x={self.x}, y={self.y})"

	def __add__(self, other:Vector2) -> Vector2:
		x = self.x + other.x
		y = self.y + other.y
		return Vector2(x, y)

	def __mul__(self, factor:float) -> Vector2:
		x = self.x * factor
		y = self.y * factor
		return Vector2(x, y)

	def __rmul__(self, factor:float) -> Vector2:
		x = self.x * factor
		y = self.y * factor
		return Vector2(x, y)

	def __sub__(self, other:Vector2) -> Vector2:
		x = self.x - other.x
		y = self.y - other.y
		return Vector2(x, y)

	def __rsub__(self, factor:float) -> Vector2:
		x = self.x - factor
		y = self.y - factor
		return Vector2(x, y)

	def __rtruediv__(self, factor:float) -> Vector2:
		x = self.x / factor
		y = self.y / factor
		return Vector2(x, y)
	
	def __iter__(self) -> Iterable:
		return iter((self.x, self.y))

	def dist(self, other:Vector2) -> float:
		# https://en.wikipedia.org/wiki/Euclidean_distance
		return sqrt(((other.x - self.x)**2) + (other.y - self.y)**2)

	def norm(self) -> float:
		# https://en.wikipedia.org/wiki/Norm_(mathematics)
		return sqrt((self.x**2) + (self.y**2))
 
	def dot(self, other:Vector2) -> float:
		# https://en.wikipedia.org/wiki/Dot_product
		return ((self.x * other.x) + (self.y * other.y))


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
		if 'windows' in platform.platform().lower():
			del os.environ["DISPLAY"]
	except Exception:
		pass
