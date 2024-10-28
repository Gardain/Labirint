import pygame
import NumberLevel
from game_config import config
from GameMain import GameMain


def initialize_game():
    """Инициализация Pygame и основных настроек окна."""
    pygame.init()
    pygame.display.set_caption('Game Window')
    width, height = config.get_list_values('width', 'height')
    screen = pygame.display.set_mode((width, height))
    config.set_value('screen', screen)
    return screen, pygame.time.Clock(), width, height


def main_game_loop(screen, clock, game, fps=60):
    """Основной игровой цикл."""
    running = True
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


def show_game_over(screen, width, height, duration=5000):
    """Отображение экрана 'Game Over' на указанное время."""
    image = pygame.image.load('data/gameover.png')
    resized_image = pygame.transform.scale(image, (550, 550))
    screen.blit(resized_image, ((width - 550) // 2, (height - 550) // 2))
    pygame.display.flip()

    game_over_start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - game_over_start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.time.Clock().tick(30)  # Поддержка частоты обновления


def main():
    """Главная функция программы."""
    screen, clock, width, height = initialize_game()
    game = GameMain()

    # Запуск основного игрового цикла
    main_game_loop(screen, clock, game)

    # Показ экрана 'Game Over' на 5 секунд
    show_game_over(screen, width, height)

    # Завершение Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
