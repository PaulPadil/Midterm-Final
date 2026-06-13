import pygame

WIDTH, HEIGHT = 1000, 600
TILE = 10

WORLD_W = 200
WORLD_H = 100

PLAYER_SPEED = 3
SPRINT_SPEED = 6
JUMP_POWER = -8
GRAVITY = 0.4

PLAYER_WIDTH = TILE * 7
PLAYER_HEIGHT = TILE * 5

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# LOAD BACKGROUND HERE (IMPORTANT FIX)
background = pygame.image.load("jungle.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))