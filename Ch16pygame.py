import pygame, sys, random
from pygameRunning import running
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

for i in range (100):
    width = random.randint(0,250)
    height = random.randint(0,250)
    top = random.randint(0,400)
    left = random.randint(0,500)

    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    
    pygame.draw.rect(screen, color,[left,top,width,height],random.randint(1,3))



    

pygame.display.flip()

running()
