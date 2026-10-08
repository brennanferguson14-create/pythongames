import pygame
pygame.init()
screen = pygame.display.set_mode((600,500))
screen.fill((0,0,0))
purple = ((155,15,155))
pygame.display.update()

class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
        self.Draw_Circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)

    def grow(self,r):
        self.circle_radius = self.circle_radius + r
        self.Draw_Circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)


mycircle = Circle(purple,(300,250),10,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            mycircle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0,0,0))
            mycircle.grow(10)
            pygame.display.update()


