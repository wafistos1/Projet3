""" module responsible for creating the labyrinth level
"""

#!/usr/bin/python3
# coding: utf-8

import pygame
from constantes import *


class Level:
    """ Class to create a level of our labyrinth
    """
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.position_elem = []

    def generate(self):
        """ Method to generate the level
        """
        # Open file of level
        with open(self.file, "r") as file:
            # Run line by line
            for line in file:
                new_line = []
                for sprite in line:
                    if sprite != '\n':
                        new_line.append(sprite)
                self.structure.append(new_line)


    def display(self, window):
        """ Method for displaying the level
        """
        # Loading images of sprites
        wall = pygame.image.load(STRUCT_WALL).convert_alpha()
        start = pygame.image.load(PRISON).convert_alpha()
        arrival = pygame.image.load(EXIT_DOOR).convert_alpha()
        my_decorations4 = pygame.image.load(DOCRATION).convert()

        # Browse the level file and implement the sprites
        line_num = 0
        for line in self.structure:
            box_num = 0
            for sprite in line:
                # Calculate the actual position
                x = box_num * SIZE_SPRITE
                y = line_num * SIZE_SPRITE
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'x':
                    window.blit(my_decorations4, (x, y))
                elif sprite == 'd':
                    window.blit(start, (x, y))
                elif sprite == 'a':
                    window.blit(arrival, (x, y))
                elif sprite == 'p':
                    self.position_elem.append((x, y))
                box_num += 1
            line_num += 1

##

# Fonctions

def posting(window, image, time=2000, pos=(65, 90)):
    """
    Function that display images as arguments
    """
    window.blit(image, pos)
    pygame.display.flip()
    pygame.time.delay(time)


def animation(window, text, my_font, text_color=(0, 7, 255),\
    backgroud_color=(255, 255, 255)):
    """ Fonctiond display animated text
    """
    letter = ""
    for letter1 in text:
        pygame.time.Clock().tick(8)
        letter += letter1
        my_surface_font = my_font.render(letter, False, text_color, backgroud_color)
        window.blit(my_surface_font, (30, 100))
        pygame.display.flip()
    pygame.time.delay(1000)
