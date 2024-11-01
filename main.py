import pygame
import NumberLevel
from game_config import config
from GameMain import GameMain
from StartScreen import StartScreen


def initialize_game():
    """Инициализация Pygame и основных настроек окна."""
    pygame.init()
    pygame.display.set_caption('Game Window')
    width, height = config.get_list_values('width', 'height')
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    config.set_value('screen', screen)
    return screen, pygame.time.Clock(), width, height


def main_game_loop(screen, clock, game, fps=60):
    """Основной игровой цикл."""
    running = True
    dt = 0
    width, height = screen.get_size()  # Инициализация текущих размеров экрана

    while running:
        for event in pygame.event.get():
            game.on_event(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Обновляем размеры экрана в config при изменении
                width, height = event.w, event.h
                config.set_value('width', width)
                config.set_value('height', height)

        screen.fill((0, 0, 0))  # Очистка экрана
        game.draw(dt)
        game.update()

        # Отображение уровня и обновление экрана
        NumberLevel.draw_number_level(screen, config.get_value('level'))
        pygame.display.flip()  # Перерисовка экрана
        dt = clock.tick(fps)  # Ограничиваем FPS


def show_game_over(screen, width, height, duration=5000):
    """Отображение экрана 'Game Over' на указанное время."""
    image = pygame.image.load('data/gameover.png')

    game_over_start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - game_over_start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.VIDEORESIZE:
                # Обновляем размеры экрана в config при изменении
                width, height = event.w, event.h
                config.set_value('width', width)
                config.set_value('height', height)

        # Масштабируем изображение под текущие размеры окна
        resized_image = pygame.transform.scale(image, (width, height))
        screen.fill((0, 0, 0))  # Очистка экрана перед рисованием
        screen.blit(resized_image, (0, 0))  # Отображаем изображение, начиная с левого верхнего угла
        pygame.display.flip()

        pygame.time.Clock().tick(30)  # Поддержка частоты обновления


def main():
    """Главная функция программы."""
    screen, clock, width, height = initialize_game()
    game = GameMain()

    # Запуск основного игрового цикла
    main_game_loop(screen, clock, game)

    # Показ экрана 'Game Over' на 5 секунд
    width, height = screen.get_size()
    show_game_over(screen, width, height)

    # Завершение Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
