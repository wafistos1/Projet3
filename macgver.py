#!/usr/bin/python3
# coding: utf-8

"""
Game: Aidez MacGyver à s'échapper !

"""

# import files and modules
import random
import pygame
import pygame.locals
import lvl
import constantes as cons
import person as pr


# Initialisation Game
pygame.init()

# Color
BLANC = (255, 230, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
MY_FONT = pygame.font.SysFont("arial", 50, True)
MY_FONT_SCORE = pygame.font.SysFont("arial", 20, True)

# Load images of game
pygame.display.set_caption(cons.WINDOW_TITLE)
WINDOW = pygame.display.set_mode(cons.WINDOW_RESOLUTION)
WINDOW_BACKGROUND = pygame.image.load(cons.GAME_MENU)
BLACK_BACKGROUND = pygame.image.load(cons.BLACK_BACKGROUND)
ICON = pygame.image.load(cons.WINDOW_ICON).convert()
pygame.display.set_icon(ICON)

# Load images of object
ELEMENT_ETHER = pygame.image.load(cons.ETHER).convert_alpha()
ELEMENT_TUBE = pygame.image.load(cons.TUBE).convert_alpha()
ELEMENT_AIGUILLE = pygame.image.load(cons.AIGUILLE).convert_alpha()
ITEM_FOUND = pygame.image.load(cons.MANUFACTURED_SYRINGE).convert_alpha()
WINNER = pygame.image.load(cons.WIN_GAME).convert()
LOOSER = pygame.image.load(cons.GAME_OVER).convert()


# Code for moving the character while holding down the key
pygame.key.set_repeat(400, 30)

# Retrieving a list for object positions
level = lvl.Level("niveau.txt")
level.generate()

# Condition for Loop of menu and game
menu = True
game_over = False
continu_game = True


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
MAIN LOOP
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
    moving = False

    # Create level
    level.display(WINDOW)

    # Create a character
    mac = pr.Perso(cons.PERSO_MACGYVER, level)
    pygame.display.flip()

    # Blit objects in labyrinthe
    position_ether, position_tube, position_aiguille = \
        random.sample(level.position_elem, 3)

    WINDOW.blit(ELEMENT_ETHER, tuple(position_ether))
    WINDOW.blit(ELEMENT_TUBE, tuple(position_tube))
    WINDOW.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))
    print(level.position_elem)
    guardian = pygame.image.load(cons.PRISON_GUARD).convert_alpha()
    WINDOW.blit(guardian, (360, 420))

    # Init a bool for new game
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

    # Loop of game
    while not game_over:
        pygame.time.Clock().tick(10)  # Framerate 30
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                continu_game = False
                game_over = True

            # character control
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_RIGHT:
                    mac.move('droite')
                    moving = True
                elif event.key == pygame.K_LEFT:
                    mac.move('gauche')
                    moving = True
                elif event.key == pygame.K_UP:
                    mac.move('haut')
                    moving = True
                elif event.key == pygame.K_DOWN:
                    mac.move('bas')
                    moving = True

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        WINDOW.blit(BLACK_BACKGROUND, (0, 0))
        remaining_obj = MY_FONT_SCORE.render(
            f" Objets restant: {len(list_object)}", False, BLUE, BLANC)
        level.display(WINDOW)
        WINDOW.blit(remaining_obj, (100, 0))

        # Check ether object
        if (mac.x_pixel, mac.y_pixel) != position_ether and not ether_found:
            WINDOW.blit(ELEMENT_ETHER, tuple(position_ether))
        else:
            if not ether_found:
                lvl.animation(WINDOW, "Éther trouvé", MY_FONT, )
                list_object.remove("Ether")
                ether_found = True
                if list_object:
                    lvl.animation(
                        WINDOW, f" {len(list_object)} Objets restant", MY_FONT)
        # Check tube object
        if (mac.x_pixel, mac.y_pixel) != position_tube and not tube_found:
            WINDOW.blit(ELEMENT_TUBE, tuple(position_tube))
        else:
            if not tube_found:
                lvl.animation(WINDOW, "Tube trouvé", MY_FONT, )
                list_object.remove("Tube")
                tube_found = True
                if list_object:
                    lvl.animation(
                        WINDOW, f" {len(list_object)} Objets restant", MY_FONT)
        # Check aiguille object
        if (mac.x_pixel, mac.y_pixel) != position_aiguille \
                and not aiguille_found:
            WINDOW.blit(ELEMENT_AIGUILLE, tuple(position_aiguille))
        else:
            if not aiguille_found:
                lvl.animation(WINDOW, "Aiguille trouvé", MY_FONT, )
                list_object.remove("Aiguille")
                aiguille_found = True
                if list_object:
                    lvl.animation(
                        WINDOW, f" {len(list_object)} Objets restant", MY_FONT)

        # Check if all object is found
        if aiguille_found and tube_found and ether_found:
            if not item_3:
                lvl.posting(WINDOW, ITEM_FOUND)
                item_3 = True

        # Meet prison guard
        if mac.x_pixel == 360 and mac.y_pixel == 420 and\
                not meet_gardien_macGver:
            meet_gardien_macGver = True
            if item_3:
                lvl.posting(WINDOW, WINNER)

            else:
                lvl.posting(WINDOW, LOOSER)
                game_over = True
                level.position_elem = []

        # Game end
        if level.structure[mac.y_box][mac.x_box] == 'a':
            game_over = True
            level.position_elem = []

        WINDOW.blit(mac.person, (mac.x_pixel, mac.y_pixel))
        if not meet_gardien_macGver:
            WINDOW.blit(guardian, (360, 420))
    #  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.display.flip()
