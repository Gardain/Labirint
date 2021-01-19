import pygame
import NumberLevel
import time

from game_config import config
from GameMain import GameMain


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    width, height = config.get_list_values('width', 'height')
    size = width, height
    screen = pygame.display.set_mode(size)
    config.set_value('screen', screen)
    clock = pygame.time.Clock()
    running = True
    game = GameMain()
    fps = 60
    dt = 0
    while running:
        for event in pygame.event.get():
            game.on_event(event)
            if event.type == pygame.QUIT:
                running = False
        game.draw(dt)
        game.update()
        NumberLevel.draw_number_level(screen, config.get_value('level'))
        pygame.display.flip()
        dt = clock.tick(fps)
    image = pygame.image.load('data/gameover.png')
    screen.blit(image, (0, 0))
    time.sleep(5)
    pygame.quit()
