#!/usr/bin/python3
#coding:UTF-8

"""
Jeu : Aidez MacGyver à s'échapper !
Jeu dans lequel on doit deplac........

"""

# import files and modules
import pygame
import pygame.locals
import random
from  niveau import *
from  constates import *
from perso import *


#Initialisation Game
pygame.init()

#Color
BLANC = (255, 255, 255)

#font
MY_FONT = pygame.font.SysFont("ubuntu", 40)



#Diffirentes etapes de la creations du jeu
pygame.display.set_caption(FENETRE_TITRE)
FENETRE = pygame.display.set_mode(FENETRE_RESOLUTION)
WINDOW_BACKGROUND = pygame.image.load(GAME_MENU)
BLACK_BACKGROUND = pygame.image.load(BLACK_BACKGROUND)
ICON = pygame.image.load(FENETRE_ICON).convert()
pygame.display.set_icon(ICON)

#Load images of game
ELEMENT_ETHER = pygame.image.load(ETHER).convert_alpha()
ELEMENT_TUBE = pygame.image.load(TUBE).convert_alpha()
ELEMENT_AIGUILLE = pygame.image.load(AIGUILLE).convert_alpha()
ITEM_FOUND = pygame.image.load(MANUFACTURED_SYRINGE).convert_alpha()
WINNER = pygame.image.load(WIN_GAME).convert()
LOOSER = pygame.image.load(GAME_OVER).convert()


#Declarations of objects
ether_trouver = False
tube_trouver = False
aiguille_trouver = False
item_3 = False
meet_gardien_macGver = False



#code for moving the character while holding down the key
pygame.key.set_repeat(400, 30)

#Retrieving a list for object positions
niv = Niveau("niveau.txt")
niv.generer()



# Condition for menu and game
menu = True
game_over = False
continu_game = True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Boucle principale
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while  menu:

#Creation
    #Creation list of object
    list_object = ["Ether", "Tube", "Aiguille"]
    #Object_declarations 
    ether_trouver = False
    tube_trouver = False
    aiguille_trouver = False
    item_3 = False
    meet_gardien_macGver = False



    niv.afficher(FENETRE)
    mac = Perso(PERSO_MACGYVER, niv)
    pygame.display.flip()

    print(niv.position_elem)
    position_ether, position_tube, position_aiguille = random.sample(niv.position_elem, 3)
    print(position_aiguille, position_ether, position_tube)

    #Blit objects in labyrinthe
    FENETRE.blit(ELEMENT_ETHER, tuple(position_ether))
    FENETRE.blit(ELEMENT_TUBE, tuple(position_tube))
    FENETRE.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))

    pygame.display.flip()
    game_over = False#condition pour une nouvelle partie
    continu_game = True#conditon pour nouvelle partie



    while continu_game:
        pygame.time.Clock().tick(10)
        FENETRE.blit(WINDOW_BACKGROUND, (50, 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    continu_game = False
                    game_over = True
                    menu = False

                elif event.key == pygame.K_c:
                    continu_game = False


    #main loop of game
    while not game_over:
        pygame.time.Clock().tick(30)# Framerate 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                continu_game = False
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
        #character control
        FENETRE.blit(BLACK_BACKGROUND, (0, 0))
        niv.afficher(FENETRE)

        #Logic of the display of objects
        if position_ether != (mac.x, mac.y) and not ether_trouver:
            FENETRE.blit(ELEMENT_ETHER, tuple(position_ether))
        else:
            if not ether_trouver:
                animation(FENETRE, "Ether find", MY_FONT, )
                list_object.remove("Ether")
                if list_object:
                    animation(FENETRE, f"Il reste {len(list_object)} Objets !!", MY_FONT)
                ether_trouver = True

        if position_tube != (mac.x, mac.y) and not tube_trouver:
            FENETRE.blit(ELEMENT_TUBE, tuple(position_tube))
        else:
            if not tube_trouver:
                animation(FENETRE, "Tube find", MY_FONT, )
                list_object.remove("Tube")
                if list_object:
                    animation(FENETRE, f"Il reste {len(list_object)} Objets !!", MY_FONT)
                tube_trouver = True

        if position_aiguille != (mac.x, mac.y) and not aiguille_trouver:
            FENETRE.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))
        else:
            if not aiguille_trouver:

                animation(FENETRE, f"Aiguille find", MY_FONT, )
                list_object.remove("Aiguille")
                if list_object:
                    animation(FENETRE, f"Il reste {len(list_object)} Objets !!", MY_FONT)
                aiguille_trouver = True
        # Verifications si tous les items on ete trouve
        if tube_trouver and ether_trouver and aiguille_trouver  and not item_3:
            affichage(FENETRE, ITEM_FOUND)
            item_3 = True

        #Meet prison guard
        if mac.x == 360 and mac.y == 420 and not meet_gardien_macGver:
            meet_gardien_macGver = True
            if item_3:
                affichage(FENETRE, WINNER)

            else:
                affichage(FENETRE, LOOSER)


        if niv.structure[mac.case_y][mac.case_x] == 'a':
            game_over = True
            niv.position_elem = [] #Initialisation the list positions of Objects at 0
            #menu = False

        FENETRE.blit(mac.personnage, (mac.x, mac.y))
        #Condition of collision
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.display.flip()
