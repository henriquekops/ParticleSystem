#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from random import uniform
from typing import List

# project dependencies
from .particle import Particle
from .box import Box
from .utils import (
	Vector2, 
	Color
)

class SpawnPoint:

	__BORDER_THRESHOLD = 0.01

	def __init__(self, x:float=0, y:float=0, width:int=0, height:int=0) -> None:
		pass

	def __set_axis(self, r:float, min:float, max:float):
		k = uniform(min, max)
		if k < 0: 
			k += (r+self.__BORDER_THRESHOLD)
		else: 
			k -= (r+self.__BORDER_THRESHOLD)
		return k

	def __set_pos(self, r:float, b:Box):
		x = self.__set_axis(r, b.right, b.left)
		y = self.__set_axis(r, b.top, b.bottom)
		return Vector2(x, y)

	def __set_radius(self) -> float:
		return uniform(0.05, 0.15)

	def __set_vel(self):
		x = uniform(2.0, 4.0)
		y = uniform(2.0, 4.0)
		return Vector2(x, y)
	
	def __set_accel(self):
		return Vector2(0.0, 0.0)

	def __set_color(self):
		r = uniform(0.5,1.0)
		g = uniform(0.5,1.0)
		b = uniform(0.5,1.0)
		return Color(r, g, b)

	def spawn(self, id:int, b:Box) -> Particle:
		r = self.__set_radius()
		return Particle(
			id=id,
			position=self.__set_pos(r,b),
			velocity=self.__set_vel(),
			acceleration=self.__set_accel(),
			color=self.__set_color(),
			radius=r
		)

	def spawn_many(self, n:int, b:Box) -> List[Particle]:
		particles = list()
		for i in range(n):
			particles.append(self.spawn(i, b))
		return particles
