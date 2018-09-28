import pygame, sys
from pygame.locals import *
import random
pygame.init()
screen=pygame.display.set_mode((1600,900))

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
screen.fill(BLACK)



for i in range(10):
    pygame.draw.line(screen, WHITE,[800,100],[850,200],5)
    pygame.draw.line(screen, WHITE,[800,100],[750,200],5)
    pygame.draw.line(screen, WHITE,[850,200],[900,350],5)
    pygame.draw.line(screen, WHITE,[750,200],[700,350],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)
    pygame.draw.line(screen, WHITE,[100,550],[153,450],5)







pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()


    

    
















while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
