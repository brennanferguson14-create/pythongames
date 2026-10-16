import pygame
from pygame.locals import *
from time import *

pygame.init()
screen = pygame.display.set_mode((750,750))
rocketx = 375
rockety = 375
rocket = pygame.image.load("images/rocket.png")
sky = pygame.image.load("images/spacebg.jpg")

keys = [False,False,False,False]

while rockety<750:
    screen.blit(rocket,(rocketx,rockety))
    screen.blit(sky,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0]=True
            elif event.key == K_LEFT:
                keys[1]=True
            elif event.key == K_DOWN:
                keys[2]=True
            elif event.key == K_RIGHT:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False
            elif event.key == K_LEFT:
                keys[1]=False
            elif event.key == K_DOWN:
                keys[2]=False
            elif event.key == K_RIGHT:
                keys[3]=False

        if keys[0]==True:
            if rockety>0:
                rockety = rockety - 5

        if keys[1]==True:
            if rocketx>0:
                rocketx = rocketx - 5

        if keys[2]==True:
            if rockety<750:
                rockety = rockety + 5

        if keys[3]==True:
            if rockety<750:
                rocketx = rocketx + 5

    

        
