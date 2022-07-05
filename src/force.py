#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from .particle import Particle
from .utils import Vector2
from . import ui

class Force:

	def __init__(self, intensity) -> None:
		self.down_force = Vector2(0,-intensity)
		self.up_force = Vector2(0,intensity)
		self.left_force = Vector2(-intensity, 0)
		self.right_force = Vector2(intensity, 0)

	def apply_forces(self, p:Particle):
		if ui.kill_forces_signal:
			p.remove_force()
		if ui.apply_down_force_signal:
			p.remove_force()
			p.apply_force(self.down_force)
		if ui.apply_up_force_signal:
			p.remove_force()
			p.apply_force(self.up_force)
		if ui.apply_left_force_signal:
			p.remove_force()
			p.apply_force(self.left_force)
		if ui.apply_right_force_signal:
			p.remove_force()
			p.apply_force(self.right_force)
