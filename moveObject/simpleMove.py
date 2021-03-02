import os.path
import pygame
from pygame.locals import *
from time import *
from random import *
from time import *
from sys import exit
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

sprite = image_load(sprite_image_filename)
# Our clock object
clock = pygame.time.Clock()
# x, y coordinate of our sprite
y = 0.
x = 0.
# Speed in pixels per second
speed = 250.

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, (100, y))  # move vertical
    pygame.draw.circle(screen, (100, 50, 20),(int(x+20), 100), int(sprite.get_width()/2))  # move horizontal
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed
    x += distance_moved
    y += distance_moved

    # If the image goes off the end of the screen, move it back
    if y > DISPLAY_HEIGHT:
        y = y - DISPLAY_HEIGHT

    if x > DISPLAY_WIDTH:
        x = x - DISPLAY_WIDTH

    pygame.display.update()
