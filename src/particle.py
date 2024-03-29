#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from .utils import (
	Object,
	Vector2,
	Color
)

# external dependencies
from numpy import (
	pi,
	sin,
	cos
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
	__VEL_THRESHOLD = 10.0

	def __init__(self, id:int = 0, position:Vector2 = Vector2(), velocity:Vector2 = Vector2(), 
		acceleration:Vector2 = Vector2(), color:Color = Color(), radius:float=0, ttl:float=0) -> None:
		self.id = id
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		self.color = color
		self.radius = radius
		self.ttl = ttl
		self.mass = self.radius * self.__MASS_MULTIPLIER
		self.__update_borders()

	def __str__(self) -> str:
		return f"(id={self.id}, "+ \
			f"position={self.position}, " + \
			f"velocity={self.velocity}, " + \
			f"acceleration={self.acceleration}, " + \
			f"color={self.color}, " + \
			f"radius={self.radius}, " + \
			f"self.ttl={self.ttl})"

	def move(self, dt:float) -> None:
		self.position += (self.velocity * dt) # sf = si + v * dt (displacement)
		self.velocity += (self.acceleration * dt) # vf = vi + a * dt (UVRM velocity variation with constant acceleration)
		self.__truncate_velocity()
		self.__update_borders()

	def __truncate_velocity(self) -> None:
		if self.velocity.x > self.__VEL_THRESHOLD:
			self.velocity.x = self.__VEL_THRESHOLD
		elif self.velocity.x < -self.__VEL_THRESHOLD:
			self.velocity.x = -self.__VEL_THRESHOLD
		if self.velocity.y > self.__VEL_THRESHOLD:
			self.velocity.y = self.__VEL_THRESHOLD
		elif self.velocity.y < -self.__VEL_THRESHOLD:
			self.velocity.y = -self.__VEL_THRESHOLD

	def apply_force(self, force:Vector2) -> None:
		self.acceleration += force
	
	def remove_force(self) -> None:
		self.acceleration = Vector2()

	def __update_borders(self) -> None:
		self.left = self.position.x-self.radius
		self.right = self.position.x+self.radius
		self.bottom = self.position.y+self.radius
		self.top = self.position.y-self.radius

	def draw(self, draw_acc_vel_signal:bool) -> None:
		glColor3f(*self.color)
		glBegin(GL_LINE_LOOP)
		for vertex in range(self.__N_VERTICES):
			angle = float(vertex) * 2.0 * pi / self.__N_VERTICES
			glVertex2f(
				self.position.x + (cos(angle) * self.radius),
				self.position.y + (sin(angle) * self.radius)
			)
		glEnd()
		if draw_acc_vel_signal:
			self.__draw_acceleration()
			self.__draw_velocity()

	def __draw_acceleration(self) -> None:
		glColor3f(*self.color)
		glBegin(GL_LINES)
		glVertex2f(*self.position)
		glVertex2f(*self.acceleration)
		glEnd()

	def __draw_velocity(self) -> None:
		glColor3f(*self.color)
		glBegin(GL_LINES)
		glVertex2f(*self.position)
		glVertex2f(*self.velocity)
		glEnd()
