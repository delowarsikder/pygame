import pygame
from pygame.locals import *
from sys import exit

'''
image load
'''
import os.path
filepath = os.path.dirname(__file__)
def image_load(image):
    return  pygame.image.load(os.path.join(filepath, image))


background_image_filename = 'img/car1.jpg'
mouse_image_filename = 'img/football.png'
pygame.init()
DISPLAY_WIDTH=800
DISPLAY_HEIGHT=600  
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
pygame.display.set_caption("Hello, World!")
background = image_load(background_image_filename).convert()
mouse_cursor =image_load(mouse_image_filename).convert_alpha()

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # screen.blit(background, (0, 0))
    x, y=pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()
