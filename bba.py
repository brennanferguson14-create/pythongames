import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
gameover = False

bee = Actor("bee")
bee.pos = 300,300

flower = Actor("flower")
flower.pos = 300,300

def draw():
    screen.blit("bg",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("score: "+str(score),color="black",topleft=(10,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("time is up your final score is: "+str(score),color="black",topleft=(10,10))

def placeflower():
    flower.x=randint(50,(WIDTH-50))
    flower.y=randint(50,(HEIGHT-50))

def timeup():
    global gameover
    gameover=True
    

def update():
    global score

    if keyboard.a:
        bee.x = bee.x - 2
    if keyboard.d:
        bee.x = bee.x + 2
    if keyboard.w:
        bee.y = bee.y - 2
    if keyboard.s:
        bee.y = bee.y + 2

    flowercollected = bee.colliderect(flower)

    if flowercollected:
        print("word")
        score = score + 10
        placeflower()
    clock.schedule(timeup,30.0)





pgzrun.go()