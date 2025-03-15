import pygame
from pygame.locals import *

pygame.init()
screen =pygame.display.set_mode((300, 300))
red=255


running=True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type==QUIT:
            running=False

        elif event.type ==KEYUP:
            if event.key== K_DOWN:
                if red >=20:
                    red-=20 
                else:
                    red=255

            elif event.key ==K_UP:
                if red<=235:
                    red+=20
                else:
                    red =0
                    



    screen.fill((red,0,0))
    pygame.display.flip()

pygame.quit()

