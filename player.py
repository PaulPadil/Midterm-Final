import pygame
from settings import *
from world import world, is_solid

class Player:

    def __init__(self):

        # =========================
        # SIZE / HITBOX
        # =========================
        self.rect = pygame.Rect(
            100,
            0,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

        self.vel_y = 0
        self.on_ground = False

        self.facing_right = True

        self.hp = 100
        self.max_hp = 100

        self.has_sword = False

        # =========================
        # LOAD SPRITE
        # =========================
        self.image = pygame.image.load("MC_idle.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        # =========================
        # PLACE PLAYER ON GROUND (IMPORTANT)
        # =========================
        self.place_on_ground()

    # =========================
    # FIND GROUND BELOW PLAYER
    # =========================
    def place_on_ground(self):

        while True:
            self.rect.y += 1
            if self.collides_world():
                self.rect.y -= 1
                break

    # =========================
    # WORLD COLLISION CHECK
    # =========================
    def collides_world(self):

        for y in range(self.rect.top // TILE, self.rect.bottom // TILE + 1):
            for x in range(self.rect.left // TILE, self.rect.right // TILE + 1):

                if 0 <= x < WORLD_W and 0 <= y < WORLD_H:

                    if is_solid(world[y][x]):
                        return True

        return False

    # =========================
    # MOVEMENT
    # =========================
    def move(self):

        keys = pygame.key.get_pressed()

        speed = PLAYER_SPEED

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = SPRINT_SPEED

        # LEFT
        if keys[pygame.K_a]:
            self.rect.x -= speed
            self.facing_right = False

            if self.collides_world():
                self.rect.x += speed

        # RIGHT
        if keys[pygame.K_d]:
            self.rect.x += speed
            self.facing_right = True

            if self.collides_world():
                self.rect.x -= speed

        # GRAVITY
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.collides_world():
            self.rect.y -= self.vel_y

            if self.vel_y > 0:
                self.on_ground = True

            self.vel_y = 0
        else:
            self.on_ground = False

        # JUMP
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_POWER

    # =========================
    # DRAW
    # =========================
    def draw(self, screen):

        img = self.image

        if not self.facing_right:
            img = pygame.transform.flip(img, True, False)

        screen.blit(img, self.rect)

        # =========================
        # SWORD VISUAL
        # =========================
        if self.has_sword:

            if self.facing_right:
                sword = pygame.Rect(
                    self.rect.right,
                    self.rect.y + self.rect.height // 2,
                    15,
                    5
                )
            else:
                sword = pygame.Rect(
                    self.rect.left - 15,
                    self.rect.y + self.rect.height // 2,
                    15,
                    5
                )

            pygame.draw.rect(screen, (220, 220, 220), sword)