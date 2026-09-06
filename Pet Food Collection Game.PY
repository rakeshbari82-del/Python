# ============================================================
# 🐾 PET FOOD ADVENTURE: THE GOLDEN BOWL MISSION 🏆
# ============================================================

# Import necessary libraries
import pygame
import random


# ============================================================
# PART 1: GAME SETTINGS
# ============================================================

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

MOVEMENT_SPEED = 5

GAME_TIME = 45

STARTING_LIVES = 3

WINNING_SCORE = 25


# ============================================================
# PART 2: INITIALIZE PYGAME
# ============================================================

pygame.init()


# ============================================================
# PART 3: CREATE GAME WINDOW
# ============================================================

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption(
    "Pet Food Adventure - Golden Bowl Mission"
)


# ============================================================
# PART 4: LOAD BACKGROUND IMAGE
# ============================================================

background_image = pygame.transform.scale(
    pygame.image.load("Background Image For Pet Food.png"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)


# ============================================================
# PART 5: CREATE FONTS
# ============================================================

small_font = pygame.font.SysFont(
    "Arial",
    22
)

font = pygame.font.SysFont(
    "Arial",
    30
)

big_font = pygame.font.SysFont(
    "Arial",
    42
)


# ============================================================
# PART 6: CREATE SPRITE CLASS
# ============================================================

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call parent Sprite constructor
        super().__init__()

        # Create sprite image
        self.image = pygame.Surface(
            [width, height]
        )

        # Fill sprite with color
        self.image.fill(color)

        # Create rectangle for position
        self.rect = self.image.get_rect()


    # --------------------------------------------------------
    # Move sprite while keeping it inside the screen
    # --------------------------------------------------------

    def move(self, x_change, y_change):

        self.rect.x = max(
            min(
                self.rect.x + x_change,
                SCREEN_WIDTH - self.rect.width
            ),
            0
        )

        self.rect.y = max(
            min(
                self.rect.y + y_change,
                SCREEN_HEIGHT - self.rect.height
            ),
            0
        )


# ============================================================
# PART 7: CREATE PET CLASS
# ============================================================

class Pet(Sprite):

    def __init__(self):

        super().__init__(
            pygame.Color("saddlebrown"),
            45,
            45
        )

        # Pet eyes
        pygame.draw.circle(
            self.image,
            pygame.Color("white"),
            (14, 15),
            6
        )

        pygame.draw.circle(
            self.image,
            pygame.Color("white"),
            (31, 15),
            6
        )

        # Pupils
        pygame.draw.circle(
            self.image,
            pygame.Color("black"),
            (14, 15),
            2
        )

        pygame.draw.circle(
            self.image,
            pygame.Color("black"),
            (31, 15),
            2
        )

        # Nose
        pygame.draw.circle(
            self.image,
            pygame.Color("black"),
            (22, 27),
            4
        )

        # Ears
        pygame.draw.circle(
            self.image,
            pygame.Color("peru"),
            (4, 5),
            8
        )

        pygame.draw.circle(
            self.image,
            pygame.Color("peru"),
            (41, 5),
            8
        )


# ============================================================
# PART 8: CREATE NORMAL FOOD CLASS
# ============================================================

class Food(Sprite):

    def __init__(self):

        super().__init__(
            pygame.Color("orange"),
            25,
            25
        )

        # Draw food
        pygame.draw.circle(
            self.image,
            pygame.Color("darkorange"),
            (12, 12),
            10
        )


# ============================================================
# PART 9: CREATE GOLDEN FOOD CLASS
# ============================================================

class GoldenFood(Sprite):

    def __init__(self):

        super().__init__(
            pygame.Color("gold"),
            30,
            30
        )

        # Draw golden food
        pygame.draw.circle(
            self.image,
            pygame.Color("yellow"),
            (15, 15),
            12
        )

        pygame.draw.circle(
            self.image,
            pygame.Color("orange"),
            (15, 15),
            6
        )


# ============================================================
# PART 10: CREATE OBSTACLE CLASS
# ============================================================

class Obstacle(Sprite):

    def __init__(self):

        super().__init__(
            pygame.Color("red"),
            35,
            35
        )

        # Draw X
        pygame.draw.line(
            self.image,
            pygame.Color("black"),
            (5, 5),
            (30, 30),
            4
        )

        pygame.draw.line(
            self.image,
            pygame.Color("black"),
            (30, 5),
            (5, 30),
            4
        )


# ============================================================
# PART 11: RANDOM POSITION FUNCTION
# ============================================================

def random_position(sprite):

    sprite.rect.x = random.randint(
        60,
        SCREEN_WIDTH - sprite.rect.width
    )

    sprite.rect.y = random.randint(
        60,
        SCREEN_HEIGHT - sprite.rect.height
    )


# ============================================================
# PART 12: CREATE GAME FUNCTION
# ============================================================

def create_game():

    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    food_group = pygame.sprite.Group()

    golden_food_group = pygame.sprite.Group()

    obstacle_group = pygame.sprite.Group()


    # --------------------------------------------------------
    # CREATE PET
    # --------------------------------------------------------

    pet = Pet()

    pet.rect.x = 30
    pet.rect.y = 180

    all_sprites.add(pet)


    # --------------------------------------------------------
    # CREATE NORMAL FOOD
    # --------------------------------------------------------

    for i in range(5):

        food = Food()

        random_position(food)

        food_group.add(food)

        all_sprites.add(food)


    # --------------------------------------------------------
    # CREATE GOLDEN FOOD
    # --------------------------------------------------------

    for i in range(4):

        golden_food = GoldenFood()

        random_position(golden_food)

        golden_food_group.add(golden_food)

        all_sprites.add(golden_food)


    # --------------------------------------------------------
    # CREATE OBSTACLES
    # --------------------------------------------------------

    for i in range(3):

        obstacle = Obstacle()

        random_position(obstacle)

        obstacle_group.add(obstacle)

        all_sprites.add(obstacle)


    return (
        pet,
        all_sprites,
        food_group,
        golden_food_group,
        obstacle_group
    )


# ============================================================
# PART 13: START THE GAME
# ============================================================

(
    pet,
    all_sprites,
    food_group,
    golden_food_group,
    obstacle_group
) = create_game()


# ============================================================
# PART 14: GAME VARIABLES
# ============================================================

running = True

game_over = False

game_won = False

score = 0

lives = STARTING_LIVES

level = 1

start_time = pygame.time.get_ticks()

clock = pygame.time.Clock()


# ============================================================
# PART 15: MAIN GAME LOOP
# ============================================================

while running:


    # ========================================================
    # HANDLE EVENTS
    # ========================================================

    for event in pygame.event.get():

        # ----------------------------------------------------
        # WINDOW CLOSE BUTTON
        # ----------------------------------------------------

        if event.type == pygame.QUIT:

            running = False


        # ----------------------------------------------------
        # KEYBOARD EVENTS
        # ----------------------------------------------------

        if event.type == pygame.KEYDOWN:


            # =================================================
            # ESC = QUIT GAME
            # =================================================

            if event.key == pygame.K_ESCAPE:

                running = False


            # =================================================
            # R = RESTART GAME
            # =================================================

            if event.key == pygame.K_r:

                (
                    pet,
                    all_sprites,
                    food_group,
                    golden_food_group,
                    obstacle_group
                ) = create_game()

                score = 0

                lives = STARTING_LIVES

                level = 1

                game_over = False

                game_won = False

                start_time = pygame.time.get_ticks()


    # ========================================================
    # GAMEPLAY
    # ========================================================

    if not game_over and not game_won:


        # ----------------------------------------------------
        # GET KEYBOARD INPUT
        # ----------------------------------------------------

        keys = pygame.key.get_pressed()


        # Move left/right
        x_change = (
            keys[pygame.K_RIGHT] -
            keys[pygame.K_LEFT]
        ) * MOVEMENT_SPEED


        # Move up/down
        y_change = (
            keys[pygame.K_DOWN] -
            keys[pygame.K_UP]
        ) * MOVEMENT_SPEED


        # Move pet
        pet.move(
            x_change,
            y_change
        )


        # ====================================================
        # NORMAL FOOD COLLISION
        # ====================================================

        collected_food = pygame.sprite.spritecollide(
            pet,
            food_group,
            True
        )


        if collected_food:

            score += len(collected_food)


            # Remove from all sprites
            for food in collected_food:

                all_sprites.remove(food)


        # ====================================================
        # GOLDEN FOOD COLLISION
        # ====================================================

        collected_golden_food = pygame.sprite.spritecollide(
            pet,
            golden_food_group,
            True
        )


        if collected_golden_food:

            # Golden food gives 5 points
            score += 5 * len(collected_golden_food)


            for food in collected_golden_food:

                all_sprites.remove(food)


        # ====================================================
        # OBSTACLE COLLISION
        # ====================================================

        hit_obstacle = pygame.sprite.spritecollide(
            pet,
            obstacle_group,
            False
        )


        if hit_obstacle:

            # Lose one life
            lives -= 1


            # Move pet back
            pet.rect.x = 30
            pet.rect.y = 180


            # Move obstacle somewhere else
            for obstacle in hit_obstacle:

                random_position(obstacle)


        # ====================================================
        # LEVEL SYSTEM
        # ====================================================

        if score >= 20:

            level = 3

        elif score >= 10:

            level = 2

        else:

            level = 1


        # ====================================================
        # WIN CONDITION
        # ====================================================

        if score >= WINNING_SCORE:

            game_won = True


        # ====================================================
        # GAME OVER CONDITION
        # ====================================================

        if lives <= 0:

            game_over = True


    # ========================================================
    # TIMER SYSTEM
    # ========================================================

    elapsed_time = (
        pygame.time.get_ticks() -
        start_time
    ) // 1000


    remaining_time = GAME_TIME - elapsed_time


    # Time runs out
    if remaining_time <= 0 and not game_won:

        remaining_time = 0

        game_over = True


    # ========================================================
    # DRAW BACKGROUND
    # ========================================================

    screen.blit(
        background_image,
        (0, 0)
    )


    # ========================================================
    # DRAW ALL SPRITES
    # ========================================================

    all_sprites.draw(screen)


    # ========================================================
    # TOP INFORMATION PANEL
    # ========================================================

    pygame.draw.rect(
        screen,
        pygame.Color("white"),
        (5, 5, 490, 35)
    )


    # ========================================================
    # SCORE
    # ========================================================

    score_text = small_font.render(
        "Score: " + str(score),
        True,
        pygame.Color("black")
    )

    screen.blit(
        score_text,
        (12, 10)
    )


    # ========================================================
    # LIVES
    # ========================================================

    lives_text = small_font.render(
        "Lives: " + str(lives),
        True,
        pygame.Color("red")
    )

    screen.blit(
        lives_text,
        (120, 10)
    )


    # ========================================================
    # LEVEL
    # ========================================================

    level_text = small_font.render(
        "Level: " + str(level),
        True,
        pygame.Color("blue")
    )

    screen.blit(
        level_text,
        (230, 10)
    )


    # ========================================================
    # TIMER
    # ========================================================

    time_text = small_font.render(
        "Time: " + str(remaining_time),
        True,
        pygame.Color("purple")
    )

    screen.blit(
        time_text,
        (350, 10)
    )


    # ========================================================
    # GAME INSTRUCTIONS
    # ========================================================

    help_text = small_font.render(
        "Orange +1 | Gold +5 | Red X = Danger",
        True,
        pygame.Color("black")
    )

    screen.blit(
        help_text,
        (55, 365)
    )


    # ========================================================
    # WIN SCREEN
    # ========================================================

    if game_won:


        # White transparent overlay
        overlay = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        overlay.set_alpha(210)

        overlay.fill(
            pygame.Color("white")
        )

        screen.blit(
            overlay,
            (0, 0)
        )


        # Main message
        title = big_font.render(
            "MISSION COMPLETE!",
            True,
            pygame.Color("green")
        )


        title_x = (
            SCREEN_WIDTH -
            title.get_width()
        ) // 2


        screen.blit(
            title,
            (title_x, 90)
        )


        # Second message
        message = font.render(
            "Golden Bowl Found!",
            True,
            pygame.Color("black")
        )


        message_x = (
            SCREEN_WIDTH -
            message.get_width()
        ) // 2


        screen.blit(
            message,
            (message_x, 155)
        )


        # Score
        final_score = font.render(
            "Final Score: " + str(score),
            True,
            pygame.Color("blue")
        )


        final_x = (
            SCREEN_WIDTH -
            final_score.get_width()
        ) // 2


        screen.blit(
            final_score,
            (final_x, 205)
        )


        # Restart
        restart = font.render(
            "Press R to Play Again",
            True,
            pygame.Color("purple")
        )


        restart_x = (
            SCREEN_WIDTH -
            restart.get_width()
        ) // 2


        screen.blit(
            restart,
            (restart_x, 265)
        )


        # Quit
        quit_text = small_font.render(
            "Press ESC to Quit",
            True,
            pygame.Color("black")
        )


        quit_x = (
            SCREEN_WIDTH -
            quit_text.get_width()
        ) // 2


        screen.blit(
            quit_text,
            (quit_x, 310)
        )


    # ========================================================
    # GAME OVER SCREEN
    # ========================================================

    if game_over:


        # Transparent overlay
        overlay = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        overlay.set_alpha(210)

        overlay.fill(
            pygame.Color("white")
        )

        screen.blit(
            overlay,
            (0, 0)
        )


        # Game over title
        title = big_font.render(
            "GAME OVER!",
            True,
            pygame.Color("red")
        )


        title_x = (
            SCREEN_WIDTH -
            title.get_width()
        ) // 2


        screen.blit(
            title,
            (title_x, 90)
        )


        # Message
        message = font.render(
            "The pet needs more food!",
            True,
            pygame.Color("black")
        )


        message_x = (
            SCREEN_WIDTH -
            message.get_width()
        ) // 2


        screen.blit(
            message,
            (message_x, 155)
        )


        # Score
        final_score = font.render(
            "Your Score: " + str(score),
            True,
            pygame.Color("blue")
        )


        final_x = (
            SCREEN_WIDTH -
            final_score.get_width()
        ) // 2


        screen.blit(
            final_score,
            (final_x, 205)
        )


        # Restart
        restart = font.render(
            "Press R to Try Again",
            True,
            pygame.Color("purple")
        )


        restart_x = (
            SCREEN_WIDTH -
            restart.get_width()
        ) // 2


        screen.blit(
            restart,
            (restart_x, 265)
        )


        # Quit
        quit_text = small_font.render(
            "Press ESC to Quit",
            True,
            pygame.Color("black")
        )


        quit_x = (
            SCREEN_WIDTH -
            quit_text.get_width()
        ) // 2


        screen.blit(
            quit_text,
            (quit_x, 310)
        )


    # ========================================================
    # REFRESH DISPLAY
    # ========================================================

    pygame.display.flip()


    # ========================================================
    # CONTROL FRAME RATE
    # ========================================================

    clock.tick(60)


# ============================================================
# CLOSE PYGAME
# ============================================================

pygame.quit()