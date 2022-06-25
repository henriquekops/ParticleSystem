#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from src.box import Box
from src.particle import Particle

# external dependencies
import numpy as np

# from utils import Vector2


class CollisionDetector():

	@staticmethod
	def handleParticleBoxCollision(b: Box, p:Particle, dt:float) -> float:
		# continuous collision detection
		x0 = p.position.x
		y0 = p.position.y
		next_pos = p.next_position(dt)
		x1 = next_pos.x
		y1 = next_pos.y

		tc = None

		if y1 >= b.bottom:
			tc = ((b.bottom + p.radius) - y0) / (y1 - y0) 
		
		# temp code
		if p.top.y <= b.top:
			p.velocity.y *= -1
		if p.left.x <= b.left or p.right.x >= b.right:
			p.velocity.x *= -1
		
		# new code

		# if y1 <= b.top:
		# 	tc = ((b.top + p.radius) - y0) / (y1 - y0)
		# if x1 <= b.left:
		# 	tc = ((b.left + p.radius) - x0) / (x1 - x0)
		# if x1 >= b.right:
		# 	tc = ((b.right + p.radius) - x0) / (x1 - x0)


		# trash code

		# linear interpolation
		# xt = tc * x0 + (1-tc) * x1
		# yt = tc * y0 + (1-tc) * y1
		# point of collision: (xt, yt)
		# return Vector2(xt, yt)

		return tc

		# old code

		# if p.bottom.y >= b.bottom or p.top.y <= b.top:
		# 	p.velocity.y *= -1
		# if p.left.x <= b.left or p.right.x >= b.right:
		# 	p.velocity.x *= -1

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

	
