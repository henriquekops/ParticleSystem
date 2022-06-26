#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.box import Box
from src.particle import Particle

# external dependencies
import numpy as np


class CollisionDetector():

	@staticmethod
	def handleParticleBoxCollision(b: Box, p:Particle) -> None:
		# discrete collision detection
		if p.bottom >= b.bottom:
			p.velocity.y *= -1
			p.position.y = b.bottom - p.radius
		if p.top <= b.top:
			p.velocity.y *= -1
			p.position.y = b.top + p.radius
		if p.left <= b.left:
			p.velocity.x *= -1
			p.position.x = b.left + p.radius
		if p.right >= b.right:
			p.velocity.x *= -1
			p.position.x = b.right - p.radius

	@staticmethod
	def handleParticleParticleCollision(p1: Particle, p2:Particle) -> None:
		
		def compute_velocity(p1: Particle, p2: Particle):
			# elastic collision: https://en.wikipedia.org/wiki/Elastic_collision
			v1 = np.array([p1.velocity.x, p1.velocity.y])
			v2 = np.array([p2.velocity.x, p2.velocity.y])
			x1 = np.array([p1.position.x, p1.position.y])
			x2 = np.array([p2.position.x, p2.position.y])
			m1 = p1.mass
			m2 = p2.mass
			return v1 - (2 * m2 / (m1 + m2)) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2) ** 2 * (x1 - x2)
		
		if p1 != p2:
			if abs(p1.position.x - p2.position.x) <= (p1.radius+p2.radius) \
			and abs(p1.position.y - p2.position.y) <= (p1.radius+p2.radius):
				v1 = compute_velocity(p1,p2)
				p1.velocity.x = v1[0]
				p1.velocity.y = v1[1]
				v2 = compute_velocity(p2,p1)
				p2.velocity.x = v2[0]
				p1.velocity.y = v2[1]

	
