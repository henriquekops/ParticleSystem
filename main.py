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
from src.detector import CollisionDetector
from src.window import Window
from src.particle import Particle
from src.box import Box

# external dependencies
from OpenGL.GLUT import glutInit


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

	cd = CollisionDetector()

	p = Particle(
		velocity=Vector2(0.5, 0.7),
		acceleration=Vector2(0.1, 2.0),
		color=Vector3(1,1,1),
		radius=0.05
	)

	b = Box(
		height=19,
		width=19,
		color=Vector3(1,1,1)
	)

	# cd.handleParticleBoxCollision(b, p)

	window.display(b, p, cd)
