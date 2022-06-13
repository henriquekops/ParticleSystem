#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.box import Box
from src.detector import CollisionDetector
from src.particle import Particle
from src.object import Object

# external dependencies
from OpenGL.GL import (
	GL_PROJECTION,
	GL_COLOR_BUFFER_BIT,
	GL_MODELVIEW,
	glClear,
	glOrtho,
	glViewport,
	glMatrixMode,
	glLoadIdentity
)
from OpenGL.GLUT import (
	GLUT_RGBA,
	GLUT_ELAPSED_TIME,
	glutCreateWindow,
	glutInitDisplayMode,
	glutInitWindowSize,
	glutInitWindowPosition,
	glutDisplayFunc,
	glutIdleFunc,
	glutSwapBuffers,
	glutPostRedisplay,
	glutReshapeFunc,
	glutMainLoop,
	glutGet
)


class Window:

	__FPS = 100

	def __init__(self, title:str, height:int = 0, width:int = 0, x:int = 0, y:int = 0):
		self.title = title
		self.heigth = height
		self.width = width
		self.x = x
		self.y = y
		self.early = glutGet(GLUT_ELAPSED_TIME)
		self.dt = 0.0
		self.acc_dt = 0.0
	
	def __reset_view(self) -> None:
		glClear(GL_COLOR_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def create(self) -> None:
		glutInitDisplayMode(GLUT_RGBA)
		glutInitWindowPosition(self.x, self.y)
		glutInitWindowSize(self.width, self.heigth)
		glutCreateWindow(self.title)

	def display(self, b:Box, *p:Particle):
		self.b = b
		self.p = p
		glutDisplayFunc(self.__display)
		glutIdleFunc(self.__idle_view)
		# glutReshapeFunc(self.__reshape)
		glutMainLoop()

	def __idle_view(self):
		latest = glutGet(GLUT_ELAPSED_TIME)
		self.dt = (latest - self.early) / 1000.0
		self.early = latest
		self.acc_dt += self.dt
		if self.acc_dt > 1.0 / self.__FPS:
			self.acc_dt = 0.0
			glutPostRedisplay()

	# def __reshape(self, w:int, h:int) -> None:
	# 	"""
	# 	Redimension OpenGL window
	# 	"""
	# 	glMatrixMode(GL_PROJECTION)
	# 	glLoadIdentity()
	# 	glOrtho(-7, 7, -7, 7, 0, 1)
	# 	glViewport(0, 0, self.width, self.heigth)


	def __display(self) -> None:
		self.__reset_view()
		self.b.draw()
		for p in self.p:
			p.draw()
			p.move(self.dt)
			CollisionDetector.handleParticleBoxCollision(self.b, p)
		for p1 in self.p:
			for p2 in self.p:
				CollisionDetector.handleParticleParticleCollision(p1, p2)
		glutSwapBuffers()
