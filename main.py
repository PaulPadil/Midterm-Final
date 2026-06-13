import pygame
import random

from settings import *
from world import world
from player import Player
from enemy import Enemy
from ui import draw_ui

# =========================
# INIT
# =========================
def reset_game():
    global player, enemies, coins, weapon_level, weapon_damage, spawn_timer, game_over

    player = Player()
    enemies = []

    coins = 100  # starter money

    weapon_level = 0
    weapon_damage = 5

    spawn_timer = 0

    game_over = False


reset_game()

shop_open = True

spawn_delay = 180
spawn_timer = 0

# =========================
# ATTACK SYSTEM
# =========================
def attack():

    keys = pygame.key.get_pressed()

    if game_over:
        return

    if not player.has_sword:
        return

    if keys[pygame.K_f]:

        if player.facing_right:
            hitbox = pygame.Rect(
                player.rect.right,
                player.rect.y,
                50,
                player.rect.height
            )
        else:
            hitbox = pygame.Rect(
                player.rect.left - 50,
                player.rect.y,
                50,
                player.rect.height
            )

        for enemy in enemies:
            if enemy.hp > 0 and hitbox.colliderect(enemy.rect):
                enemy.hp -= weapon_damage

                if enemy.hp < 0:
                    enemy.hp = 0


# =========================
# GAME LOOP
# =========================
running = True

while running:

    clock.tick(60)

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # restart
            if game_over and event.key == pygame.K_r:
                reset_game()

            # toggle shop
            if event.key == pygame.K_e and not game_over:
                shop_open = not shop_open

            # buy sword
            if event.key == pygame.K_q and shop_open and not game_over:
                if coins >= 30 and not player.has_sword:
                    coins -= 30
                    player.has_sword = True

            # upgrade weapon
            if event.key == pygame.K_r and shop_open and not game_over:

                upgrade_cost = 40 + (weapon_level * 20)

                if coins >= upgrade_cost and player.has_sword:
                    coins -= upgrade_cost
                    weapon_level += 1
                    weapon_damage += 5

    # =========================
    # GAME OVER CHECK
    # =========================
    if player.hp <= 0:
        game_over = True

    # =========================
    # UPDATE
    # =========================
    if not game_over:

        player.move()

        for enemy in enemies:
            enemy.update(player)

        attack()

        # spawn enemies
        spawn_timer += 1

        if spawn_timer >= spawn_delay:
            spawn_timer = 0

            new_enemy = Enemy()

            if random.randint(0, 1) == 0:
                new_enemy.rect.x = 0
            else:
                new_enemy.rect.x = 900

            enemies.append(new_enemy)

        # coin reward
        for enemy in enemies:
            if enemy.hp <= 0 and not enemy.dead_rewarded:
                coins += 50
                enemy.dead_rewarded = True

        enemies = [e for e in enemies if e.hp > 0]

    # =========================
    # DRAW
    # =========================
    screen.blit(background, (0, 0))

    # WORLD
    for y in range(WORLD_H):
        for x in range(WORLD_W):

            tile = world[y][x]

            if tile == 1:
                color = (80, 200, 120)
            elif tile == 2:
                color = (134, 96, 67)
            elif tile == 3:
                color = (120, 120, 120)
            else:
                continue

            pygame.draw.rect(
                screen,
                color,
                (x * TILE, y * TILE, TILE, TILE)
            )

    # ENTITIES
    player.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    # UI
    draw_ui(screen, player, coins)

    # =========================
    # ATTACK GUIDE TEXT
    # =========================
    if not game_over:

        if not player.has_sword:
            screen.blit(
                font.render("Buy Sword (Q) to Unlock Attack", True, (255, 200, 200)),
                (10, 70)
            )
        else:
            screen.blit(
                font.render("Press F to Attack", True, (255, 255, 255)),
                (10, 70)
            )

    # =========================
    # SHOP UI
    # =========================
    if shop_open and not game_over:

        pygame.draw.rect(screen, (30, 30, 30), (700, 100, 250, 220))
        pygame.draw.rect(screen, (255, 255, 255), (700, 100, 250, 220), 2)

        screen.blit(font.render("SHOP", True, (255,255,255)), (710, 110))
        screen.blit(font.render("Q = Buy Sword (30)", True, (255,255,255)), (710, 140))

        upgrade_cost = 40 + (weapon_level * 20)

        screen.blit(font.render(
            f"R = Upgrade ({upgrade_cost})",
            True,
            (255,255,255)
        ), (710, 170))

        screen.blit(font.render(
            f"Damage: {weapon_damage}",
            True,
            (255,255,0)
        ), (710, 200))

    # =========================
    # GAME OVER SCREEN
    # =========================
    if game_over:

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        screen.blit(font.render("YOU DIED", True, (255, 0, 0)), (WIDTH//2 - 60, HEIGHT//2 - 40))
        screen.blit(font.render("Press R to Restart", True, (255, 255, 255)), (WIDTH//2 - 100, HEIGHT//2))

    pygame.display.flip()

pygame.quit()