import math
import random
import pygame
from pygame import mixer

# =====================================================
# INITIALIZE PYGAME
# =====================================================

pygame.init()
mixer.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Space Invader - Galaxy Defender")

# =====================================================
# BACKGROUND
# =====================================================

background = pygame.image.load("Background.png")
background = pygame.transform.scale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Background music
mixer.music.load("Background.wav")
mixer.music.play(-1)

# =====================================================
# ICON
# =====================================================

icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)

# =====================================================
# PLAYER
# =====================================================

playerImg = pygame.image.load("Player.png")

playerX = 370
playerY = 400

playerX_change = 0

# =====================================================
# ENEMIES
# =====================================================

enemyImg = []

enemyX = []
enemyY = []

enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):

    enemyImg.append(
        pygame.image.load("Enemy.png")
    )

    enemyX.append(
        random.randint(0, 736)
    )

    enemyY.append(
        random.randint(50, 150)
    )

    enemyX_change.append(2)
    enemyY_change.append(30)

# =====================================================
# BULLET
# =====================================================

bulletImg = pygame.image.load("Bullet.png")

bulletX = 0
bulletY = 400

bulletY_change = 8

bullet_state = "ready"

# =====================================================
# SCORE
# =====================================================

score_value = 0

font = pygame.font.Font(
    "freesansbold.ttf",
    28
)

big_font = pygame.font.Font(
    "freesansbold.ttf",
    55
)

small_font = pygame.font.Font(
    "freesansbold.ttf",
    22
)

# =====================================================
# GAME VARIABLES
# =====================================================

lives = 3
level = 1

game_running = True
game_over = False
victory = False

# =====================================================
# FUNCTIONS
# =====================================================

