import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

sponge = Actor('download')

sponge.pos = 150,150

diver = Actor('images')

diver.pos = 200,100

#background = Actor('ocean')

def draw():
    screen.blit("ocean",(0,0))
    sponge.draw()
    diver.draw()
    
pgzrun.go()