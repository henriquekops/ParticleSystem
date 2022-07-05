#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from .box import Box
from .particle import Particle


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
			return p1.velocity -  (2 * p2.mass) / (p1.mass + p2.mass) * \
				(p1.velocity - p2.velocity).dot(p1.position - p2.position) / \
				(p1.position - p2.position).norm() ** 2 * (p1.position - p2.position)

		if p1 != p2:
			if (p1.position-p2.position).norm()*0.96 <= (p1.radius+p2.radius):
				v1 = compute_velocity(p1,p2)
				v2 = compute_velocity(p2,p1)
				p1.velocity.x, p1.velocity.y = v1
				p2.velocity.x, p2.velocity.y = v2
