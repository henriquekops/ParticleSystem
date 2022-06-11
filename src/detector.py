#!/usr/bin/env python3
#-*- coding: utf-8 -*-


# project dependencies
from src.box import Box
from src.particle import Particle


class CollisionDetector():

	def handleParticleBoxCollision(self, b: Box, p:Particle) -> None:
		if p.left.x <= b.left or p.right.x >= b.right:
			p.velocity.x *= -1
		if p.bottom.y <= b.bottom or p.top.y >= b.top:
			p.velocity.y *= -1
