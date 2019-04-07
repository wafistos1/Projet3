#!/usr/bin/python3
# -*- coding: UTf8 -*-
import pygame
from pygame.locals import *
from constates import *


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
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:

			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				self.structure.append(ligne_niveau)
			#On sauvegarde cette structure


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
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x, y))
					fenetre.blit(gardien, (x-TAILLE_SPRITE, y))
				elif sprite == 'p':		   #p = position for items
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
