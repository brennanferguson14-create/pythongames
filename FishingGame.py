import pgzrun
import random

WIDTH = 650
HEIGHT = 400

snook = Actor("snook")
snook.pos = 400,120

rod = Actor("fishingrod")
rod.pos = 200,325

redfish = Actor("redfish")
redfish.pos = 150,120

mackerel = Actor("mackerel")
mackerel.pos = 40,235

score = 0

gameover = False

def draw():
    screen.blit("everglades",(0,0))
    snook.draw()
    redfish.draw()
    mackerel.draw()
    screen.draw.text("score: "+str(score),color="black",topleft=(10,10))
    if gameover:
        screen.draw.text("Game Over score: "+str(score),color="black",center=(0,0))

def placeredfish():
    redfish.x=randint(50,(WIDTH-50))
    redfish.y=randint(50,(HEIGHT-50))

def placesnook():
    snook.x=randint(50,(WIDTH-50))
    snook.x=randint(50,(WIDTH-50))

def placemackerel():
    mackerel.x=randint(50,(WIDTH-50))
    mackerel.y=randint(50,(WIDTH-50))

def timeup():
    global gameover
    gameover = True

def update():
    if keyboard.a:
        rod.x = rod.x - 2
    if keyboard.d:
        rod.x = rod.x + 2
    if keyboard.s:
        rod.y = rod.y - 2
    if keyboard.w:
        rod.y = rod.y + 2

    snookcollected = rod.colliderect(snook)
    redfishcollected = rod.colliderect(redfish)
    mackerelcollected = rod.colliderect(mackerel)

    if snookcollected:
        score = score + randint(1,35)
        placesnook()

    

pgzrun.go()