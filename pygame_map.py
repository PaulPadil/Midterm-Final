import pygame

# =========================
# SETTINGS
# =========================
WIDTH, HEIGHT = 1000, 600
TILE = 10
WORLD_W = 200
WORLD_H = 100

PLAYER_WIDTH = TILE * 7
PLAYER_HEIGHT = TILE * 5

PLAYER_SPEED = 3
SPRINT_SPEED = 6
JUMP_POWER = -8
GRAVITY = 0.4

# =========================
# INIT
# =========================
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Terraria Style Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# =========================
# BACKGROUND
# =========================
background = pygame.image.load("jungle.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# =========================
# WORLD
# =========================
GROUND_Y = WORLD_H // 2

world = [[0 for x in range(WORLD_W)] for y in range(WORLD_H)]

for x in range(WORLD_W):
    for y in range(WORLD_H):
        if y < GROUND_Y:
            world[y][x] = 0
        elif y == GROUND_Y:
            world[y][x] = 1
        elif y < GROUND_Y + 10:
            world[y][x] = 2
        else:
            world[y][x] = 3

# =========================
# PLAYER (FIXED GROUND SPAWN)
# =========================
player_img = pygame.image.load("MC_idle.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

player = pygame.Rect(
    100,
    GROUND_Y * TILE - PLAYER_HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

# =========================
# NPC (START OF MAP)
# =========================
npc_img = pygame.image.load("player1.png").convert_alpha()
npc_img = pygame.transform.scale(npc_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

npc = pygame.Rect(
    50,
    GROUND_Y * TILE - PLAYER_HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

npc_dir = 1
npc_speed = 1

# =========================
# ENEMY
# =========================
enemy_img = pygame.image.load("player1.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

enemy = pygame.Rect(
    600,
    GROUND_Y * TILE - PLAYER_HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

enemy_speed = 2
enemy_chase_range = 200
enemy_attack_cooldown = 0
enemy_awake = False

# =========================
# PLAYER DATA
# =========================
vel_y = 0
on_ground = False
facing_right = True

# =========================
# GAME DATA
# =========================
coins = 100
inventory = []
shop_open = False
inventory_open = False
sword_price = 30

bag_rect = pygame.Rect(950, 10, 40, 40)

# =========================
# HEALTH
# =========================
player_hp = 100
player_max_hp = 100
game_over = False

# =========================
# RESTART BUTTON
# =========================
restart_btn = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 60)

# =========================
# COLLISION
# =========================
def is_solid(tile):
    return tile in (1, 2, 3)

def check_collision(rect):
    for y in range(rect.top // TILE, rect.bottom // TILE + 1):
        for x in range(rect.left // TILE, rect.right // TILE + 1):
            if 0 <= x < WORLD_W and 0 <= y < WORLD_H:
                if is_solid(world[y][x]):
                    return True
    return False

# =========================
# RESET GAME (FIXED GROUND)
# =========================
def reset_game():
    global player, enemy, coins, inventory
    global player_hp, game_over, enemy_awake, enemy_attack_cooldown
    global vel_y

    player.x = 100
    player.y = GROUND_Y * TILE - player.height

    enemy.x = 600
    enemy.y = GROUND_Y * TILE - enemy.height

    coins = 100
    inventory = []

    player_hp = 100
    game_over = False

    enemy_awake = False
    enemy_attack_cooldown = 0
    vel_y = 0

# =========================
# PLAYER MOVEMENT
# =========================
def move_player():
    global vel_y, on_ground, facing_right

    keys = pygame.key.get_pressed()

    speed = PLAYER_SPEED
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        speed = SPRINT_SPEED

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
        facing_right = False
        if check_collision(player):
            player.x += speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
        facing_right = True
        if check_collision(player):
            player.x -= speed

    vel_y += GRAVITY
    if vel_y > 10:
        vel_y = 10

    player.y += vel_y

    if check_collision(player):
        while check_collision(player):
            player.y -= 1
        vel_y = 0
        on_ground = True
    else:
        on_ground = False

    if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and on_ground:
        vel_y = JUMP_POWER

# =========================
# NPC MOVE
# =========================
def move_npc():
    global npc_dir

    npc.y = GROUND_Y * TILE - npc.height

    npc.x += npc_speed * npc_dir

    if npc.x < 0:
        npc.x = 0
        npc_dir = 1

    if npc.x > 200:
        npc.x = 200
        npc_dir = -1

# =========================
# ENEMY AI
# =========================
def move_enemy():
    global enemy_attack_cooldown, enemy_awake, player_hp

    enemy.y = GROUND_Y * TILE - enemy.height

    distance = player.x - enemy.x

    if abs(distance) < enemy_chase_range:
        enemy_awake = True

    if not enemy_awake:
        return

    if distance > 0:
        enemy.x += enemy_speed
    else:
        enemy.x -= enemy_speed

    if enemy.x < 0:
        enemy.x = 0
    if enemy.x > WORLD_W * TILE - enemy.width:
        enemy.x = WORLD_W * TILE - enemy.width

    if enemy_attack_cooldown > 0:
        enemy_attack_cooldown -= 1

    if player.colliderect(enemy) and enemy_attack_cooldown == 0:
        player_hp -= 10
        if player_hp < 0:
            player_hp = 0
        enemy_attack_cooldown = 60

# =========================
# PIXEL TEXT
# =========================
def draw_pixel_text(text, x, y, color=(255,255,255), size=40):
    font = pygame.font.SysFont("Courier", size, bold=True)
    screen.blit(font.render(text, True, color), (x, y))

# =========================
# DRAW
# =========================
def draw():

    screen.blit(background, (0, 0))

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

            pygame.draw.rect(screen, color, (x * TILE, y * TILE, TILE, TILE))

    screen.blit(npc_img, (npc.x, npc.y))
    screen.blit(enemy_img, (enemy.x, enemy.y))

    img = player_img
    if not facing_right:
        img = pygame.transform.flip(img, True, False)

    screen.blit(img, (player.x, player.y))

    # HP
    pygame.draw.rect(screen, (60, 60, 60), (10, 40, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 40, 200 * (player_hp / player_max_hp), 20))
    screen.blit(font.render(f"HP: {player_hp}", True, (255,255,255)), (10, 65))

    # COINS
    screen.blit(font.render(f"Coins: {coins}", True, (255,255,0)), (10, 10))

    # BAG
    pygame.draw.rect(screen, (139, 69, 19), bag_rect)
    pygame.draw.rect(screen, (255,255,255), bag_rect, 2)

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        draw_pixel_text("GAME OVER", WIDTH//2 - 170, HEIGHT//2 - 120, (255,0,0), 50)

        pygame.draw.rect(screen, (80,80,80), restart_btn)
        pygame.draw.rect(screen, (255,255,255), restart_btn, 3)

        draw_pixel_text("RESTART", restart_btn.x + 35, restart_btn.y + 15, (255,255,255), 30)

# =========================
# LOOP
# =========================
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_btn.collidepoint(event.pos):
                reset_game()

    if not game_over:
        move_player()
        move_npc()
        move_enemy()

    if player_hp <= 0:
        game_over = True

    draw()
    pygame.display.flip()

pygame.quit()