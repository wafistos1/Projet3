#!/usr/bin/python3
# -*- coding: UTf8 -*-

"""
Classes

"""
"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constates import *
import random 

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = []
		self.position_elem = []
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
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
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		
		
		
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(structures_mur).convert_alpha()
		depart = pygame.image.load(start).convert_alpha()
		arrivee = pygame.image.load(arrival).convert_alpha()
		gardien = pygame.image.load(Gardien).convert_alpha()
		my_decorations4 = pygame.image.load(decorations4).convert()
		
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x, y))
				elif sprite == 'x':
					fenetre.blit(my_decorations4, (x, y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x, y))
					fenetre.blit(gardien, (x-taille_sprite, y))
				elif sprite == 'p':		   #p = position pour items 
					self.position_elem.append((x, y))
					
				num_case += 1
			num_ligne += 1
		
		
    
   
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
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and self.niveau.structure[self.case_y][self.case_x+1] != 'x':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			self.direction = self.personnage
			#Image dans la bonne direction
			
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and self.niveau.structure[self.case_y][self.case_x-1] != 'x':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.personnage
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and self.niveau.structure[self.case_y-1][self.case_x] != 'x':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.personnage
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 'x':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.personnage

	
	
def affichage(fenetre, image, tmp=2000, position=(70, 70)):
	"""
	Fonction qui affiche en premier plan des images passer en argument
	"""
	fenetre.blit(image, position)
	pygame.display.flip()
	pygame.time.delay(tmp)


def animation(fenetre, texte, my_font, text_color=(0, 7, 255), backgroud_color=(255, 255, 255)):
	"""Fonction animated text
	"""
	lettre = ""
	for lettre1 in texte:
		pygame.time.Clock().tick(8)
		
		lettre += lettre1
		my_surface_font = my_font.render(lettre, False, text_color, backgroud_color)
		fenetre.blit(my_surface_font, (100, 100))
		pygame.display.flip()
		#ajouter une surface pour netoyer l'ecran ....
	pygame.time.delay(1000)
		
