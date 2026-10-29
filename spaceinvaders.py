import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2-5,10,HEIGHT)

BULLETHITSOUND = pygame.mixer.Sound('assets/Grenade+1.mp3')
BULLETFIRESOUND = pygame.mixer.Sound('assets/Gun+Silencer.mp3')

HEALTHFONT = pygame.font.SysFont('Arial',40)
WINNERFONT = pygame.font.SysFont('Arial',80)

FPS = 90
VEL = 15
BULLETVEL = 30
MAXBULLETS = 20
SWIDTH = 35
SHEIGHT = 20

YELLOWHIT = pygame.USEREVENT + 1
REDHIT = pygame.USEREVENT + 1

YELLOWSPACESHIP = pygame.image.load('yellowspaceship')
REDSPACESHIP