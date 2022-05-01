#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_XSIZE = 400
WINDOW_YSIZE = 600
WINDOW_XPOSITION = 0
WINDOW_YPOSITION = 0

if __name__ == "__main__":

	try:
		del os.environ["DISPLAY"]
	except Exception:
		pass

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowPosition(WINDOW_XPOSITION, WINDOW_YPOSITION)
	glutInitWindowSize(WINDOW_XSIZE, WINDOW_YSIZE)
	glutCreateWindow("ParticleSystem")

	try:
		glutMainLoop
	except Exception as error:
		print(f"ERROR: {error}")
		sys.exit(1)
