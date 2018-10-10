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
GREY = (48, 41, 50)
BLUE = (1, 7, 52)
LIGHTBLUE = (95, 164, 201)
LIGHTRED = (150, 1, 28)
BEIGE = (128, 102, 79)
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
    


#INSIDE OF HEAD
    pygame.draw.polygon(screen, BLACK, [[650, 900], [665, 750],[700, 550],[750, 400],[800, 250],[850, 400],[900, 550],[935, 750],[950, 900]])
#TEETH
    x=0
    y=0
    extra = 0
    for i in range (3):
        pygame.draw.line(screen, WHITE,[800+x,725+y],[800+x,825+y],3)
        x=x+25
        y=y-7
        
    for i in range(2):
                pygame.draw.line(screen, WHITE,[800+x,725+y],[800+x,807+y],3)
                x=x+25
                y=y-28

    x=0
    y=0
    for i in range (3):
        pygame.draw.line(screen, WHITE,[800-x,725+y],[800-x,825+y],3)
        x=x+25
        y=y-7
        
    for i in range(2):
                pygame.draw.line(screen, WHITE,[800-x,725+y],[800-x,807+y],3)
                x=x+25
                y=y-28        
            
        
    
          
        

          
        
        
            

#MOUTH
pygame.draw.arc(screen, BLACK, (682,525,238,300), 3, 6.4, 5)
pygame.draw.arc(screen, RED, (682,525,238,200), 3, 6.4, 5)
pygame.draw.arc(screen, BLACK, (682,525,238,250), 3, 6.4, 5)
pygame.draw.arc(screen, WHITE, (682,525,238,300), 3, 6.4, 5)
pygame.draw.arc(screen, WHITE, (682,525,238,200), 3, 6.4, 5)
pygame.draw.arc(screen, WHITE, (682,525,238,250), 3, 6.4, 5)
    

#EYES
pygame.draw.polygon(screen, LIGHTBLUE, [[700, 450], [785, 505],[790, 530],[770, 560],[750,560],[735, 555]])
pygame.draw.polygon(screen, BLACK, [[700, 450], [785, 505],[790, 530],[770, 560],[750,560],[735, 555]],3)
pygame.draw.polygon(screen, LIGHTBLUE, [[900, 450], [815, 505],[810, 530],[830, 560],[850, 560],[865, 555]])
pygame.draw.polygon(screen, BLACK, [[900, 450], [815, 505],[810, 530],[830, 560],[850, 560],[865, 555]],3)
#OUTSIDE OF HEAD
pygame.draw.polygon(screen, GREY, [[550, 900], [575, 750],[625, 500],[700, 300],[800, 100],[900, 300],[975, 500],[1025, 750],[1050, 900],[650, 900], [665, 750],[700, 550],[750, 400],[800, 250],[850, 400],[900, 550],[935, 750],[950, 900]])
                              

#OUTLINE
pygame.draw.line(screen, BLACK, [800,100],[800,255],3)
pygame.draw.polygon(screen,BLACK, [[550, 900], [575, 750],[625, 500],[700, 300],[800, 100],[900, 300],[975, 500],[1025, 750],[1050, 900]],5)
pygame.draw.polygon(screen, BLACK, [[650, 900], [665, 750 ],[700, 550],[750, 400],[800, 250],[850, 400],[900, 550],[935, 750],[950, 900]],5)
pygame.draw.polygon(screen, BLACK, [[650, 900], [665, 750 ],[700, 550],[750, 400],[800, 250],[850, 400],[900, 550],[935, 750],[950, 900]],5)
#SCYTHE(RIGHT)
pygame.draw.arc(screen, WHITE, (700,200,800,800), 5, 8, 7)
pygame.draw.arc(screen, WHITE, (760,200,650,725), 5, 8, 7)
    
#SCYTHE(LEFT)
pygame.draw.arc(screen, WHITE, (130,200,800,800), 1.5, 5, 7)
pygame.draw.arc(screen, WHITE, (220,200,650,725), 1.5, 5, 7)    


#x = [20, 1580]
#y = [20, 1580]
#random.randint
#x = 20
#y = 20
#pygame.draw.circle(screen, BEIGE,(x,y),300)
    







pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()


    

    

















