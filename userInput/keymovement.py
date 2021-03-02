from gameobjects.vector2 import Vector2
from sys import exit
from pygame.locals import *
import pygame
import os.path
filepath=os.path.dirname(__file__)

###load image
def image_load(img):
    return pygame.image.load(os.path.join(filepath,img))

background_image_filename = '../img/nature.jpg'
sprite_image_filename = '../img/bitcoin.png'
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = image_load(background_image_filename).convert()
sprite = image_load(sprite_image_filename).convert_alpha()
clock = pygame.time.Clock()
# sprite_pos = Vector2(200, 150)
sprite_pos=(200,150)
sprite_speed = 300.
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()
    key_direction = Vector2(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1
    # key_direction.normalize()
    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    sprite_pos += key_direction * sprite_speed * time_passed_seconds
    pygame.display.update()