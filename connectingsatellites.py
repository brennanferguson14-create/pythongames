import pgzrun
from random import randint
from time import time
import pygame

WIDTH = 600
HEIGHT = 400

satellites = []
lines = []
next_satellite = 0

totalsatellites = 10

starttime = 0
endtime = 0
totaltime = 0

def create():
    global starttime
    for count in range(0,totalsatellites):
        satellite = Actor('satellite')
        satellite.pos = randint(50,550), randint(50,350)
        #satellite._surf = pygame.transform.scale(satellite._surf, (60,60))
        satellites.append(satellite)
        starttime = time()

def draw():
    global totaltime

    screen.blit('space',(0,0))
    number = 1
    for s in satellites:
        screen.draw.text(str(number),(s.pos[0],s.pos[1]+25))
        s.draw()
        number = number + 1
    
    for l in lines:
        screen.draw.line(l[0],l[1],(191,0,255))

    if next_satellite < totalsatellites:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    
def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines

    print("Mouse clicked",pos)

    if next_satellite < totalsatellites:
        if satellites[next_satellite].collidepoint(pos):
            print("Correct")
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite=next_satellite+1
        else:
            print("Wrong")
            lines=[]
            next_satellite=0

    

create()
pgzrun.go()
