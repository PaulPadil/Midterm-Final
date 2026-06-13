import pygame

from settings import *
from world import *

class NPC:

    def __init__(self):

        self.image = pygame.image.load("player1.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        self.rect = pygame.Rect(
            50,
            GROUND_Y * TILE - PLAYER_HEIGHT,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

        self.direction = 1

    def update(self):

        self.rect.x += self.direction

        if self.rect.x < 0:
            self.direction = 1

        if self.rect.x > 200:
            self.direction = -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)