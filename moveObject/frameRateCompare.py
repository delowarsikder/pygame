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

import os.path
filepath = os.path.dirname(__file__)

def image_load(image):
    return pygame.image.load(os.path.join(filepath, image))


DISPLAY_HEIGHT=480
DISPLAY_WIDTH=640

SCREEN_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = image_load(background_image_filename).convert()

sprite = image_load(sprite_image_filename)
screen.fill((255,255,255))

# Our clock object
clock = pygame.time.Clock()
x1 = 0.
x2 = 0.
# Speed in pixels per second
speed = 250.
frame_no = 0
while True:
    screen.clean()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    screen.blit(sprite, (50,x1))
    screen.blit(sprite, (200,x2))
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed
    x1 += distance_moved
    if (frame_no % 5) == 0:
        distance_moved = time_passed_seconds * speed
        x2 += distance_moved * 5.
    # If the image goes off the end of the screen, move it back
    if x1 > 640.:
        x1 =x1- 640.
    if x2 > 640.:
        x2 =x2- 640.
    pygame.display.update()
    frame_no += 1