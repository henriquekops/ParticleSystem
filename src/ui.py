#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os

# external dependencies
from OpenGL.GLUT import glutPostRedisplay


ESCAPE = b'\x1b'


def keyboard(*args):
	key = args[0]
	if key == ESCAPE:
		os._exit(0)
	glutPostRedisplay()
