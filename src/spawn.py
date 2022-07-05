#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from random import uniform
from turtle import position
from typing import List

# project dependencies
from .particle import Particle
from .box import Box
from .utils import (
	Object,
	Vector2, 
	Color
)

# external dependencies
from OpenGL.GL import (
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glVertex2f,
	glColor3f
)


class SpawnPoint(Object):

	__BORDER_THRESHOLD = 0.15
	__MIN_RADIUS = 0.05
	__MAX_RADIUS = 0.15
	__MIN_VELOCITY = 2.0
	__MAX_VELOCITY = 4.0
	__MIN_RGB = 0.5
	__MAX_RGB = 1.0

	def __init__(self, box:Box, spawn_num:int=1, position:Vector2 = Vector2(), color:Color = Color()) -> None:
		self.position = position
		self.color = color
		self.size = self.__MAX_RADIUS
		self.spawn_enable_signal = True
		self.spawn_num = spawn_num
		self.box = box
		self.particles = dict()
		self.delay = 0.5
		self.dt_acc = 0.0

	def __set_radius(self) -> float:
		return uniform(self.__MIN_RADIUS, self.__MAX_RADIUS)

	def __set_vel(self):
		x = uniform(self.__MIN_VELOCITY, self.__MAX_VELOCITY)
		y = uniform(self.__MIN_VELOCITY, self.__MAX_VELOCITY)
		return Vector2(x, y)
	
	def __set_accel(self):
		return Vector2(0.0, 0.0)

	def __set_color(self):
		r = uniform(self.__MIN_RGB, self.__MAX_RGB)
		g = uniform(self.__MIN_RGB, self.__MAX_RGB)
		b = uniform(self.__MIN_RGB, self.__MAX_RGB)
		return Color(r, g, b)

	def __spawn(self) -> Particle:
		return Particle(
			id=self.spawn_num,
			position=self.position,
			velocity=self.__set_vel(),
			acceleration=self.__set_accel(),
			color=self.__set_color(),
			radius=self.__set_radius()
		)

	def spawn(self) -> List[Particle]:
		if self.spawn_num == 0:
			self.spawn_enable_signal = False
		elif len(self.particles) > 0:
			particle:Particle = self.particles.get(self.spawn_num+1)
			if (particle.position.dist(self.position)) > ((self.size/2) + particle.radius + self.__BORDER_THRESHOLD):
				self.particles.update({self.spawn_num: self.__spawn()})
				self.spawn_num -= 1
		else:
			self.particles.update({self.spawn_num: self.__spawn()})
			self.spawn_num -= 1


	def draw(self) -> None:
		line_size = self.size/2
		glColor3f(*self.color)
		glBegin(GL_LINE_LOOP)
		glVertex2f(-line_size, -line_size) # top left
		glVertex2f(line_size, -line_size) # top right
		glVertex2f(line_size, line_size) # bottom right
		glVertex2f(-line_size, line_size) # bottom left
		glEnd()
