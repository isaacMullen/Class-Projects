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

pygame.draw.rect(screen, GREEN, [10, 400, 1600, 300])

pygame.draw.rect(screen, WHITE, [10, 400, 1600, 300],10)

pygame.draw.rect(screen, WHITE, [150, 150, 5, 300])

pygame.draw.circle(screen, WHITE,(150,100),50,5)

pygame.draw.line(screen, WHITE,[100,550],[153,450],5)

pygame.draw.line(screen, WHITE,[200,550],[153,450],5)

pygame.draw.line(screen, WHITE,[250,250],[150,300],5)

pygame.draw.line(screen, WHITE,[150,297],[50,250],5)

pygame.draw.circle(screen, WHITE,(125,80),15,5)

pygame.draw.circle(screen, WHITE,(175,80),15,5)

pygame.draw.rect(screen, RED, [130, 120, 40, 15])

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
