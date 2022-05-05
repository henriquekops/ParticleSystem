#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import sys

# project dependencies
from src.utils import (
	Vector2, 
	Vector3, 
	fix_environment
)
from src.window import Window
from src.particle import Particle
from src.ui import keyboard

# external dependencies
from OpenGL.GLUT import (
	glutInit,
	glutMainLoop,
	glutKeyboardFunc
)


if __name__ == "__main__":
	fix_environment()
	glutInit(sys.argv)

	window = Window(
		title="ParticleSystem",
		height=400,
		width=400,
		x=0,
		y=0
	)

	window.create()

	p = Particle(
		color=Vector3(1,1,1)
	)

	print(p)

	window.display(p)

	glutKeyboardFunc(keyboard)
	glutMainLoop()
