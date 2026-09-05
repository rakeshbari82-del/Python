# ============================================================
# CODEMENTOR
# A Digital Teacher's Day Surprise
# ============================================================

import pygame
import random
import math

pygame.init()


# ============================================================
# SCREEN
# ============================================================

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(
    "CodeMentor - A Teacher's Day Surprise"
)

clock = pygame.time.Clock()


# ============================================================
# COLORS
# ============================================================

BLACK = (8, 12, 30)
NAVY = (15, 25, 55)
BLUE = (40, 120, 255)
CYAN = (50, 220, 255)
PURPLE = (150, 80, 255)
PINK = (255, 100, 180)
WHITE = (245, 245, 255)
YELLOW = (255, 220, 70)
GREEN = (70, 230, 150)
ORANGE = (255, 150, 60)
GRAY = (120, 130, 160)
RED = (255, 80, 90)


# ============================================================
# FONTS
# ============================================================

small_font = pygame.font.Font(None, 25)
font = pygame.font.Font(None, 32)
medium_font = pygame.font.Font(None, 42)
big_font = pygame.font.Font(None, 58)
huge_font = pygame.font.Font(None, 76)


# ============================================================
# CUSTOM EVENTS
# ============================================================

STAR_EVENT = pygame.USEREVENT + 1
MESSAGE_EVENT = pygame.USEREVENT + 2

pygame.time.set_timer(STAR_EVENT, 700)


# ============================================================
# HELPER FUNCTION
# ============================================================

def draw_text(text, font_object, color, x, y, center=False):

    image = font_object.render(
        text,
        True,
        color
    )

    if center:

        rect = image.get_rect(
            center=(x, y)
        )

    else:

        rect = image.get_rect(
            topleft=(x, y)
        )

    screen.blit(image, rect)


# ============================================================
# STAR SPRITE
# ============================================================

class Star(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        size = random.randint(2, 5)

        self.image = pygame.Surface(
            (size * 2, size * 2),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            self.image,
            random.choice(
                [WHITE, CYAN, YELLOW, PINK]
            ),
            (size, size),
            size
        )

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(
            0,
            WIDTH
        )

        self.rect.y = random.randint(
            0,
            HEIGHT
        )

        self.speed = random.uniform(
            0.3,
            1.2
        )


    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:

            self.rect.bottom = 0

            self.rect.x = random.randint(
                0,
                WIDTH
            )


# ============================================================
# FLOATING PARTICLE
# ============================================================

class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface(
            (8, 8),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            self.image,
            random.choice(
                [CYAN, PURPLE, PINK, YELLOW]
            ),
            (4, 4),
            4
        )

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.speed_x = random.uniform(
            -2,
            2
        )

        self.speed_y = random.uniform(
            -2.5,
            -0.5
        )

        self.life = 60


    def update(self):

        self.rect.x += self.speed_x

        self.rect.y += self.speed_y

        self.life -= 1

        if self.life <= 0:

            self.kill()


# ============================================================
# BOOK CLASS
# ============================================================

class Book(pygame.sprite.Sprite):

    def __init__(self, x, y, color):

        super().__init__()

        self.image = pygame.Surface(
            (90, 28),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            self.image,
            color,
            (0, 0, 90, 28),
            border_radius=5
        )

        pygame.draw.line(
            self.image,
            WHITE,
            (10, 7),
            (80, 7),
            2
        )

        pygame.draw.line(
            self.image,
            WHITE,
            (10, 14),
            (65, 14),
            2
        )

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.original_y = y

        self.angle = random.uniform(
            0,
            6.28
        )


    def update(self):

        self.angle += 0.02

        self.rect.y = (
            self.original_y
            + math.sin(self.angle) * 8
        )


# ============================================================
# SPRITE GROUPS
# ============================================================

stars = pygame.sprite.Group()

particles = pygame.sprite.Group()

books = pygame.sprite.Group()


# ============================================================
# CREATE STARS
# ============================================================

for i in range(70):

    stars.add(
        Star()
    )


# ============================================================
# CREATE FLOATING BOOKS
# ============================================================

books.add(
    Book(130, 400, BLUE)
)

books.add(
    Book(770, 420, PURPLE)
)

books.add(
    Book(150, 470, GREEN)
)

books.add(
    Book(750, 500, ORANGE)
)


# ============================================================
# BUTTON CLASS
# ============================================================

class Button:

    def __init__(
        self,
        x,
        y,
        width,
        height,
        text
    ):

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.text = text

        self.hover = False


    def draw(self):

        mouse_pos = pygame.mouse.get_pos()

        self.hover = self.rect.collidepoint(
            mouse_pos
        )

        if self.hover:

            color = CYAN

        else:

            color = BLUE


        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            2,
            border_radius=10
        )

        draw_text(
            self.text,
            font,
            BLACK,
            self.rect.centerx,
            self.rect.centery,
            True
        )


