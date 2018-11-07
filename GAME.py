#import other files 
import pygame, sys
from pygame.locals import *
import random
pygame.init()
#load images and set up clock
PLAYER = pygame.image.load('PLAYER.png')
PLAYER = pygame.transform.scale(PLAYER,(150, 150))
DEFENDER = pygame.image.load('DEFENDER.png')
DEFENDER = pygame.transform.scale(DEFENDER,(150, 150))

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption('Animation')
# create colours
WHITE = (255, 255, 255)
#set up starting loration of the rat
PLAYERx = 10
PLAYERy = 10
DEFENDERx = 15
DEFENDERy = 15
while True: # the main game loop
    
    screen.fill(WHITE)
    screen.blit(DEFENDER, (DEFENDERx, DEFENDERy))
    screen.blit(PLAYER, (PLAYERx, PLAYERy))
    if PLAYERx > DEFENDERx:   # If the THOMAS is to the right of the rat
        DEFENDERx=DEFENDERx+2	# chase THOMAS to the right
    elif PLAYERx < DEFENDERx:
        DEFENDERx=DEFENDERx-2     #otherwise move left to get away
    if PLAYERy > DEFENDERy:	# If the THOMAS is below the rat
           DEFENDERy=DEFENDERy+2   # move further down to get away
    elif PLAYERy < DEFENDERy:
            DEFENDERy=DEFENDERy-2    #otherwise move up the get away

    if PLAYERx>1920:  #off right side of screen
            PLAYERx=100
    if PLAYERx<0:    #off left side of screen
            PLAYERx=1900
    if PLAYERy>1080:   #off bottom of screen
            PLAYERy=100
    if PLAYERy<0:     #off top of screen
            PLAYERy=900


          #--------------------------------------------------------------
    for event in pygame.event.get(): #check for user input
         if event.type == QUIT:  #quit if requested to do so
            pygame.quit()
            sys.exit()
         if event.type==KEYDOWN:  #react when a key is pressed
              if event.key==K_LEFT:  #move left
                   PLAYERx=PLAYERx-50
              elif event.key==K_RIGHT:   #move   right
                   PLAYERx=PLAYERx+50
              elif event.key==K_UP:   #move   up
                   PLAYERy=PLAYERy-50
              elif event.key==K_DOWN:   #move  down
                   PLAYERy=PLAYERy+50
    pygame.display.update()   #show image in new location
    fpsClock.tick(FPS)   #pause the program

