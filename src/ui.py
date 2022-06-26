#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os

# external dependencies
from OpenGL.GLUT import glutPostRedisplay


SPACE = b' '
ESCAPE = b'\x1b'

collision_signal = True

def keyboard(*args):
	global collision_signal

	key = args[0]

	if key == ESCAPE:
		os._exit(0)

	if key == SPACE:
		collision_signal = not collision_signal

	glutPostRedisplay()
