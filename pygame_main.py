import pygame
import sys
import os

from pygame_setting import *

from pygame_mainmenu import MainMenu
from pygame_settingmenu import SettingsMenu

pygame.init()

# =========================
# SCREEN
# =========================
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

# =========================
# LOAD BACKGROUND
# =========================
def load_background():

    if os.path.exists(BACKGROUND_IMAGE):

        bg = pygame.image.load(
            BACKGROUND_IMAGE
        )

        bg = pygame.transform.scale(
            bg,
            (WIDTH, HEIGHT)
        )

        return bg

    else:

        surface = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        surface.fill((30, 30, 40))

        return surface

background = load_background()

# =========================
# SCENES
# =========================
main_menu = MainMenu()
settings_menu = SettingsMenu()

MAIN_MENU = "main_menu"
SETTINGS = "settings"

current_scene = MAIN_MENU

fullscreen = False

# =========================
# FULLSCREEN
# =========================
def toggle_fullscreen():

    global screen
    global fullscreen

    fullscreen = not fullscreen

    if fullscreen:
        screen = pygame.display.set_mode(
            (WIDTH, HEIGHT),
            pygame.FULLSCREEN
        )
    else:
        screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

# =========================
# GAME LOOP
# =========================
running = True

while running:

    # =========================
    # BACKGROUND
    # =========================
    screen.blit(background, (0, 0))

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 120))

    screen.blit(overlay, (0, 0))

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # =========================
        # MAIN MENU
        # =========================
        if current_scene == MAIN_MENU:

            if main_menu.play_button.clicked(event):
                print("Start Game")

            if main_menu.settings_button.clicked(event):
                current_scene = SETTINGS

            if main_menu.exit_button.clicked(event):
                pygame.quit()
                sys.exit()

        # =========================
        # SETTINGS MENU
        # =========================
        elif current_scene == SETTINGS:

            if settings_menu.fullscreen_button.clicked(event):
                toggle_fullscreen()

            if settings_menu.back_button.clicked(event):
                current_scene = MAIN_MENU

    # =========================
    # DRAW SCENES
    # =========================
    if current_scene == MAIN_MENU:
        main_menu.draw(screen)

    elif current_scene == SETTINGS:
        settings_menu.draw(screen, fullscreen)

    # =========================
    # UPDATE
    # =========================
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()