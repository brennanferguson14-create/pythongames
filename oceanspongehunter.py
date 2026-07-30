import pgzrun
from random import randint
import pygame

WIDTH = 600
HEIGHT = 500

score = 0
gameover = False

diver = Actor("images")
diver.pos = 300,300
diver._surf = pygame.transform.scale(diver._surf, (60,60))

sponge = Actor("download")
sponge.pos = 300,300
sponge._surf = pygame.transform.scale(sponge._surf, (60,60))


def draw():
    screen.blit("ocean",(0,0))
    sponge.draw()
    diver.draw()
    screen.draw.text("score: "+str(score),color="black",topleft=(10,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("time is up your final score is: "+str(score),color="black",topleft=(10,10))

def placesponge():
    sponge.x=randint(50,(WIDTH-50))
    sponge.y=randint(50,(HEIGHT-50))

def timeup():
    global gameover
    gameover=True
    

def update():
    global score

    if keyboard.a:
        diver.x = diver.x - 2
    if keyboard.d:
        diver.x = diver.x + 2
    if keyboard.w:
        diver.y = diver.y - 2
    if keyboard.s:
        diver.y = diver.y + 2

    spongecollected = diver.colliderect(sponge)

    if spongecollected:
        print("word")
        score = score + 10
        placesponge()
    clock.schedule(timeup,30.0)





pgzrun.go()