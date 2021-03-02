import pygame
import random
import os.path

# --- constants --- (UPPER_CASE names)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAR_WITDH = 64

# --- functions --- (lower_case names)

def text_objects(text, font):
    text_image = font.render(text, True, BLACK)
    return text_image, text_image.get_rect()

def message_display(text):
    large_font = pygame.font.Font('font/BalooTamma2-Regular.ttf', 40)
    text_image, text_rect = text_objects(text, large_font)
    text_rect.center = screen_rect.center

    screen.blit(text_image, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)

def crash(score):
    message_display(('You dropped a fruit! Your score was: {}').format(score))

def reset_positions():
    car_rect.x = DISPLAY_WIDTH * 0.45
    car_rect.y = DISPLAY_HEIGHT * 0.8

    apple_rect.x = random.randrange(0, DISPLAY_WIDTH)
    apple_rect.y = -600


def game_loop():
    score = 0

    x_change = 0

    apple_speed = 7

    reset_positions()

    clock = pygame.time.Clock()

    while True:

        # --- events ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        # --- updates (without draws) ---

        car_rect.x += x_change
        apple_rect.y += apple_speed

        if car_rect.right > DISPLAY_WIDTH or car_rect.left < 0:
            crash(score)
            reset_positions()
            score = 0

        if apple_rect.bottom > DISPLAY_HEIGHT:
            crash(score)
            reset_positions()
            score = 0

        if car_rect.colliderect(apple_rect):
            score += 1
            car_rect.y -= 10
            apple_rect.x = random.randrange(0, DISPLAY_WIDTH-apple_rect.width)
            apple_rect.y = -600

        # --- draws (without updates) ---

        screen.fill(WHITE)
        screen.blit(apple_image, apple_rect)
        screen.blit(car_image, car_rect)
        pygame.display.update()

        # --- FPS ---

        clock.tick(60)

# --- main --- (lower_case names)

# - init -


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
screen_rect = screen.get_rect()

pygame.display.set_caption('Avoid The Falling Objects')

# - objects -
'''
image load
'''
car_image_filename = 'img/busket.png'
sprite_image_filename = 'img/football.png'

filepath = os.path.dirname(__file__)


def image_load(image):
    return pygame.image.load(os.path.join(filepath, image))


car_image = image_load(car_image_filename)
car_rect = car_image.get_rect()

apple_image = image_load(sprite_image_filename)
apple_rect = apple_image.get_rect()

# - mainloop -

game_loop()
