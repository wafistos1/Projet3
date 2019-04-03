#!/usr/bin/python3
# -*- coding: UTf8 -*-


import pygame
from pygame.locals import * 
from constates import *
import random 
"""
class that creates the characters of the game 
"""
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, image, niveau):
		#Sprites du personnage
		#supprime 
		self.personnage = pygame.image.load(image).convert_alpha()
		
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		#supprime 
		self.direction = self.personnage
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la personnage
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (NOMBRE_SPRITE_FACE - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and self.niveau.structure[self.case_y][self.case_x+1] != 'x':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * TAILLE_SPRITE
			self.direction = self.personnage
			#Image dans la bonne direction
			
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and self.niveau.structure[self.case_y][self.case_x-1] != 'x':
					self.case_x -= 1
					self.x = self.case_x * TAILLE_SPRITE
			self.direction = self.personnage
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and self.niveau.structure[self.case_y-1][self.case_x] != 'x':
					self.case_y -= 1
					self.y = self.case_y * TAILLE_SPRITE
			self.direction = self.personnage
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (NOMBRE_SPRITE_FACE - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 'x':
					self.case_y += 1
					self.y = self.case_y * TAILLE_SPRITE
			self.direction = self.personnage