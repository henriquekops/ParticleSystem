#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from __future__ import annotations
import os

# external dependencies
from numpy import array


class Vector2:

	def __init__(self, x:float = 0 , y:float = 0) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"(x={self.x}, y={self.y})"

	def __add__(self, other:Vector2):
		x = self.x + other.x
		y = self.y + other.y
		return Vector2(x, y) 

	def __mul__(self, factor:float):
		x = self.x * factor
		y = self.y * factor
		return Vector2(x, y)


class Vector3:

	def __init__(self, x:float = 0 , y:float = 0, z:float = 0) -> None:
		self.x = x
		self.y = y
		self.z = z

	def __str__(self) -> str:
		return f"(x={self.x}, y={self.y}, z={self.z})"


def fix_environment() -> None:
	try:
		del os.environ["DISPLAY"]
	except Exception:
		pass
