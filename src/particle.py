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
	GL_LINES,
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glColor3f,
	glVertex2f
)


class Particle(Object):

	__N_VERTICES = 30
	__MASS_MULTIPLIER = 0.2

	def __init__(self, position:Vector2 = Vector2(), velocity:Vector2 = Vector2(), 
		acceleration:Vector2 = Vector2(), color:Vector3 = Vector3(), radius:float=0, ttl:float=0) -> None:
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		self.color = color
		self.radius = radius
		self.ttl = ttl
		self.mass = self.radius * self.__MASS_MULTIPLIER
		self.__update_borders()

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
		self.__update_borders()
		# self.__draw_acceleration()
		self.__draw_velocity()

	def __update_borders(self):
		self.left = self.position.x-self.radius
		self.right = self.position.x+self.radius
		self.bottom = self.position.y+self.radius
		self.top = self.position.y-self.radius

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

	def __draw_acceleration(self):
		glColor3f(self.color.x, self.color.y, self.color.z)
		glBegin(GL_LINES)
		glVertex2f(self.position.x, self.position.y)
		glVertex2f(self.acceleration.x, self.acceleration.y)
		glEnd()

	def __draw_velocity(self):
		glColor3f(self.color.x, self.color.y, self.color.z)
		glBegin(GL_LINES)
		glVertex2f(self.position.x, self.position.y)
		glVertex2f(self.velocity.x, self.velocity.y)
		glEnd()
