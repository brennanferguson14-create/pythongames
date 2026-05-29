import pgzrun
from random import randint

#screensize
WIDTH = 500
HEIGHT = 500

def draw():
    r = 255
    g = 0 
    b = randint(120,255)

    #size of rectangle
    width = WIDTH
    height = HEIGHT - 200
    

    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 250,250
        screen.draw.rect

pgzrun.go()