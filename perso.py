"""
module responsible for creating the characters of the game
"""
#!/usr/bin/python3
#coding: utf-8

import random
import pygame
from pygame.locals import *
from constantes import *

class Perso:
	"""constructor
	"""
	def __init__(self, image, niveau):

		self.personnage = pygame.image.load(image).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.niveau = niveau

	def move(self, direction):
		"""method to move the character
		"""

		# moving to right
		if direction == 'droite':
			if self.case_x < (NOMBRE_SPRITE_FACE - 1):
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and \
					self.niveau.structure[self.case_y][self.case_x+1] != 'x':
					self.case_x += 1
					self.x = self.case_x * TAILLE_SPRITE
		# moving to left
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and \
					self.niveau.structure[self.case_y][self.case_x-1] != 'x':
					self.case_x -= 1
					self.x = self.case_x * TAILLE_SPRITE
		# moving to up
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and \
					self.niveau.structure[self.case_y-1][self.case_x] != 'x':
					self.case_y -= 1
					self.y = self.case_y * TAILLE_SPRITE
		# moving to down
		if direction == 'bas':
			if self.case_y < (NOMBRE_SPRITE_FACE - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and \
					self.niveau.structure[self.case_y+1][self.case_x] != 'x':
					self.case_y += 1
					self.y = self.case_y * TAILLE_SPRITE
			