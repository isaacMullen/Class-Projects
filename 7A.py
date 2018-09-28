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

pygame.draw.rect(screen, WHITE, [10, 10, 100, 100])

pygame.draw.rect(screen, WHITE, [200, 10, 300, 100])

pygame.draw.polygon(screen, WHITE, [[600, 10], [600, 200],[800, 100]],)

pygame.draw.circle(screen, WHITE,(1000,100),100)  

pygame.draw.polygon(screen, WHITE, [[100, 200], [10, 400],[100, 600],[200, 400]])

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
