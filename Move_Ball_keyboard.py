import pygame
from pygame.locals import *
from sys import exit


'''stat game section'''
pygame.init()

'''
image load
'''
import os.path
filepath = os.path.dirname(__file__)

def image_load(image_name):  
    try:
        image = pygame.image.load(os.path.join(filepath, image_name))   
    except pygame.error as message:   
        print("Cannot load image: " + image_name)
        raise SystemExit(message)    
    return image
background_image_filename = 'img/bitcoin.png'

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480
screen_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
background = image_load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = +1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = +1
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0

        #control screen
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        DISPLAY_WIDTH,DISPLAY_HEIGHT=SCREEN_SIZE
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))

    
    x += move_x
    y += move_y
    screen.fill((0, 100, 50))

# check boundary
    if x <= 0:
        x = 0
    elif x >= DISPLAY_WIDTH-30:
        x = DISPLAY_WIDTH-30
    if y <= 0:
        y = 0
    elif y >= DISPLAY_HEIGHT-30:
        y = DISPLAY_HEIGHT-30

    screen.blit(background, (x, y))
    pygame.display.flip()
