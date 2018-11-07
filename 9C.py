#import other files 
import pygame, sys
from pygame.locals import *
import pygame, sys, math

pygame.init()
#load images and set up clock
ratImg = pygame.image.load('rat(1).png')
THOMASImg = pygame.image.load('THOMAS(1).png')
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption('Animation')
# create colours
WHITE = (255, 255, 255)
#set up starting loTHOMASion of the THOMAS
THOMASx = 10
THOMASy = 10
ratx = 15
raty = 15
while True: # the ma-in game loop
    if math.hypot((THOMASx-ratx),(THOMASy-raty)) <100 :
        print('REEEEEE YOU DIED')
        THOMASx=0    # do something when the objects collide
        THOMASy=0

    screen.fill(WHITE)
    screen.blit(THOMASImg, (THOMASx, THOMASy))
    screen.blit(ratImg, (ratx, raty))
    if ratx > THOMASx:   # If the rat is to the right of the THOMAS
        ratx=ratx+2	# keep moving right to get away
    else:
        ratx=ratx-2     #otherwise move left to get away
    if raty > THOMASy:	# If the rat is below the THOMAS
           raty=raty+2   # move further down to get away
    else:
            raty=raty-2    #otherwise move up the get away

    if ratx>1920:  #off right side of screen
            ratx=random.randint(0, 1920)
##    if ratx<0:    #off left side of screen
##            ratx=1900
    if raty>1080:   #off bottom of screen
            raty=0
##    if raty<0:     #off top of screen
##            raty=900


          #--------------------------------------------------------------
    for event in pygame.event.get(): #check for user input
         if event.type == QUIT:  #quit if requested to do so
            pygame.quit()
            sys.exit()
         if event.type==KEYDOWN:  #react when a key is pressed
              if event.key==K_LEFT:  #move left
                   THOMASx=THOMASx-50
              elif event.key==K_RIGHT:   #move   right
                   THOMASx=THOMASx+50
              elif event.key==K_UP:   #move   up
                   THOMASy=THOMASy-50
              elif event.key==K_DOWN:   #move  down
                   THOMASy=THOMASy+50
    pygame.display.update()   #show image in new loTHOMASion
    fpsClock.tick(FPS)   #pause the program

