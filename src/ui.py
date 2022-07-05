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
K = b'k'
ESCAPE = b'\x1b'

collision_signal = True
show_acc_vec_signal = False
animation_signal = True
apply_up_force_signal=False
apply_down_force_signal=False
apply_right_force_signal=False
apply_left_force_signal=False
kill_forces_signal=False


def reset_forces() -> None:
	global	apply_up_force_signal, \
			apply_down_force_signal, \
			apply_right_force_signal, \
			apply_left_force_signal, \
			kill_forces_signal

	apply_up_force_signal = False
	apply_down_force_signal = False
	apply_right_force_signal = False
	apply_left_force_signal = False
	kill_forces_signal = False


def special(*args) -> None:
	global 	apply_up_force_signal, \
			apply_down_force_signal, \
			apply_right_force_signal, \
			apply_left_force_signal

	key = args[0]
	
	if key == GLUT_KEY_UP:
		apply_up_force_signal = True

	if key == GLUT_KEY_DOWN:
		apply_down_force_signal = True

	if key == GLUT_KEY_RIGHT:
		apply_right_force_signal = True

	if key == GLUT_KEY_LEFT:
		apply_left_force_signal = True


def keyboard(*args) -> None:
	global	collision_signal, \
			show_acc_vec_signal, \
			animation_signal, \
			kill_forces_signal

	key = args[0]

	if key == ESCAPE:
		os._exit(0)

	if key == SPACE:
		collision_signal = not collision_signal

	if key == X:
		show_acc_vec_signal = not show_acc_vec_signal

	if key == P:
		animation_signal = not animation_signal

	if key == K:
		kill_forces_signal = True

	glutPostRedisplay()
