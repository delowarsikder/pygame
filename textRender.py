import pygame
from pygame.locals import *

my_name = "DELOWAR SIKDER CSE2k16"

pygame.init()

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480
screen_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

try:
    screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
except pygame.error as e:
    print ("Can't create the display :-(")
    print (e)
    exit()
font=pygame.font.get_fonts()
# my_font = pygame.font.SysFont(font[0], 32)
my_font=pygame.font.Font('E:/PythonPractice/pygame/book/font/BalooTamma2-ExtraBold.ttf',20)
# name_surface = my_font.render(my_name, True, (255, 255, 255),None)
# pygame.image.save(name_surface, "E:/PythonPractice/pygame/book/name.png")

running = True
i=0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    name_surface = my_font.render(my_name, True, (255, 255, 255),None)
    screen.blit(name_surface,(10,20))
    pygame.display.flip()        