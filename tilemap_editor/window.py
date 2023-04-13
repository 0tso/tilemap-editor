import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

WINDOW_TITLE = "Tilemap editor"

SCREEN_CLEAR_COLOR = (255, 255, 255)

def init():
    global screen

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

def clear():
    screen.fill(SCREEN_CLEAR_COLOR)

def blit():
    pygame.display.flip()