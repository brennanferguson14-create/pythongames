import pygame
import time

pygame.init()

display_surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("Bday card")

bgimg = pygame.image.load("images/bdaybg.jpg")
bgimg = pygame.transform.scale(bgimg,(500,500))

while True:
    font = pygame.font.SysFont("Roboto Mono",70)
    msg1 = font.render("Happy",True,(0,0,0))
    msg2 = font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(bgimg,(0,0))
    display_surface.blit(msg1,(175,225))
    display_surface.blit(msg2,(175,275))
    pygame.display.update()
    time.sleep(3)

    bgimg2 = pygame.image.load("images/cake.jpg")
    display_surface.fill((255,255,255))
    display_surface.blit(bgimg2,(0,0))
    pygame.display.update()
    time.sleep(5)

    bgimg3 = pygame.image.load("images/present.jpg")
    display_surface.fill((0,0,0))
    display_surface.blit(bgimg3,(0,0))
    pygame.display.update()
    time.sleep(5)