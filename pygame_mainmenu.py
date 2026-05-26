import pygame

from pygame_setting import *
from pygame_button import Button

title_font = pygame.font.SysFont(
    "timesnewroman",
    90,
    bold=True
)

class MainMenu:

    def __init__(self):

        button_width = 320
        button_height = 70

        center_x = WIDTH // 2 - button_width // 2

        self.play_button = Button(
            "Play",
            center_x,
            300,
            button_width,
            button_height
        )

        self.settings_button = Button(
            "Settings",
            center_x,
            400,
            button_width,
            button_height
        )

        self.exit_button = Button(
            "Exit",
            center_x,
            500,
            button_width,
            button_height
        )

    def draw(self, screen):

        title = title_font.render(
            TITLE,
            True,
            GOLD
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 150)
        )

        screen.blit(title, title_rect)

        pygame.draw.line(
            screen,
            GOLD,
            (400, 220),
            (880, 220),
            3
        )

        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.exit_button.draw(screen)