#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from .utils import (
	Color,
	Object,
	Vector2
)

# external dependencies
from OpenGL.GL import (
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glVertex2f,
	glColor3f
)

class Box(Object):

	def __init__(self, position:Vector2=Vector2(), width:int=1, 
	height:int=1, color:Color=Color()) -> None:
		self.position = position
		self.width = width
		self.height = height 
		self.color = color
		self.left = -0.1*(self.width/2)
		self.right = 0.1*(self.width/2)
		self.bottom = 0.1*(self.height/2)
		self.top = -0.1*(self.height/2)

	def draw(self) -> None:
		glColor3f(*self.color)
		glBegin(GL_LINE_LOOP)
		glVertex2f(self.left, self.top) # top left
		glVertex2f(self.right, self.top) # top right
		glVertex2f(self.right, self.bottom) # bottom right
		glVertex2f(self.left, self.bottom) # bottom left
		glEnd()
