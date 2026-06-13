import pygame
from settings import *
from world import GROUND_Y

class Enemy:

    def __init__(self):

        # LOAD IMAGE
        self.image = pygame.image.load("player1.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        # ✅ FIXED: spawn on ground
        self.rect = pygame.Rect(
            600,
            GROUND_Y * TILE - PLAYER_HEIGHT,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

        self.hp = 100
        self.max_hp = 100

        self.speed = 2
        self.attack_cd = 0
        self.awake = False

        self.dead_rewarded = False

    def update(self, player):

        if self.hp <= 0:
            return

        if abs(player.rect.x - self.rect.x) < 250:
            self.awake = True

        if not self.awake:
            return

        if player.rect.x > self.rect.x:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

        if self.attack_cd > 0:
            self.attack_cd -= 1

        if self.rect.colliderect(player.rect) and self.attack_cd == 0:
            player.hp -= 10
            self.attack_cd = 60

    def draw(self, screen):

        if self.hp <= 0:
            return

        screen.blit(self.image, self.rect)

        # HP BAR
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (self.rect.x, self.rect.y - 10, 60, 6)
        )

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                self.rect.x,
                self.rect.y - 10,
                60 * self.hp / self.max_hp,
                6
            )
        )