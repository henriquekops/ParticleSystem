#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import sys
from itertools import combinations
from typing import (
	Dict, 
	Callable
)

# project dependencies
from src import ui
from src.utils import Vector2, fix_environment
from src.window import Window
from src.particle import Particle
from src.box import Box
from src.detector import CollisionDetector
from src.spawn import SpawnPoint

# external dependencies
from OpenGL.GLUT import glutInit


def main(b:Box, spawn_point:SpawnPoint) -> Callable[[float], None]:
	def __main(dt:float) -> None:
		b.draw()
		particles:Dict[int, Particle] = spawn_point.particles
		if spawn_point.spawn_enable_signal:
			spawn_point.draw()
			spawn_point.spawn()
		
		p:Particle
		for p in particles.values():
			p.draw(ui.show_acc_vec_signal)
			if ui.animation_signal:
				if ui.kill_forces_signal:
					p.remove_force()
				if ui.apply_down_force_signal:
					p.remove_force()
					p.apply_force(Vector2(0,-50))
				if ui.apply_up_force_signal:
					p.remove_force()
					p.apply_force(Vector2(0,+50))
				if ui.apply_left_force_signal:
					p.remove_force()
					p.apply_force(Vector2(-50,0))
				if ui.apply_right_force_signal:
					p.remove_force()
					p.apply_force(Vector2(+50,0))
				p.move(dt)
				CollisionDetector.handleParticleBoxCollision(b, p)
		
		ui.reset_forces()
		
		if ui.collision_signal and len(particles) > 1:
			for p1, p2 in combinations(particles.values(), 2):
				CollisionDetector.handleParticleParticleCollision(p1, p2)

	return __main


if __name__ == "__main__":
	fix_environment()
	glutInit(sys.argv)

	window = Window(
		title="ParticleSystem",
		height=800,
		width=800,
		x=0,
		y=0
	)

	window.create(
		keyboard_func=ui.keyboard,
		special_func=ui.special
	)

	box = Box(
		height=19,
		width=19
	)

	spawn_point = SpawnPoint(
		box=box,
		spawn_num=5
	)

	window.display(main(box, spawn_point))
