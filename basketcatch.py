import pygame
import random

WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode(WIDTH,HEIGHT)

ball = pygame.image.load('images/ball.jpg')
basket = pygame.image.load('images/basket.jpg')
park = pygame.image.load('images/park.jpg')

FPS = 120
VEL = 60
MAXBALLS = 15
BHEIGHT = 25
BWIDTH = 25
BAHEIGHT = 30
BAWIDTH = 30
score = 0
ball = pygame.transform.scale(ball,(25,25))
basket = pygame.transform.scale(basket,(30,30))
park = pygame.transform.scale(park,(800,500))
basketx = 30
baskeky = 30
balls = []

for i in range(MAXBALLS):
    x = random.randint(0,WIDTH)
    y = random.randint(25,500)

font = pygame.font.SysFont("Arial",50)

#the collecting system the positions add the font the score variable start the loop 
while True:
    screen.blit(park,(0,0))
    screen.blit(ball,(400,0))
    screen.blit(basket,(400,500))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()
            exit(0)
        if event.type == pygame.KEYDOWN and event.key == K_LEFT:
                basketx = basketx - 20
        if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                basketx = basketx + 20

    

