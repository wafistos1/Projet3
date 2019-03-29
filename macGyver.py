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

pygame.display.set_caption(fenetre_titre)
fenetre = pygame.display.set_mode(fenetre_resolution)
fond = pygame.image.load(fenetre_fond)
icone = pygame.image.load(fenetre_icon).convert()
pygame.display.set_icon(icone)

sering = pygame.image.load(seringue).convert()


niv = Niveau("niveau.txt")
niv.generer()
niv.afficher(fenetre)


mac = Perso(perso_MacGyver, perso_MacGyver, perso_MacGyver, perso_MacGyver, niv)




fenetre.blit(sering, (330, 0))
pygame.display.flip()
game_over = False 

while not game_over:
    pygame.time.Clock().tick(30)# Framerate 30
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_RIGHT:
                mac.deplacer('droite')
                print("droite")
            elif event.key == pygame.K_LEFT:
                mac.deplacer('gauche')
            elif event.key == pygame.K_UP:
                mac.deplacer('haut')
            elif event.key == pygame.K_DOWN:
                mac.deplacer('bas')
    fenetre.blit(fond, (0, 0))
    niv.afficher(fenetre)
    fenetre.blit(mac.gauche, (mac.x, mac.y))
    pygame.display.flip()