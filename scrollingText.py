import os.path
import pygame
from pygame.locals import *
from sys import exit
pygame.init()

'''
image load
'''
filepath = os.path.dirname(__file__)


def image_load(image_name):
    try:
        image = pygame.image.load(os.path.join(filepath, image_name))
    except pygame.error as message:
        print("Cannot load image: " + image_name)
        raise SystemExit(message)
    return image


background_image_filename = 'img/car1.jpg'

SCREEN_SIZE = (640, 480)
# message = " This is a demonstration of the scrolly message script. "
message = "Delowar Sikder "


screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.SysFont("arial", 80)
text_surface = font.render(message, True, (0, 10, 55), (100, 200, 10))
x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2
background = image_load(background_image_filename).convert()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # screen.blit(background, (0, 0))
    x -= .05
    if x < -text_surface.get_width():
        x = 0
    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x+text_surface.get_width(), y))
    pygame.display.update()
