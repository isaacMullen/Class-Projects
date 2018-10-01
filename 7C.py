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
    #pygame.draw.line(screen, WHITE,[800,100],[850,200],5)
    #pygame.draw.line(screen, WHITE,[800,100],[750,200],5)
    #pygame.draw.line(screen, WHITE,[850,200],[900,350],5)
    #pygame.draw.line(screen, WHITE,[750,200],[700,350],5)
    #pygame.draw.line(screen, WHITE,[700,350],[650,500],5)
    #pygame.draw.line(screen, WHITE,[900,350],[950,500],5)
    #pygame.draw.line(screen, WHITE,[650,500],[625,700],5)
    #pygame.draw.line(screen, WHITE,[950,500],[975,700],5)
    #pygame.draw.line(screen, WHITE,[800,200],[725,500],5)
    #pygame.draw.line(screen, WHITE,[800,200],[875,500],5)
    #pygame.draw.line(screen, WHITE,[800,200],[875,500],5)
    pygame.draw.polygon(screen, WHITE, [[550, 900], [575, 750],[625, 500],[700, 300],[800, 100],[900, 300],[975, 500],[1025, 750],[1050, 900]])
    pygame.draw.polygon(screen, BLACK, [[650, 900], [665, 750 ],[700, 550],[750, 400],[800, 250],[850, 400],[900, 550],[935, 750],[950, 900]])
    pygame.draw.line(screen, BLACK,[800,100],[800,255],4)








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
