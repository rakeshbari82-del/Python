# 🚀 SPACE INVADER - GALAXY DEFENDER
# Today's Class Project + Extra Features

import math
import random
import pygame

# --------------------------------------------------
# GAME SETTINGS
# --------------------------------------------------

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_START_X = 370
PLAYER_START_Y = 420

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 160

ENEMY_SPEED_X = 3
ENEMY_SPEED_Y = 35

BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

NUM_OF_ENEMIES = 8

# --------------------------------------------------
# INITIALIZE PYGAME
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("🚀 Galaxy Defender")

clock = pygame.time.Clock()

# --------------------------------------------------
# LOAD AND RESIZE IMAGES
# --------------------------------------------------

icon = pygame.image.load("UFO.png")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

playerImg = pygame.image.load("Rocket Player.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))

enemyImage = pygame.image.load("Enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (64, 64))

bulletImg = pygame.image.load("Bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32, 32))

# --------------------------------------------------
# PLAYER VARIABLES
# --------------------------------------------------

playerX = PLAYER_START_X
playerY = PLAYER_START_Y

playerX_change = 0

# --------------------------------------------------
# ENEMY VARIABLES
# --------------------------------------------------

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(NUM_OF_ENEMIES):

    enemyImg.append(enemyImage)

    enemyX.append(
        random.randint(0, SCREEN_WIDTH - 64)
    )

    enemyY.append(
        random.randint(
            ENEMY_START_Y_MIN,
            ENEMY_START_Y_MAX
        )
    )

    enemyX_change.append(ENEMY_SPEED_X)

    enemyY_change.append(ENEMY_SPEED_Y)

# --------------------------------------------------
# BULLET VARIABLES
# --------------------------------------------------

bulletX = 0
bulletY = PLAYER_START_Y

bulletX_change = 0
bulletY_change = BULLET_SPEED_Y

bullet_state = "ready"

# --------------------------------------------------
# SCORE / GAME VARIABLES
# --------------------------------------------------

score_value = 0

lives = 3

level = 1

high_score = 0

game_over = False

paused = False

# --------------------------------------------------
# FONTS
# --------------------------------------------------

font = pygame.font.Font(
    "freesansbold.ttf",
    24
)

big_font = pygame.font.Font(
    "freesansbold.ttf",
    55
)

small_font = pygame.font.Font(
    "freesansbold.ttf",
    18
)

# --------------------------------------------------
# CREATE SPACE STARS
# --------------------------------------------------

stars = []

for i in range(80):

    stars.append(
        [
            random.randint(0, SCREEN_WIDTH),
            random.randint(0, SCREEN_HEIGHT),
            random.randint(1, 3)
        ]
    )

# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def draw_background():

    # Dark space background
    screen.fill((5, 5, 30))

    # Draw stars
    for star in stars:

        x = star[0]
        y = star[1]
        size = star[2]

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (x, y),
            size
        )


def show_score():

    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(score, (15, 15))


def show_lives():

    life_text = font.render(
        "Lives : " + str(lives),
        True,
        (255, 255, 255)
    )

    screen.blit(
        life_text,
        (300, 15)
    )


def show_level():

    level_text = font.render(
        "Level : " + str(level),
        True,
        (255, 255, 255)
    )

    screen.blit(
        level_text,
        (650, 15)
    )


def player(x, y):

    screen.blit(
        playerImg,
        (x, y)
    )


def enemy(x, y, i):

    screen.blit(
        enemyImg[i],
        (x, y)
    )


def fire_bullet(x, y):

    global bullet_state

    bullet_state = "fire"

    screen.blit(
        bulletImg,
        (x + 16, y + 10)
    )


def isCollision(
    enemyX,
    enemyY,
    bulletX,
    bulletY
):

    distance = math.sqrt(
        (enemyX - bulletX) ** 2
        +
        (enemyY - bulletY) ** 2
    )

    return distance < COLLISION_DISTANCE


def game_over_screen():

    game_over_text = big_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    restart_text = font.render(
        "Press R to Restart",
        True,
        (255, 255, 255)
    )

    quit_text = font.render(
        "Press ESC to Quit",
        True,
        (255, 255, 255)
    )

    final_score = font.render(
        "Final Score : " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(
        game_over_text,
        (235, 180)
    )

    screen.blit(
        final_score,
        (290, 260)
    )

    screen.blit(
        restart_text,
        (285, 310)
    )

    screen.blit(
        quit_text,
        (300, 350)
    )


def level_up():

    global level

    # Every 5 points = new level
    level = (score_value // 5) + 1


def restart_game():

    global playerX
    global playerY
    global playerX_change
    global score_value
    global lives
    global level
    global bullet_state
    global bulletY
    global game_over
    global paused

    playerX = PLAYER_START_X
    playerY = PLAYER_START_Y

    playerX_change = 0

    score_value = 0

    lives = 3

    level = 1

    bullet_state = "ready"

    bulletY = PLAYER_START_Y

    game_over = False

    paused = False

    # Reset enemies

    for i in range(NUM_OF_ENEMIES):

        enemyX[i] = random.randint(
            0,
            SCREEN_WIDTH - 64
        )

        enemyY[i] = random.randint(
            ENEMY_START_Y_MIN,
            ENEMY_START_Y_MAX
        )

        enemyX_change[i] = ENEMY_SPEED_X


# --------------------------------------------------
# MAIN GAME LOOP
# --------------------------------------------------

running = True

while running:

    clock.tick(60)

    draw_background()

    # --------------------------------------------------
    # EVENTS
    # --------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # Keyboard pressed
        if event.type == pygame.KEYDOWN:

            # ESC = Quit
            if event.key == pygame.K_ESCAPE:

                running = False

            # LEFT
            if event.key == pygame.K_LEFT:

                playerX_change = -5

            # RIGHT
            if event.key == pygame.K_RIGHT:

                playerX_change = 5

            # SPACE = Shoot
            if (
                event.key == pygame.K_SPACE
                and bullet_state == "ready"
                and not game_over
                and not paused
            ):

                bulletX = playerX

                bulletY = playerY

                fire_bullet(
                    bulletX,
                    bulletY
                )

            # P = Pause
            if (
                event.key == pygame.K_p
                and not game_over
            ):

                paused = not paused

            # R = Restart
            if (
                event.key == pygame.K_r
                and game_over
            ):

                restart_game()

        # Keyboard released
        if (
            event.type == pygame.KEYUP
            and event.key in [
                pygame.K_LEFT,
                pygame.K_RIGHT
            ]
        ):

            playerX_change = 0

    # --------------------------------------------------
    # PAUSE SCREEN
    # --------------------------------------------------

    if paused:

        pause_text = big_font.render(
            "PAUSED",
            True,
            (255, 255, 255)
        )

        continue_text = font.render(
            "Press P to Continue",
            True,
            (255, 255, 255)
        )

        screen.blit(
            pause_text,
            (300, 200)
        )

        screen.blit(
            continue_text,
            (285, 280)
        )

        show_score()
        show_lives()
        show_level()

        pygame.display.update()

        continue

    # --------------------------------------------------
    # GAME OVER SCREEN
    # --------------------------------------------------

    if game_over:

        game_over_screen()

        pygame.display.update()

        continue

    # --------------------------------------------------
    # PLAYER MOVEMENT
    # --------------------------------------------------

    playerX += playerX_change

    # Keep player inside screen

    playerX = max(
        0,
        min(
            playerX,
            SCREEN_WIDTH - 64
        )
    )

    # --------------------------------------------------
    # ENEMY MOVEMENT
    # --------------------------------------------------

    for i in range(NUM_OF_ENEMIES):

        # Enemy reaches player area
        if enemyY[i] > 370:

            lives -= 1

            enemyX[i] = random.randint(
                0,
                SCREEN_WIDTH - 64
            )

            enemyY[i] = random.randint(
                ENEMY_START_Y_MIN,
                ENEMY_START_Y_MAX
            )

            # No lives left
            if lives <= 0:

                game_over = True

                if score_value > high_score:

                    high_score = score_value

                break

        # Enemy movement
        enemyX[i] += enemyX_change[i]

        # Enemy touches edge
        if (
            enemyX[i] <= 0
            or enemyX[i] >= SCREEN_WIDTH - 64
        ):

            enemyX_change[i] *= -1

            enemyY[i] += enemyY_change[i]

        # --------------------------------------------------
        # COLLISION
        # --------------------------------------------------

        if isCollision(
            enemyX[i],
            enemyY[i],
            bulletX,
            bulletY
        ):

            bulletY = PLAYER_START_Y

            bullet_state = "ready"

            score_value += 1

            # Respawn enemy
            enemyX[i] = random.randint(
                0,
                SCREEN_WIDTH - 64
            )

            enemyY[i] = random.randint(
                ENEMY_START_Y_MIN,
                ENEMY_START_Y_MAX
            )

            # Level calculation
            level_up()

            # Increase enemy speed
            for j in range(NUM_OF_ENEMIES):

                if enemyX_change[j] > 0:

                    enemyX_change[j] = (
                        ENEMY_SPEED_X
                        + level - 1
                    )

                else:

                    enemyX_change[j] = -(
                        ENEMY_SPEED_X
                        + level - 1
                    )

        # Draw enemy
        enemy(
            enemyX[i],
            enemyY[i],
            i
        )

    # --------------------------------------------------
    # BULLET MOVEMENT
    # --------------------------------------------------

    if bulletY <= 0:

        bulletY = PLAYER_START_Y

        bullet_state = "ready"

    elif bullet_state == "fire":

        fire_bullet(
            bulletX,
            bulletY
        )

        bulletY -= bulletY_change

    # --------------------------------------------------
    # DRAW PLAYER
    # --------------------------------------------------

    player(
        playerX,
        playerY
    )   

    # --------------------------------------------------
    # DISPLAY INFORMATION
    # --------------------------------------------------

    show_score()

    show_lives()

    show_level()

    # --------------------------------------------------
    # UPDATE SCREEN
    # --------------------------------------------------

    pygame.display.update()


pygame.quit()