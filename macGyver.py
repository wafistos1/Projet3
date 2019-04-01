#!/usr/bin/python3
# -*- coding: UTf8 -*-

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
from itertools import zip_longest 

#Initialisation du jeu
pygame.init()

#Couleur
BLANC = (255, 255, 255)

#font
ubuntu_my_font = pygame.font.SysFont("ubuntu", 40)

#Diffirentes etapes de la creations du jeu
pygame.display.set_caption(fenetre_titre)
fenetre = pygame.display.set_mode(fenetre_resolution)
fond = pygame.image.load(fenetre_fond)
icone = pygame.image.load(fenetre_icon).convert()
pygame.display.set_icon(icone)

#Chargement des diffirentes images du jeu
sering = pygame.image.load(seringue).convert()
element_ether = pygame.image.load(ether).convert_alpha()
element_tube = pygame.image.load(tube_plastique).convert_alpha()
element_aiguille = pygame.image.load(aiguille).convert_alpha()
item_trouver = pygame.image.load(bravo).convert_alpha()
item_trouver.set_colorkey(BLANC)
libre = pygame.image.load(libre).convert()
non_libre = pygame.image.load(non_libre).convert()
ob_ether = pygame.image.load(ob_ether).convert()
ob_seringue = pygame.image.load(ob_seringue).convert()
ob_tube = pygame.image.load(ob_tube).convert()


#Creation du labyrinthe avec affichage
niv = Niveau("niveau.txt")
niv.generer()
niv.afficher(fenetre)

#Recuperation d'une liste pour les positions des items
i = iter(niv.position_elem)
liste_postion = list(zip_longest(i, i))
position_ether,  position_tube, position_aiguille = random.sample(liste_postion, 3)

#Declarations des items
ether_trouver = False
tube_trouver = False
aiguille_trouver = False
item_3 = False
meet_gardien_macGver = False


#Creation du personnage McGyver
mac = Perso(perso_MacGyver, niv)

#Blit les items sur le labyrinthe
fenetre.blit(element_ether, tuple(position_ether))
fenetre.blit(element_tube, tuple(position_tube))
fenetre.blit(element_aiguille, tuple(position_aiguille))

#Deplacement en laisant la touche enfoncee 
pygame.key.set_repeat(400, 30)

pygame.display.flip()
game_over = False 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Boucle principale 
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while not game_over:
    pygame.time.Clock().tick(30)# Framerate 30
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        #Control du personnage
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_RIGHT:
                mac.deplacer('droite')
            elif event.key == pygame.K_LEFT:
                mac.deplacer('gauche')
            elif event.key == pygame.K_UP:
                mac.deplacer('haut')
            elif event.key == pygame.K_DOWN:
                mac.deplacer('bas')
            
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=   
    #Affichage (raffrichissement)
    fenetre.blit(fond, (0, 0))
    niv.afficher(fenetre)
    
    #Logique de l'affichage des items
    if position_ether != (mac.x, mac.y) and ether_trouver == False:
        fenetre.blit(element_ether, tuple(position_ether))
    else:
        if ether_trouver == False:
            affichage(fenetre, ob_ether) 
            ether_trouver = True

    if position_tube != (mac.x, mac.y) and tube_trouver == False:
        fenetre.blit(element_tube, tuple(position_tube))    
    else:
        if tube_trouver == False:
            affichage(fenetre, ob_tube) 
            tube_trouver = True

    if position_aiguille != (mac.x, mac.y) and aiguille_trouver == False:
        fenetre.blit(element_aiguille, tuple(position_aiguille))
    else:
        if aiguille_trouver == False:
            
            animation(fenetre, "Seringue touvee", ubuntu_my_font, )
            aiguille_trouver = True
    # Verifications si tous les items on ete trouve 
    if tube_trouver == True and ether_trouver == True and aiguille_trouver == True and item_3 == False:
       affichage(fenetre, item_trouver)
       item_3 = True 
    
    #Rencontre avec le Gardien
    if mac.x == 360 and mac.y == 420 and meet_gardien_macGver == False:
        meet_gardien_macGver = True
        if item_3 == True:
            #fenetre.blit(discution)
            affichage(fenetre, libre)
            
            
        else:
            #fenetre de vous avez perdu
            affichage(fenetre, non_libre)
            


    if niv.structure[mac.case_y][mac.case_x] == 'a':
        game_over = True 
    fenetre.blit(mac.gauche, (mac.x, mac.y))
    #Condition de collision
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    pygame.display.flip()