def show_score():

    score = font.render(
        "Score: " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(score, (10, 10))


def show_lives():

    life_text = font.render(
        "Lives: " + str(lives),
        True,
        (255, 255, 255)
    )

    screen.blit(
        life_text,
        (650, 10)
    )


def show_level():

    level_text = font.render(
        "Level: " + str(level),
        True,
        (255, 255, 255)
    )

    screen.blit(
        level_text,
        (350, 10)
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


def isCollision(enemyX, enemyY, bulletX, bulletY):

    distance = math.sqrt(
        math.pow(enemyX - bulletX, 2)
        +
        math.pow(enemyY - bulletY, 2)
    )

    if distance < 30:
        return True

    return False


def reset_enemies():

    for i in range(num_of_enemies):

        enemyX[i] = random.randint(
            0,
            736
        )

        enemyY[i] = random.randint(
            50,
            150
        )


def game_over_screen():

    screen.blit(
        background,
        (0, 0)
    )

    text = big_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    screen.blit(
        text,
        (240, 180)
    )

    score_text = font.render(
        "Final Score: " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(
        score_text,
        (290, 250)
    )

    restart_text = small_font.render(
        "Press R to Restart or ESC to Quit",
        True,
        (255, 255, 255)
    )

    screen.blit(
        restart_text,
        (235, 310)
    )


def victory_screen():

    screen.blit(
        background,
        (0, 0)
    )

    text = big_font.render(
        "GALAXY SAVED!",
        True,
        (255, 255, 255)
    )

    screen.blit(
        text,
        (190, 170)
    )

    score_text = font.render(
        "Final Score: " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(
        score_text,
        (290, 240)
    )

    restart_text = small_font.render(
        "Press R to Play Again",
        True,
        (255, 255, 255)
    )

    screen.blit(
        restart_text,
        (285, 300)
    )


# =====================================================
# GAME LOOP
# =====================================================

running = True

while running:

    # -------------------------------------------------
    # EVENTS
    # -------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # KEY DOWN
        if event.type == pygame.KEYDOWN:

            # Quit
            if event.key == pygame.K_ESCAPE:

                running = False

            # Restart
            if event.key == pygame.K_r:

                if game_over or victory:

                    score_value = 0
                    lives = 3
                    level = 1

                    playerX = 370

                    bulletY = 400
                    bullet_state = "ready"

                    game_over = False
                    victory = False

                    for i in range(num_of_enemies):

                        enemyX_change[i] = 2

                    reset_enemies()

            # Player movement
            if event.key == pygame.K_LEFT:

                playerX_change = -6

            if event.key == pygame.K_RIGHT:

                playerX_change = 6

            # Shoot
            if event.key == pygame.K_SPACE:

                if bullet_state == "ready" and not game_over and not victory:

                    bulletX = playerX
                    bulletY = playerY

                    bullet_state = "fire"

                    bulletSound = mixer.Sound(
                        "Laser.wav"
                    )

                    bulletSound.play()

        # KEY UP
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

                playerX_change = 0

            if event.key == pygame.K_RIGHT:

                playerX_change = 0

    # -------------------------------------------------
    # GAME OVER SCREEN
    # -------------------------------------------------

    if game_over:

        game_over_screen()

        pygame.display.update()

        continue

    # -------------------------------------------------
    # VICTORY SCREEN
    # -------------------------------------------------

    if victory:

        victory_screen()

        pygame.display.update()

        continue

    # -------------------------------------------------
    # BACKGROUND
    # -------------------------------------------------

    screen.blit(
        background,
        (0, 0)
    )

    # -------------------------------------------------
    # PLAYER MOVEMENT
    # -------------------------------------------------

    playerX += playerX_change

    if playerX <= 0:

        playerX = 0

    elif playerX >= 736:

        playerX = 736

    # -------------------------------------------------
    # ENEMY MOVEMENT
    # -------------------------------------------------

    enemies_remaining = 0

    for i in range(num_of_enemies):

        # Enemy reached player area
        if enemyY[i] > 350:

            lives -= 1

            enemyX[i] = random.randint(
                0,
                736
            )

            enemyY[i] = random.randint(
                50,
                150
            )

            if lives <= 0:

                game_over = True

        # Move enemy
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:

            enemyX_change[i] = abs(
                enemyX_change[i]
            )

            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 736:

            enemyX_change[i] = -abs(
                enemyX_change[i]
            )

            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(
            enemyX[i],
            enemyY[i],
            bulletX,
            bulletY
        )

        if collision:

            explosionSound = mixer.Sound(
                "Explosion.wav"
            )

            explosionSound.play()

            bulletY = playerY

            bullet_state = "ready"

            score_value += 1

            enemyX[i] = random.randint(
                0,
                736
            )

            enemyY[i] = random.randint(
                50,
                150
            )

        enemy(
            enemyX[i],
            enemyY[i],
            i
        )

        enemies_remaining += 1

    # -------------------------------------------------
    # BULLET MOVEMENT
    # -------------------------------------------------

    if bullet_state == "fire":

        fire_bullet(
            bulletX,
            bulletY
        )

        bulletY -= bulletY_change

    if bulletY <= 0:

        bulletY = playerY

        bullet_state = "ready"

    # -------------------------------------------------
    # LEVEL SYSTEM
    # -------------------------------------------------

    if score_value >= 10 and level == 1:

        level = 2

        for i in range(num_of_enemies):

            enemyX_change[i] = 3

        reset_enemies()

    if score_value >= 25 and level == 2:

        level = 3

        for i in range(num_of_enemies):

            enemyX_change[i] = 4

        reset_enemies()

    # -------------------------------------------------
    # VICTORY
    # -------------------------------------------------

    if score_value >= 40:

        victory = True

    # -------------------------------------------------
    # DRAW PLAYER
    # -------------------------------------------------

    player(
        playerX,
        playerY
    )

    # -------------------------------------------------
    # INFORMATION
    # -------------------------------------------------

    show_score()
    show_level()
    show_lives()

    # -------------------------------------------------
    # UPDATE SCREEN
    # -------------------------------------------------

    pygame.display.update()


pygame.quit()