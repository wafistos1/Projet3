#!/usr/bin/python3
#coding: utf-8

import pygame
from pygame.locals import *
from constantes import *


"""
Classes level for Labyrinthe
"""



class Niveau:
	"""Class to create a level
	"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = []
		self.position_elem = []


	def generer(self):
		"""Method to generate the level.
		"""
		#Open files of level
		with open(self.fichier, "r") as fichier:

			#Run line by line
			for ligne in fichier:
				
				#Stocke a single line of our level file 
				ligne_niveau = []
				#Run letters
				for sprite in ligne:
					#has made a line break and we ignore the \n
					if sprite != '\n':
						#Add sprite to the list
						ligne_niveau.append(sprite)
				#Add the stock line to our list 
				self.structure.append(ligne_niveau)
			#Backup our structure


	def afficher(self, fenetre):
		"""Method for displaying the level
		"""

		#Loading images
		mur = pygame.image.load(STRUCT_WALL).convert_alpha()
		depart = pygame.image.load(PRISON).convert_alpha()
		arrivee = pygame.image.load(EXIT_DOOR).convert_alpha()
		gardien = pygame.image.load(PRISON_GUARD).convert_alpha()
		my_decorations4 = pygame.image.load(DOCRATION).convert()

		#We go through the list of the level
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				# calculate the actual position in pixels
				x = num_case * TAILLE_SPRITE
				y = num_ligne * TAILLE_SPRITE
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x, y))
				elif sprite == 'x':
					fenetre.blit(my_decorations4, (x, y))
				elif sprite == 'd':		   #d = Start
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':		   #a = Arrival
					fenetre.blit(arrivee, (x, y))
					fenetre.blit(gardien, (x-TAILLE_SPRITE, y))
				elif sprite == 'p':		   #p = position for our objects
					self.position_elem.append((x, y))

				num_case += 1
			num_ligne += 1

#===================================================================================================
#Fonctions
#===================================================================================================

def affichage(fenetre, image, tmp=4000, position=(70, 70)):
	"""
	Function that displays images as arguments
	"""
	fenetre.blit(image, position)
	pygame.display.flip()
	pygame.time.delay(tmp)


def animation(fenetre, texte, my_font, text_color=(0, 7, 255),
		 backgroud_color=(255, 255, 255)):
	"""Fonction animated text
	"""
	lettre = ""
	for lettre1 in texte:
		pygame.time.Clock().tick(8)
		lettre += lettre1
		my_surface_font = my_font.render(lettre, False, text_color, backgroud_color)
		fenetre.blit(my_surface_font, (100, 100))
		pygame.display.flip()

	pygame.time.delay(1000)
