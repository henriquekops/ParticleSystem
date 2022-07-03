#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import sys
from itertools import combinations
from typing import (
	List, 
	Callable
)

# project dependencies
from src import ui
from src.utils import fix_environment
from src.window import Window
from src.particle import Particle
from src.box import Box
from src.detector import CollisionDetector
from src.spawn import SpawnPoint

# external dependencies
from OpenGL.GLUT import glutInit


def main(b:Box, ps:List[Particle]) -> Callable[[float], None]:
	def __main(dt:float) -> None:
		b.draw()
		for p in ps:
			p.draw(ui.show_acc_vec_signal)
			if ui.animation_signal:
				p.move(dt)
				CollisionDetector.handleParticleBoxCollision(b, p)
		if ui.collision_signal:
			for p1, p2 in combinations(ps, 2):
				CollisionDetector.handleParticleParticleCollision(p1, p2)
	return __main


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

	window.create(keyboard_func=ui.keyboard)

	b = Box(
		height=19,
		width=19
	)

	spawn_point = SpawnPoint()

	particles = spawn_point.spawn_many(5, b)

	window.display(main(b, particles))
