import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (155,25,150)
screen.fill(purple)
pygame.display.update()

class Rect():
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimensions)

greenRect = Rect(green, (50,20,100,100))
redRect = Rect(red, (150,200,180,180))
greenRect.draw()
pygame.display.update()