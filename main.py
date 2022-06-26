#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import sys
from itertools import combinations
from typing import List

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
		for p1, p2 in combinations(ps, 2):
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
		name="p1(red)",
		velocity=Vector2(7.0, -7.0),
		acceleration=Vector2(1.0, -2.0),
		color=Vector3(1,0,0),
		radius=0.13
	)

	p2 = Particle(
		name="p2(green)",
		position=Vector2(0.9, 0.9),
		velocity=Vector2(9.0, -8.0),
		acceleration=Vector2(3.0, 2.0),
		color=Vector3(0,1,0),
		radius=0.1
	)

	p3 = Particle(
		name="p3(blue)",
		position=Vector2(0.5, 0.5),
		velocity=Vector2(10.0, -1.0),
		acceleration=Vector2(3.0, 2.0),
		color=Vector3(0,0,1),
		radius=0.08
	)

	p4 = Particle(
		name="p4(yellow)",
		position=Vector2(0.4, 0.2),
		velocity=Vector2(8.0, -2.0),
		acceleration=Vector2(3.0, 2.0),
		color=Vector3(1,1,0),
		radius=0.08
	)

	b = Box(
		height=19,
		width=19,
		color=Vector3(1,1,1)
	)

	window.display(main(b, p1, p2, p3, p4))
