import pygame, sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1100,500))

ratImg = pygame.image.load('rat.jpg')

FPS = 30 
fpsClock = pygame.time.Clock()



RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
YELLOW=(255, 255,   0)


x = 10
y = 100
direction = 'right'



while True: #6the main game loop
     screen.fill(WHITE)      # erase
     pygame.draw.circle(screen,BLACK,(x,y),100)    #draw
     if direction == 'right':
        x = x+10   #move to the right
        if (x >= 500):
            direction = 'down'
     if direction == 'down':
                y+=5
            
     for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
     pygame.display.update()
     fpsClock.tick(FPS)   #pause
