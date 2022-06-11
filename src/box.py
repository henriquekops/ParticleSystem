#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.object import Object
from src.utils import Vector2, Vector3

# external dependencies
from OpenGL.GL import (
	GL_LINE_LOOP,
	glBegin,
	glEnd,
	glVertex2f,
	glColor3f
)

class Box(Object):

	def __init__(self, position:Vector2=Vector2(0,0), width:int=1, 
	height:int=1, color:Vector3=Vector3(0,0,0)) -> None:
		self.position = position
		self.width = width
		self.height = height 
		self.color = color
		self.left = -0.1*(self.width/2)
		self.right = 0.1*(self.width/2)
		self.bottom = 0.1*(self.height/2)
		self.top = -0.1*(self.height/2)

	def draw(self):
		glColor3f(self.color.x, self.color.y, self.color.z)
		glBegin(GL_LINE_LOOP)
		glVertex2f(-0.1*(self.width/2), -0.1*(self.height/2)) #Left
		glVertex2f(0.1*(self.width/2), -0.1*(self.height/2)) #Top
		glVertex2f(0.1*(self.width/2), 0.1*(self.height/2)) #Right
		glVertex2f(-0.1*(self.width/2), 0.1*(self.height/2)) #Bottom
		glEnd()
