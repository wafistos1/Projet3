#!/usr/bin/python3
# conding: utf8

""" 
Jeu : Aidez MacGyver à s'échapper !
Jeu dans lequel on doit deplac........

"""
#
# import some files and modules 
import pygame 
import pygame.locals
import random
from  classes import *
from  constates import *


pygame.init()


fenetre = pygame.display.set_mode(fenetre_resolution)
icone = pygame.image.load(fenetre_icon).convert()
pygame.display.set_icon(icone)

niv = Niveau("niveau.txt")
niv.generer()
niv.afficher(fenetre)

fond = pygame.image.load(structures).convert()

"""image_macGyver = pygame.image.load(perso_MacGyver).convert()
image_gardien = pygame.image.load(Gardien).convert()

fenetre.blit(fond, (0, 0))
fenetre.blit(image_macGyver, (5, 5))
fenetre.blit(image_gardien, (460, 80))"""

pygame.display.set_caption(fenetre_titre)



pygame.display.flip()
game_over = False 

while not game_over:
    pygame.time.Clock().tick(30)# Framerate 30
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    



