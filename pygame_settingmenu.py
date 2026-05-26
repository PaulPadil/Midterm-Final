import pygame

from pygame_setting import *
from pygame_button import Button

menu_font = pygame.font.SysFont(
    "timesnewroman",
    50
)

button_font = pygame.font.SysFont(
    "timesnewroman",
    40
)

class SettingsMenu:

    def __init__(self):

        button_width = 320
        button_height = 70

        center_x = WIDTH // 2 - button_width // 2

        self.fullscreen_button = Button(
            "Toggle Fullscreen",
            center_x,
            320,
            button_width,
            button_height
        )

        self.back_button = Button(
            "Back",
            center_x,
            430,
            button_width,
            button_height
        )

    def draw(self, screen, fullscreen):

        title = menu_font.render(
            "SETTINGS",
            True,
            GOLD
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 170)
        )

        screen.blit(title, title_rect)

        status = "ON" if fullscreen else "OFF"

        status_text = button_font.render(
            f"Fullscreen: {status}",
            True,
            WHITE
        )

        status_rect = status_text.get_rect(
            center=(WIDTH // 2, 260)
        )

        screen.blit(status_text, status_rect)

        self.fullscreen_button.draw(screen)
        self.back_button.draw(screen)