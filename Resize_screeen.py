import pygame
from pygame.locals import *
from sys import exit

'''
image load
'''
import os.path
filepath = os.path.dirname(__file__)

background_image_filename = 'img/bitcoin.png'
def image_load(image):
    return pygame.image.load(os.path.join(filepath, image))

SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = image_load(background_image_filename).convert()

Fullscreen=False
#print all display size
print(pygame.display.list_modes())

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()

    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)

    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))
    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    pygame.display.update()