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
from src.ui import keyboard
from src.window import Window
from src.particle import Particle
from src.box import Box
from src.detector import CollisionDetector

# external dependencies
from OpenGL.GLUT import (
	glutInit,
	glutKeyboardFunc
)


def main(b:Box, *ps:Particle):
	def __main(dt:float):
		b.draw()
		for p in ps:
			p.draw()
			p.move(dt)
			CollisionDetector.handleParticleBoxCollision(b, p)
		for p1, p2 in zip(ps, ps[1:]):
			CollisionDetector.handleParticleParticleCollision(p1, p2)
	return __main


if __name__ == "__main__":
	fix_environment()
	glutInit(sys.argv)
	glutKeyboardFunc(keyboard)

	window = Window(
		title="ParticleSystem",
		height=400,
		width=400,
		x=0,
		y=0
	)

	window.create()

	p1 = Particle(
		velocity=Vector2(2.0, -2.0),
		acceleration=Vector2(0.0, -5.0),
		color=Vector3(1,0,0),
		radius=0.1
	)

	p2 = Particle(
		position=Vector2(0.3, 0.3),
		velocity=Vector2(2.0, -2.75),
		acceleration=Vector2(0.0, -3.0),
		color=Vector3(0,1,0),
		radius=0.1
	)

	b = Box(
		height=19,
		width=19,
		color=Vector3(1,1,1)
	)

	window.display(main(b, p1, p2))
