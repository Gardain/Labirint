from AssetManager import assetManager
import pygame
import random
from config.Config import config


class StartScreen:
    def __init__(self, next_scene):
        self.screen, self.width, self.height = config.get_list_values('screen', 'width', 'height')
        self.animate = False
        self.next_scene = next_scene
        self.timer = None

    def draw(self, dt=None):
        self.draw_background()
        self.draw_text()
        if self.animate:
            self.timer += dt
            self.draw_animate()

    def draw_background(self):
        # Масштабируем изображение фона в зависимости от текущих размеров окна
        bg = pygame.transform.scale(assetManager.load_image('start_screen_bg.jpg'), (self.width, self.height))
        self.screen.blit(bg, (0, 0))

    def start_animate(self):
        self.timer = 0
        self.animate = True

    def draw_animate(self):
        # Анимация случайных белых пикселей на экране
        for i in range(15000):
            self.screen.fill(pygame.Color('white'),
                             (random.random() * self.width,
                              random.random() * self.height, 1, 1))
        if self.timer > 2000:
            self.next_scene()

    def draw_text(self):
        text_lines = ["МЕНЮ", "Нажмите любую клавишу"]
        offset_x, offset_y = 0, 0
        line_offset = 10
        color = pygame.Color('white')
        font_size = 40
        font = pygame.font.Font(None, font_size)
        text_rendered_lines = []

        # Отрисовка текста
        for text_line in text_lines:
            string_rendered = font.render(text_line, True, color)
            rect = string_rendered.get_rect()
            rect.x = offset_x
            rect.y = offset_y
            offset_y += rect.height + line_offset
            text_rendered_lines.append((string_rendered, rect))

        width = max(*text_rendered_lines, key=lambda x: x[1].width)[1].width
        height = offset_y
        surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # Центрируем текст в середине экрана
        for text_line in text_rendered_lines:
            text, rect = text_line
            rect.x = width // 2 - rect.width // 2
            surface.blit(text, rect)
        x = self.width // 2 - width // 2
        y = self.height // 2 - height // 2
        self.screen.blit(surface, pygame.Rect(x, y, width, height))

    def on_event(self, event):
        # Запуск анимации при нажатии клавиши
        if event.type == pygame.KEYUP:
            self.start_animate()
        # Обновление размеров окна при изменении его размера
        elif event.type == pygame.VIDEORESIZE:
            self.width, self.height = event.w, event.h  # Обновляем текущие размеры
            config.set_value('width', self.width)  # Обновляем ширину в config
            config.set_value('height', self.height)  # Обновляем высоту в config

    def update(self):
        pass
