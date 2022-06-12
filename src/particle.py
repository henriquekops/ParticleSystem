#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from copy import deepcopy

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
	cos,
	array
)
from OpenGL.GL import (
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glColor3f,
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
		self.borders()


	def __str__(self) -> str:
		return f"(position={self.position}, " + \
			f"velocity={self.velocity}, " + \
			f"acceleration={self.acceleration}, " + \
			f"color={self.color}, " + \
			f"radius={self.radius}, " + \
			f"self.ttl={self.ttl})"

	def move(self, dt:float):
		aux: Vector2 = deepcopy(self.velocity)
		self.velocity.sum(self.acceleration.mult(dt))
		self.position.sum(aux.mult(dt))
		self.borders()

	def borders(self):
		self.left = Vector2(self.position.x-self.radius, self.position.y)
		self.right = Vector2(self.position.x+self.radius, self.position.y)
		self.bottom = Vector2(self.position.x, self.position.y+self.radius)
		self.top = Vector2(self.position.x, self.position.y-self.radius)

	def draw(self) -> None:
		glColor3f(self.color.x, self.color.y, self.color.z)
		glBegin(GL_LINE_LOOP)
		for vertex in range(self.__N_VERTICES):
			angle = float(vertex) * 2.0 * pi / self.__N_VERTICES
			glVertex2f(
				self.position.x + (cos(angle) * self.radius),
				self.position.y + (sin(angle) * self.radius)
			)
		glEnd()
		glColor3f(1,0,0)
