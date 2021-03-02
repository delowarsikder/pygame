import pygame
from pygame.locals import *
from sys import exit
from random import *
from time import *
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            exit()
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_radius = randint(1,200)
    pygame.draw.circle(screen, random_color, random_pos, random_radius)
    # clock.tick(10)
    sleep(.5)
    pygame.display.update()