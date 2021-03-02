import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            exit()

    screen.lock()        
    # rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    rand_col = (randint(0, 255), 100, 0)
    for _ in range(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_col)
    screen.unlock()
    pygame.display.update()
