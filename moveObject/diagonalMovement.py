import os.path
import pygame
from pygame.locals import *
from time import *
from random import *
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

sprite = image_load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()
x, y = 100., 0.
speed_x, speed_y = 100., 130.
cnt = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0, 0, 0))
    # screen.blit(background, (0,0))

    screen.blit(sprite, (x, y))
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds
    # If the sprite goes off the edge of the screen,
    # make it move in the opposite direction
    if x > (640 - sprite.get_width()):
        speed_x = speed_x/-1.
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = speed_x/-1.
        x = 0.
    if y > (480 - sprite.get_height()):
        speed_y = speed_y/-1.
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = speed_y/-1.
        y = 0
    # print("sprit x : ",speed_x,"sprit y: ",speed_y)
    # print(" x : ",x," y: ",y)

    pygame.display.update()
