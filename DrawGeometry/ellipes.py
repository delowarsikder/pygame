import pygame
from pygame.locals import *
from sys import exit
from random import *
pygame.init()
from time import *
screen = pygame.display.set_mode((640, 480), 0, 32)
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            exit()
    x, y = pygame.mouse.get_pos()
    color=(randint(0,255),randint(0,255),randint(0,255))
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, color, (0,0,x,y))
    sleep(.5)
    pygame.display.update()