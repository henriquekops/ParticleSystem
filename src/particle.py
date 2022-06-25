#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from copy import deepcopy
from math import pi

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
	# array,
	# sqrt
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

	def __init__(self, position:Vector2 = Vector2(), velocity:Vector2 = Vector2(), 
		acceleration:Vector2 = Vector2(), color:Vector3 = Vector3(), radius:float=0, ttl:float=0) -> None:
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		self.color = color
		self.radius = radius
		self.ttl = ttl
		self.mass = self.radius * pi ** 2
		self.__update_borders()

	def __str__(self) -> str:
		return f"(position={self.position}, " + \
			f"velocity={self.velocity}, " + \
			f"acceleration={self.acceleration}, " + \
			f"color={self.color}, " + \
			f"radius={self.radius}, " + \
			f"self.ttl={self.ttl})"

	def move(self, dt:float, tc:Vector2) -> float:
		# aux_vel2: Vector2 = deepcopy(self.velocity)
		# aux_acc: Vector2 = deepcopy(self.acceleration)
		# aux_acc2: Vector2 = deepcopy(self.acceleration)
		# vel_segment = None
		if tc:
			# v1 = aux_vel.sum(aux_acc.mult(tc))
			# v2 = aux_vel2.sum(aux_acc2.mult(dt))
			
			# vel_segment = self.__dist(v1, v2)
			
			self.position.sum(self.velocity.mult(tc))
			self.velocity.sum(self.acceleration.mult(tc))

			self.draw()

			self.velocity.mult(dt)
			self.velocity.y *= -1

			self.position.sum(self.velocity)
			self.velocity.sum(self.acceleration.mult(dt))

		else:
			self.position.sum(self.velocity.mult(dt))
			self.velocity.sum(self.acceleration.mult(dt))

		self.__update_borders()
		# self.__draw_acceleration()
		self.__draw_velocity()
	
	def next_position(self, dt: float):
		pos_aux = deepcopy(self.position)
		vel_aux = deepcopy(self.velocity)
		return pos_aux.sum(vel_aux.mult(dt))

	# def __dist(v1:Vector2, v2:Vector2) -> float:
	# 	# euclidean dist
	# 	return sqrt(((v2.x - v1.x)**2) + ((v2.y - v2.x)**2))

	def __update_borders(self):
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
