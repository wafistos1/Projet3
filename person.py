"""
module responsible for creating the characters of the game
"""
#!/usr/bin/python3
#coding: utf-8


import pygame
from pygame.locals import *
from constantes import *

class Perso:
    """constructor
    """
    def __init__(self, image, lvl):

        self.person = pygame.image.load(image).convert_alpha()
        self.x_box = 0
        self.y_box = 0
        self.x_pixel = 0
        self.y_pixel = 0
        self.lvl = lvl

    def move(self, direction):
        """method to move the character
		"""

		# moving to right
        if direction == 'droite':
            if self.x_box < (NOMBRE_SPRITE_FACE - 1):
                if self.lvl.structure[self.y_box][self.x_box+1] != 'm' and \
                    self.lvl.structure[self.y_box][self.x_box+1] != 'x':
                    self.x_box += 1
                    self.x_pixel = self.x_box * SIZE_SPRITE
		# moving to left
        if direction == 'gauche':
            if self.x_box > 0:
                if self.lvl.structure[self.y_box][self.x_box-1] != 'm' and \
                    self.lvl.structure[self.y_box][self.x_box-1] != 'x':
                    self.x_box -= 1
                    self.x_pixel = self.x_box * SIZE_SPRITE
		# moving to up
        if direction == 'haut':
            if self.y_box > 0:
                if self.lvl.structure[self.y_box-1][self.x_box] != 'm' and \
                    self.lvl.structure[self.y_box-1][self.x_box] != 'x':
                    self.y_box -= 1
                    self.y_pixel = self.y_box * SIZE_SPRITE
		# moving to down
        if direction == 'bas':
            if self.y_box < (NOMBRE_SPRITE_FACE - 1):
                if self.lvl.structure[self.y_box+1][self.x_box] != 'm' and \
                    self.lvl.structure[self.y_box+1][self.x_box] != 'x':
                    self.y_box += 1
                    self.y_pixel = self.y_box * SIZE_SPRITE
