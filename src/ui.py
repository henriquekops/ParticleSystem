#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os

# external dependencies
from OpenGL.GLUT import (
	glutPostRedisplay,
	GLUT_KEY_DOWN,
	GLUT_KEY_UP,
	GLUT_KEY_LEFT,
	GLUT_KEY_RIGHT
)

SPACE = b' '
X = b'x'
P = b'p'
ESCAPE = b'\x1b'

collision_signal = True
show_acc_vec_signal = False
animation_signal = True
apply_up_force_signal=False
apply_down_force_signal=False
apply_right_force_signal=False
apply_left_force_signal=False

def reset_forces():
	global	apply_up_force_signal, \
			apply_down_force_signal, \
			apply_right_force_signal, \
			apply_left_force_signal

	apply_up_force_signal = False
	apply_down_force_signal = False
	apply_right_force_signal = False
	apply_left_force_signal = False

def special(*args):
	global 	apply_up_force_signal, \
			apply_down_force_signal, \
			apply_right_force_signal, \
			apply_left_force_signal

	key = args[0]
	
	if key == GLUT_KEY_UP:
		apply_up_force_signal = not apply_up_force_signal

	if key == GLUT_KEY_DOWN:
		apply_down_force_signal = not apply_down_force_signal

	if key == GLUT_KEY_RIGHT:
		apply_right_force_signal = not apply_right_force_signal

	if key == GLUT_KEY_LEFT:
		apply_left_force_signal = not apply_left_force_signal


def keyboard(*args):
	global	collision_signal, \
			show_acc_vec_signal, \
			animation_signal

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