# ============================================================
# BUTTONS
# ============================================================

learn_button = Button(
    210,
    485,
    150,
    50,
    "MY JOURNEY"
)

message_button = Button(
    375,
    485,
    150,
    50,
    "MESSAGE"
)

surprise_button = Button(
    540,
    485,
    150,
    50,
    "SURPRISE"
)


# ============================================================
# GAME VARIABLES
# ============================================================

running = True

# Page meanings:
#
# 0 = Welcome
# 1 = My Journey
# 2 = Message
# 3 = Final Surprise

page = 0

show_surprise = False

click_count = 0

message_index = 0


# ============================================================
# MAIN GAME LOOP
# ============================================================

while running:


    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():


        # ----------------------------------------------------
        # CLOSE WINDOW
        # ----------------------------------------------------

        if event.type == pygame.QUIT:

            running = False


        # ----------------------------------------------------
        # NEW STAR
        # ----------------------------------------------------

        elif event.type == STAR_EVENT:

            stars.add(
                Star()
            )


        # ----------------------------------------------------
        # MOUSE CLICK
        # ----------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                click_count += 1


                # ============================================
                # MY JOURNEY
                # ============================================

                if learn_button.rect.collidepoint(
                    event.pos
                ):

                    page = 1

                    show_surprise = False


                # ============================================
                # MESSAGE
                # ============================================

                elif message_button.rect.collidepoint(
                    event.pos
                ):

                    page = 2

                    show_surprise = False


                # ============================================
                # SURPRISE
                # ============================================

                elif surprise_button.rect.collidepoint(
                    event.pos
                ):

                    page = 3

                    show_surprise = True


                    # Celebration particles

                    for i in range(100):

                        particles.add(
                            Particle(
                                WIDTH // 2,
                                HEIGHT // 2
                            )
                        )


    # ========================================================
    # UPDATE
    # ========================================================

    stars.update()

    books.update()

    particles.update()


    # ========================================================
    # BACKGROUND
    # ========================================================

    screen.fill(
        BLACK
    )


    # Large background circles

    pygame.draw.circle(
        screen,
        (20, 30, 70),
        (150, 150),
        130
    )

    pygame.draw.circle(
        screen,
        (25, 20, 70),
        (760, 170),
        150
    )


    # Stars

    stars.draw(
        screen
    )


    # ========================================================
    # HEADER
    # ========================================================

    draw_text(
        "CODEMENTOR",
        huge_font,
        CYAN,
        WIDTH // 2,
        55,
        True
    )

    draw_text(
        "A LITTLE GIFT MADE WITH CODE",
        small_font,
        WHITE,
        WIDTH // 2,
        95,
        True
    )


    # ========================================================
    # COMPUTER BODY
    # ========================================================

    computer = pygame.Rect(
        240,
        120,
        420,
        300
    )

    pygame.draw.rect(
        screen,
        NAVY,
        computer,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        CYAN,
        computer,
        3,
        border_radius=15
    )


    # ========================================================
    # COMPUTER MONITOR
    # ========================================================

    monitor = pygame.Rect(
        260,
        145,
        380,
        245
    )

    pygame.draw.rect(
        screen,
        BLACK,
        monitor,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        BLUE,
        monitor,
        2,
        border_radius=8
    )


    # ========================================================
    # PAGE 0 - WELCOME
    # ========================================================

    if page == 0:

        draw_text(
            "HELLO, CODE MENTOR!",
            medium_font,
            YELLOW,
            450,
            190,
            True
        )

        draw_text(
            "This program was created",
            font,
            WHITE,
            450,
            235,
            True
        )

        draw_text(
            "especially for you.",
            font,
            CYAN,
            450,
            270,
            True
        )

        draw_text(
            "Thank you for teaching me to code!",
            font,
            PINK,
            450,
            305,
            True
        )


    # ========================================================
    # PAGE 1 - MY JOURNEY
    # ========================================================

    elif page == 1:

        draw_text(
            "MY CODING JOURNEY",
            medium_font,
            YELLOW,
            450,
            185,
            True
        )

        draw_text(
            "You taught me how to turn",
            font,
            WHITE,
            450,
            225,
            True
        )

        draw_text(
            "ideas into programs.",
            font,
            CYAN,
            450,
            260,
            True
        )

        draw_text(
            "Python  |  Pygame  |  Logic  |  Creativity",
            small_font,
            GREEN,
            450,
            300,
            True
        )

        draw_text(
            "Every lesson became another step forward.",
            small_font,
            WHITE,
            450,
            330,
            True
        )


    # ========================================================
    # PAGE 2 - MESSAGE
    # ========================================================

    elif page == 2:

        draw_text(
            "A MESSAGE FOR YOU",
            medium_font,
            YELLOW,
            450,
            170,
            True
        )

        draw_text(
            "Dear Preethi Ma'am,",
            font,
            PINK,
            450,
            205,
            True
        )

        draw_text(
            "Sometimes a teacher teaches a subject,",
            small_font,
            WHITE,
            450,
            240,
            True
        )

        draw_text(
            "but sometimes a teacher inspires a student",
            small_font,
            WHITE,
            450,
            265,
            True
        )

        draw_text(
            "to believe in themselves.",
            small_font,
            CYAN,
            450,
            290,
            True
        )

        draw_text(
            "Every lesson becomes another step",
            small_font,
            WHITE,
            450,
            320,
            True
        )

        draw_text(
            "in my coding journey.",
            small_font,
            WHITE,
            450,
            345,
            True
        )

        draw_text(
            "Thank you for your patience and guidance.",
            small_font,
            GREEN,
            450,
            375,
            True
        )


    # ========================================================
    # PAGE 3 - FINAL SURPRISE
    # ========================================================

    elif page == 3:

        draw_text(
            "HAPPY TEACHER'S DAY!",
            medium_font,
            YELLOW,
            450,
            170,
            True
        )

        draw_text(
            "Dear Preethi Ma'am,",
            font,
            PINK,
            450,
            205,
            True
        )

        draw_text(
            "You are my STAR",
            medium_font,
            CYAN,
            450,
            245,
            True
        )

        draw_text(
            "You helped me turn my ideas into code,",
            small_font,
            WHITE,
            450,
            285,
            True
        )

        draw_text(
            "and my code into confidence.",
            small_font,
            GREEN,
            450,
            315,
            True
        )

        draw_text(
            "Thank you for believing in my learning.",
            small_font,
            WHITE,
            450,
            350,
            True
        )

        draw_text(
            "HAPPY TEACHER'S DAY!",
            font,
            YELLOW,
            450,
            380,
            True
        )


    # ========================================================
    # COMPUTER STAND
    # ========================================================

    pygame.draw.rect(
        screen,
        NAVY,
        (420, 420, 60, 25)
    )

    pygame.draw.rect(
        screen,
        NAVY,
        (360, 445, 180, 15),
        border_radius=5
    )


    # ========================================================
    # FLOATING BOOKS
    # ========================================================

    books.draw(
        screen
    )


    # ========================================================
    # BUTTONS
    # ========================================================

    learn_button.draw()

    message_button.draw()

    surprise_button.draw()


    # ========================================================
    # BOTTOM MESSAGE
    # ========================================================

    if page == 0:

        draw_text(
            "Start the journey...",
            small_font,
            GRAY,
            WIDTH // 2,
            570,
            True
        )


    elif page == 1:

        draw_text(
            "Now discover the MESSAGE...",
            small_font,
            YELLOW,
            WIDTH // 2,
            570,
            True
        )


    elif page == 2:

        draw_text(
            "One more click for your surprise...",
            small_font,
            CYAN,
            WIDTH // 2,
            570,
            True
        )


    else:

        draw_text(
            "Made with code, creativity and gratitude",
            small_font,
            GRAY,
            WIDTH // 2,
            570,
            True
        )


    # ========================================================
    # CELEBRATION PARTICLES
    # ========================================================

    particles.draw(
        screen
    )


    # ========================================================
    # DISPLAY
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


# ============================================================
# CLOSE
# ============================================================


pygame.quit()
