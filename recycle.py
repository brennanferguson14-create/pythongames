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

ITEMS = ["chips","bag","trashbag","bottle","battery"]

gameover = False
gamecomplete = False
currentlevel = 1
Items = []
animations = []

def display_message(title,subtitle):
    screen.draw.text(title,fontsize=50, center=CENTRE,color="white")
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
    if len(Items)==0:
        Items= makeitems(currentlevel)


def getoptiontocreate(level):
    itemstocreate=["bag"]
    for i in range(0,level):
        randomoption = random.choice(ITEMS)
        itemstocreate.append(randomoption)
    return itemstocreate

def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        item = Actor(i + "img")
        newitems.append(item)
    return newitems

def layoutitems(itemstolayout):
    numberofgaps = len(itemstolayout)
    gapsize = WIDTH/numberofgaps
    random.shuffle(itemstolayout)
    for index,item in enumerate (itemstolayout):
        newxpos = (index+1)*gapsize
        item.x = newxpos


def handlegameover():
    global gameover
    gameover = True

def onmousedown(pos):
    global items, currentlevel
    for i in Items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handlegamecomplete()
            else:
                handlegameover()

def handlegamecomplete():
    global currentlevel, Items, animations, gamecomplete
    stopanimations(animations)
    if currentlevel == FINAL_LEVEL:
        gamecomplete = True
    else:
        currentlevel += 1
        Items = []
        animations = []

def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration = START_SPEED - currentlevel
        i.anchor = {"center","bottom"}
        animation = animate(i, duration=duration, onfinished=handlegameover, y=HEIGHT)
        animations.append(animation)

def stopanimations(animationstostop):
        for animation in animationstostop:
            if animation.running:
                animation.stop

pgzrun.go()
