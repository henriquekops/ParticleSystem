#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import sys

# project dependencies
from src.utils import fix_environment
from src.window import Window

# external dependencies
from OpenGL.GLUT import (
	glutInit,
	glutMainLoop
)


if __name__ == "__main__":
	fix_environment()
	glutInit(sys.argv)
	window = Window(
		"ParticleSystem",
		400,
		600,
		0,
		0
	)
	window.create()
	window.display()
	glutMainLoop()
