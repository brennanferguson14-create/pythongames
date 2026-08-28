import pgzrun
from random import randint

WIDTH = 450
HEIGHT = 350

snook = Actor("snook")
snook.pos = 400,120

rod = Actor("fishingrod")
rod.pos = 200,325

redfish = Actor("redfish")
redfish.pos = 150,120

mackerel = Actor("mackerel")
mackerel.pos = 40,140

score = 0

gameover = False

def draw():
    screen.blit("everglades",(0,0))
    snook.draw()
    redfish.draw()
    mackerel.draw()
    rod.draw()
    screen.draw.text("score: "+str(score),color="black",topleft=(5,5))
    if gameover:
        screen.fill("olivedrab")
        screen.draw.text("Game Over score: "+str(score),color="black",topleft=(5,5))

def placeredfish():
    redfish.x=randint(50,(WIDTH-50))
    redfish.y=randint(50,(HEIGHT-50))

def placesnook():
    snook.x=randint(50,(WIDTH-50))
    snook.x=randint(50,(HEIGHT-50))

def placemackerel():
    mackerel.x=randint(50,(WIDTH-50))
    mackerel.y=randint(50,(HEIGHT-50))

def timeup():
    global gameover
    gameover = True

def update():
    global score
    if keyboard.a:
        rod.x = rod.x - 2
    if keyboard.d:
        rod.x = rod.x + 2
    if keyboard.s:
        rod.y = rod.y + 2
    if keyboard.w:
        rod.y = rod.y - 2

    snookcollected = rod.colliderect(snook)
    redfishcollected = rod.colliderect(redfish)
    mackerelcollected = rod.colliderect(mackerel)

    if snookcollected:
        score = score + randint(1,35)
        placesnook()
    if redfishcollected:
        score = score + randint(1,35)
        placeredfish()
    if mackerelcollected:
        score = score + randint(5,40)
        placemackerel()

clock.schedule(timeup,30.0)

    

pgzrun.go()