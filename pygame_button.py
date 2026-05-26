import pygame
from pygame_setting import WHITE, HOVER, GOLD

pygame.font.init()

button_font = pygame.font.SysFont("timesnewroman", 40)

class Button:

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            text_color = HOVER
            border_color = GOLD
        else:
            text_color = WHITE
            border_color = (120, 90, 40)

        # Background
        pygame.draw.rect(
            surface,
            (25, 25, 25),
            self.rect,
            border_radius=12
        )

        # Border
        pygame.draw.rect(
            surface,
            border_color,
            self.rect,
            3,
            border_radius=12
        )

        # Text
        text_surface = button_font.render(
            self.text,
            True,
            text_color
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        surface.blit(text_surface, text_rect)

    def clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

        return False