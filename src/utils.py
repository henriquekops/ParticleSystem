#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os


class Vector2:

	def __init__(self, x:float = 0 , y:float = 0) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"(x={self.x}, y={self.y})"


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
