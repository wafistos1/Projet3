#!/usr/bin/python3
# coding: utf-8


"""
Game: Aidez MacGyver à s'échapper !

"""

# import files and modules
import random
import pygame
import pygame.locals
from level import *
from constantes import *
from perso import *


# Initialisation Game
pygame.init()

# Color
BLANC = (255, 255, 255)

# Font
MY_FONT = pygame.font.SysFont("ubuntu", 50)

# Diffirentes etapes de la creations du jeu
pygame.display.set_caption(WINDOW_TITRE)
WINDOW = pygame.display.set_mode(WINDOW_RESOLUTION)
WINDOW_BACKGROUND = pygame.image.load(GAME_MENU)
BLACK_BACKGROUND = pygame.image.load(BLACK_BACKGROUND)
ICON = pygame.image.load(WINDOW_ICON).convert()
pygame.display.set_icon(ICON)

# Load images of game
ELEMENT_ETHER = pygame.image.load(ETHER).convert_alpha()
ELEMENT_TUBE = pygame.image.load(TUBE).convert_alpha()
ELEMENT_AIGUILLE = pygame.image.load(AIGUILLE).convert_alpha()
ITEM_trouvé = pygame.image.load(MANUFACTURED_SYRINGE).convert_alpha()
WINNER = pygame.image.load(WIN_GAME).convert()
LOOSER = pygame.image.load(GAME_OVER).convert()

# Declarations of objects
ether_found = False
tube_trouver = False
aiguille_trouver = False
item_3 = False
meet_gardien_macGver = False

# Code for moving the character while holding down the key
pygame.key.set_repeat(400, 30)

# Retrieving a list for object positions
level = Level("niveau.txt")
level.generer()

# Condition for menu and game
menu = True
game_over = False
continu_game = True


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Boucle principale
"""
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while menu:
    # Creation list of object
    list_object = ["Ether", "Tube", "Aiguille"]

    # Object_declarations
    ether_found = False
    tube_found = False
    aiguille_found = False
    item_3 = False
    meet_gardien_macGver = False

    # Create level
    level.display(WINDOW)

    # Create a character
    mac = Perso(PERSO_MACGYVER, level)
    pygame.display.flip()

    # Blit objects in labyrinthe
    position_ether, position_tube, position_aiguille = random.sample(level.position_elem, 3)
    WINDOW.blit(ELEMENT_ETHER, tuple(position_ether))
    WINDOW.blit(ELEMENT_TUBE, tuple(position_tube))
    WINDOW.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))
    guardian = pygame.image.load(PRISON_GUARD).convert_alpha()
    WINDOW.blit(guardian, (360, 420))
    pygame.display.flip()

    game_over = False
    continu_game = True

    while continu_game:
        pygame.time.Clock().tick(10)
        WINDOW.blit(WINDOW_BACKGROUND, (65, 90))
        

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    continu_game = False
                    game_over = True
                    menu = False

                elif event.key == pygame.K_c:
                    continu_game = False

    # Main loop of game
    while not game_over:
        pygame.time.Clock().tick(10)  # Framerate 30
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                continu_game = False
                game_over = True

            # Control du personnage
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_RIGHT:
                    mac.move('droite')
                elif event.key == pygame.K_LEFT:
                    mac.move('gauche')
                elif event.key == pygame.K_UP:
                    mac.move('haut')
                elif event.key == pygame.K_DOWN:
                    mac.move('bas')

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
        # Character control
        WINDOW.blit(BLACK_BACKGROUND, (0, 0))
        level.display(WINDOW)

        # Logic of the display of objects
        if position_ether != (mac.x, mac.y) and not ether_found:
            WINDOW.blit(ELEMENT_ETHER, tuple(position_ether))
        else:
            if not ether_found:
                animation(WINDOW, "Éther trouvé", MY_FONT, )
                list_object.remove("Ether")
                if list_object:
                    animation(WINDOW, f" {len(list_object)} Objets restant", MY_FONT)
                ether_found = True

        if position_tube != (mac.x, mac.y) and not tube_found:
            WINDOW.blit(ELEMENT_TUBE, tuple(position_tube))
        else:
            if not tube_found:
                animation(WINDOW, "Tube trouvé", MY_FONT, )
                list_object.remove("Tube")
                if list_object:
                    animation(WINDOW, f" {len(list_object)} Objets restant", MY_FONT)
                tube_found = True

        if position_aiguille != (mac.x, mac.y) and not aiguille_found:
            WINDOW.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))
        else:
            if not aiguille_found:

                animation(WINDOW, f"Aiguille trouvée", MY_FONT, )
                list_object.remove("Aiguille")
                if list_object:
                    animation(WINDOW, f" {len(list_object)} Objets restant", MY_FONT)
                aiguille_found = True

        # Verifications si tous les objets on ete trouves
        if tube_found and ether_found and aiguille_found and not item_3:
            posting(WINDOW, ITEM_trouvé)
            item_3 = True

        # Meet prison guard
        if mac.x == 360 and mac.y == 420 and not meet_gardien_macGver:
            meet_gardien_macGver = True
            if item_3:
                posting(WINDOW, WINNER)

            else:
                posting(WINDOW, LOOSER)
                game_over = True
                level.position_elem = []

        if level.structure[mac.case_y][mac.case_x] == 'a':
            game_over = True
            level.position_elem = []

        WINDOW.blit(mac.personnage, (mac.x, mac.y))
        if not meet_gardien_macGver:
            WINDOW.blit(guardian, (360, 420))
        
    #  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.display.flip()
