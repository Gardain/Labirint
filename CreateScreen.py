import pygame
from game_config import config


def create_screen():
    width, height = config.get_list_values('width', 'height')
    size = width, height
    screen = pygame.display.set_mode(size)
    return screen
