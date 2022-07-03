#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os

# external dependencies
from OpenGL.GLUT import glutPostRedisplay


SPACE = b' '
X = b'x'
P = b'p'
ESCAPE = b'\x1b'

collision_signal = True
show_acc_vec_signal = False
animation_signal = True


def keyboard(*args):
	global collision_signal, show_acc_vec_signal, animation_signal

	key = args[0]

	if key == ESCAPE:
		os._exit(0)

	if key == SPACE:
		collision_signal = not collision_signal

	if key == X:
		show_acc_vec_signal = not show_acc_vec_signal

	if key == P:
		animation_signal = not animation_signal

	glutPostRedisplay()
