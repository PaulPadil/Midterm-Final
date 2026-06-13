import pygame

from settings import *

def draw_ui(screen, player, coins):

    pygame.draw.rect(
        screen,
        (60,60,60),
        (10,40,200,20)
    )

    pygame.draw.rect(
        screen,
        (0,255,0),
        (10,40,200 * player.hp/player.max_hp,20)
    )

    screen.blit(
        font.render(
            f"Coins: {coins}",
            True,
            (255,255,0)
        ),
        (10,10)
    )