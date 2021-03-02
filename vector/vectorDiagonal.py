import os.path
import pygame
from pygame.locals import *
from time import *
from random import *
from sys import exit
from Vector2Class import Vector2


pygame.init()

'''
image load
'''
background_image_filename = '../img/nature.jpg'
sprite_image_filename = '../img/football.png'

filepath = os.path.dirname(__file__)


def image_load(image):
    return pygame.image.load(os.path.join(filepath, image))


DISPLAY_HEIGHT = 480
DISPLAY_WIDTH = 640

SCREEN_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = image_load(background_image_filename).convert()

sprite = image_load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()
position = Vector2(100, 100)
speed = 250.
heading = Vector2()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
    if event.type == MOUSEBUTTONDOWN:
        destination = Vector2(*event.pos)-Vector2(*sprite.get_size())*(1/2)
        heading = Vector2.from_points(position, destination)
        heading.normalize()
    screen.blit(background, (0, 0))
    screen.blit(sprite, position)
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed
    position += heading * distance_moved
    pygame.display.update()
