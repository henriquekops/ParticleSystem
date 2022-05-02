#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.object import Object
from src.utils import (
	Vector2,
	Vector3
)

# external dependencies
from numpy import (
	pi,
	sin,
	cos
)
from OpenGL.GL import (
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glVertex2f
)


class Particle(Object):

	__N_VERTICES = 30

	def __init__(self, position:Vector2 = Vector2(0,0), velocity:Vector2 = Vector2(0,0), 
		acceleration:Vector2 = Vector2(0,0), color:Vector3 = Vector3(0,0,0), 
		radius:float = 0.5, ttl:float = 0.5) -> None:
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		self.color = color
		self.radius = radius
		self.ttl = ttl

	def __str__(self):
		return f"(position={self.position}, " + \
			f"velocity={self.velocity}, " + \
			f"acceleration={self.acceleration}, " + \
			f"color={self.color}, " + \
			f"radius={self.radius}, " + \
			f"self.ttl={self.ttl})"

	def draw(self) -> None:
		glBegin(GL_LINE_LOOP)
		for vertex in range(self.__N_VERTICES):
			angle = float(vertex) * 2.0 * pi / self.__N_VERTICES
			glVertex2f(
				self.position.x + (cos(angle) * self.radius),
				self.position.y + (sin(angle) * self.radius)
			)
		glEnd()
