#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.box import Box
from src.detector import CollisionDetector
from src.particle import Particle
# from src.object import Object

# built-in dependencies
import time

# external dependencies
from OpenGL.GL import (
	GL_COLOR_BUFFER_BIT,
	GL_DEPTH_BUFFER_BIT,
	GL_MODELVIEW,
	glClear,
	glMatrixMode,
	glLoadIdentity
)
from OpenGL.GLUT import (
	GLUT_RGBA,
	glutCreateWindow,
	glutInitDisplayMode,
	glutInitWindowSize,
	glutInitWindowPosition,
	glutDisplayFunc,
	glutIdleFunc,
	glutSwapBuffers,
	glutPostRedisplay,
	glutReshapeFunc,
	glutMainLoop
)


class Window:

	def __init__(self, title:str, height:int = 0, width:int = 0, x:int = 0, y:int = 0):
		self.title = title
		self.heigth = height
		self.width = width
		self.x = x
		self.y = y
		self.init_time = time.time()
		self.acc_dt = 0
		self.dt = 0
	
	def __reset_view(self) -> None:
		glClear(GL_COLOR_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def create(self) -> None:
		glutInitDisplayMode(GLUT_RGBA)
		glutInitWindowPosition(self.x, self.y)
		glutInitWindowSize(self.width, self.heigth)
		glutCreateWindow(self.title)

	# def display(self, *objects:Object) -> None:
	# 	glutDisplayFunc(self.__reset_view)
	# 	glutIdleFunc(self.__idle_view)
	# 	for object in objects:
	# 		object.draw()
	# 	glutSwapBuffers()

	def display(self, b:Box, p:Particle, cd: CollisionDetector):
		self.b = b
		self.p = p
		self.cd = cd
		glutDisplayFunc(self.__display)
		glutIdleFunc(self.__idle_view)
		# glutReshapeFunc()
		glutMainLoop()

	def __idle_view(self):
		now = time.time()
		dt = now - self.init_time
		self.init_time = now
		self.acc_dt += dt
		if self.acc_dt > 1.0 / 30:
			self.dt = self.acc_dt
			self.acc_dt = 0
			glutPostRedisplay()

	def __display(self) -> None:
		self.__reset_view()
		self.p.draw()
		self.b.draw()
		self.cd.handleParticleBoxCollision(self.b, self.p)
		self.p.move(self.dt)
		glutSwapBuffers()
