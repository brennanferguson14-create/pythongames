import pgzrun
from random import randint

TITLE= "good shot"
WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill(color=(34,12,200))
    alien.draw()
    screen.draw.text(message, center = (400,20), fontsize = 30 )

def placealien():
    alien.x=randint(50,450)
    alien.y=randint(50,450)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "goodshot"
        placealien()
    else:
        message = "you missed"


pgzrun.go()