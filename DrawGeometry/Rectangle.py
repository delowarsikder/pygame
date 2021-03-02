import pygame
from pygame.locals import *
from sys import exit
from random import *
from time import *
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
screen_color = (150, 200, 200)  # RGB
screen.fill(screen_color)  
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    # draw rectangle in random position
    # for count in range(1):
    sleep(0.3)
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0],639), 479-randint (random_pos[1],479))
    pygame.draw.rect(screen, (random_color), Rect(random_pos, random_size))
    # pygame.draw.rect(screen, (0,100,250), Rect(100,150, 150,200)) #draw rectangle fixed sixe and position
    screen.unlock()
    pygame.display.update()