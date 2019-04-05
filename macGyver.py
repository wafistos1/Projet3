#!/usr/bin/python3
# -*- coding: UTf8 -*-

""" 
Jeu : Aidez MacGyver à s'échapper !
Jeu dans lequel on doit deplac........

"""
#
# import files and modules 
import pygame 
import pygame.locals
import random
from  niveau import *
from  constates import *
from perso import *
from itertools import zip_longest 

#Initialisation Game
pygame.init()

#Color
BLANC = (255, 255, 255)

#font
ubuntu_my_font = pygame.font.SysFont("ubuntu", 40)



#Diffirentes etapes de la creations du jeu
pygame.display.set_caption(FENETRE_TITRE)
fenetre = pygame.display.set_mode(FENETRE_RESOLUTION)
fond = pygame.image.load(GAME_MENU)
fond_noir = pygame.image.load(BLACK_BACKGROUND)
icone = pygame.image.load(FENETRE_ICON).convert()
pygame.display.set_icon(icone)

#Load images of game
sering = pygame.image.load(SERINGUE).convert()
element_ether = pygame.image.load(ETHER).convert_alpha()
element_tube = pygame.image.load(TUBE).convert_alpha()
element_aiguille = pygame.image.load(AIGUILLE).convert_alpha()
item_trouver = pygame.image.load(MANUFACTURED_SYRINGE).convert_alpha()
item_trouver.set_colorkey(BLANC)
libre = pygame.image.load(WIN_GAME).convert()
non_libre = pygame.image.load(GAME_OVER).convert()
ob_ether = pygame.image.load(ETHER_FIND).convert()
ob_seringue = pygame.image.load(SYRINGE_FOUND).convert()
ob_tube = pygame.image.load(FIND_TUBE).convert()






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
    #Declarations des items
    ether_trouver = False
    tube_trouver = False
    aiguille_trouver = False
    item_3 = False
    meet_gardien_macGver = False



    niv.afficher(fenetre)
    mac = Perso(PERSO_MACGYVER, niv)
    pygame.display.flip()
    

    print(niv.position_elem)
    position_ether,  position_tube, position_aiguille = random.sample(niv.position_elem, 3)
    print(position_aiguille, position_ether, position_tube)

       

    #Blit objects in labyrinthe
    fenetre.blit(element_ether, tuple(position_ether))
    fenetre.blit(element_tube, tuple(position_tube))
    fenetre.blit(element_aiguille, tuple(position_aiguille))
    pygame.display.flip()
    game_over = False#condition pour une nouvelle partie
    continu_game = True#conditon pour nouvelle partie



    while continu_game:
        pygame.time.Clock().tick(10)
        fenetre.blit(fond, (50, 50))
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
        fenetre.blit(fond_noir, (0, 0))
        niv.afficher(fenetre)
        
        #Logic of the display of objects
        if position_ether != (mac.x, mac.y) and ether_trouver == False:
            fenetre.blit(element_ether, tuple(position_ether))
        else:
            if ether_trouver == False:
                animation(fenetre, "Ether find", ubuntu_my_font, )
                list_object.remove("Ether")
                if len(list_object) != 0:
                    animation(fenetre, f"Il reste {len(list_object)} Objets !!", ubuntu_my_font)
                ether_trouver = True

        if position_tube != (mac.x, mac.y) and tube_trouver == False:
            fenetre.blit(element_tube, tuple(position_tube))    
        else:
            if tube_trouver == False:
                animation(fenetre, "Tube find", ubuntu_my_font, )
                list_object.remove("Tube")
                if len(list_object) != 0:
                    animation(fenetre, f"Il reste {len(list_object)} Objets !!", ubuntu_my_font)
                tube_trouver = True

        if position_aiguille != (mac.x, mac.y) and aiguille_trouver == False:
            fenetre.blit(element_aiguille, tuple(position_aiguille))
        else:
            if aiguille_trouver == False:
                
                animation(fenetre, f"Aiguille find", ubuntu_my_font, )
                list_object.remove("Aiguille")
                if len(list_object) != 0:
                    animation(fenetre, f"Il reste {len(list_object)} Objets !!", ubuntu_my_font)
                aiguille_trouver = True
        # Verifications si tous les items on ete trouve 
        if tube_trouver == True and ether_trouver == True and aiguille_trouver == True and item_3 == False:
            affichage(fenetre, item_trouver)
            item_3 = True 
        
        #Rencontre avec le Gardien
        if mac.x == 360 and mac.y == 420 and meet_gardien_macGver == False:
            meet_gardien_macGver = True
            if item_3 == True:
                affichage(fenetre, libre)
                
                
            else:
                affichage(fenetre, non_libre)
                


        if niv.structure[mac.case_y][mac.case_x] == 'a':
            game_over = True
            niv.position_elem = [] #Initialisation the list positions of Objects at 0   
            #menu = False
            
        fenetre.blit(mac.personnage, (mac.x, mac.y))
        #Condition of collision
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.display.flip()
