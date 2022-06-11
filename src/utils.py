#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from __future__ import annotations
import os


class Vector2:

	def __init__(self, x:float = 0 , y:float = 0) -> None:
		self.x = x
		self.y = y

	def __str__(self):
		return f"(x={self.x}, y={self.y})"

	def mult(self, factor:float):
		if factor > 0:
			self.x *= factor
			self.y *= factor
		return self

	def sum(self, vector2:Vector2):
		self.x += vector2.x
		self.y += vector2.y
		return self


class Vector3:

	def __init__(self, x:float = 0 , y:float = 0, z:float = 0) -> None:
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return f"(x={self.x}, y={self.y}, z={self.z})"


def fix_environment() -> None:
	try:
		del os.environ["DISPLAY"]
	except Exception:
		pass
