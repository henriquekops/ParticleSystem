#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import os


def fix_environment() -> None:
	try:
		del os.environ["DISPLAY"]
	except Exception:
		pass
