#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.box import Box
from src.particle import Particle


class CollisionDetector():

	@staticmethod
	def handleParticleBoxCollision(b: Box, p:Particle) -> None:
		if p.bottom.y >= b.bottom or p.top.y <= b.top:
			p.velocity.y *= -1
		if p.left.x <= b.left or p.right.x >= b.right:
			p.velocity.x *= -1
