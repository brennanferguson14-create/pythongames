import pgzrun
import random

FONT_option = (255, 255, 255)

WIDTH = 800
HEIGHT = 600

CENTRE_X = WIDTH/2
CENTRE_Y = HEIGHT/2

CENTRE = (CENTRE_X,CENTRE_Y)

FINAL_LEVEL = 5

START_SPEED = 5

ITEMS = ["chipsimg","bagimg","trashbagimg","bottleimg"]

gameover = False
gamecomplete = False
currentlevel = 1
Items = []
animations = []

def display_message(title,subtitle):
    screen.draw.text(title,fontsize=50, center=CENTRE.color="white")
    screen.draw.text(subtitle,fontsize=30, center = (CENTER.X,CENTRE.Y+30),color="white")

def draw():
    global gameover, gamecomplete, currentlevel, Items
    screen.clear()
    screen.blit("greenbgimg", (0,0))
    if gameover:
        display_message("game over","try again")
    elif gamecomplete:
        display_message("you win","play again")
    else:
        for item in Items:
          item.draw()

def makeitems(level):
    itemstocreate = getoptiontocreate(level)#choose what to create
    newitems = createitems(itemstocreate)#create the actors from the items
    layoutitems(newitems)#position the items  
    animateitems(newitems)#animate the items to make the items move
    return newitems 


def update():
    global Items
    if len(Items)==0
    Items= makeitems(currentlevel)


pgzrun.go()
