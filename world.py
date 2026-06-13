from settings import *

GROUND_Y = WORLD_H // 2

world = [[0 for _ in range(WORLD_W)] for _ in range(WORLD_H)]

for x in range(WORLD_W):
    for y in range(WORLD_H):

        if y < GROUND_Y:
            world[y][x] = 0
        elif y == GROUND_Y:
            world[y][x] = 1  # grass
        elif y < GROUND_Y + 10:
            world[y][x] = 2  # dirt
        else:
            world[y][x] = 3  # stone


def is_solid(tile):
    return tile in (1, 2, 3)


def check_collision(rect):
    for y in range(rect.top // TILE, rect.bottom // TILE + 1):
        for x in range(rect.left // TILE, rect.right // TILE + 1):
            if 0 <= x < WORLD_W and 0 <= y < WORLD_H:
                if is_solid(world[y][x]):
                    return True
    return False