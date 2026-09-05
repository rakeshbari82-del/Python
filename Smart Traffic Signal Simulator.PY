# 🚨 SMART CITY - EMERGENCY TRAFFIC CONTROL
# Smart Traffic Signal Simulator

import pygame
import random

# Initialize Pygame
pygame.init()


# -------------------------------------------------
# CUSTOM EVENTS
# -------------------------------------------------

CAR_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2


# -------------------------------------------------
# COLOURS
# -------------------------------------------------

ROAD = pygame.Color("darkgray")
GRASS = pygame.Color("darkgreen")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")
CYAN = pygame.Color("cyan")
PURPLE = pygame.Color("purple")


# -------------------------------------------------
# CAR SPRITE CLASS
# -------------------------------------------------

class Car(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call parent Sprite constructor
        super().__init__()

        # Create the car image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Create the car rectangle
        self.rect = self.image.get_rect()

        # Horizontal velocity
        self.velocity = [4, 0]

        # Number of times boundary was reached
        self.sensor_count = 0


    # -------------------------------------------------
    # UPDATE CAR
    # -------------------------------------------------

    def update(self):

        # Move the car
        self.rect.move_ip(self.velocity)

        sensor_triggered = False

        # Check road boundaries
        if self.rect.left <= 20 or self.rect.right >= 580:

            # Reverse direction
            self.velocity[0] = -self.velocity[0]

            sensor_triggered = True

            # Increase sensor count
            self.sensor_count += 1


        # Send custom events
        if sensor_triggered:

            pygame.event.post(
                pygame.event.Event(CAR_COLOR_CHANGE_EVENT)
            )

            pygame.event.post(
                pygame.event.Event(SIGNAL_CHANGE_EVENT)
            )


    # -------------------------------------------------
    # CHANGE CAR COLOUR
    # -------------------------------------------------

    def change_color(self):

        new_color = random.choice(
            [WHITE, YELLOW, BLUE, ORANGE, CYAN]
        )

        self.image.fill(new_color)


# -------------------------------------------------
# TRAFFIC SIGNAL FUNCTION
# -------------------------------------------------

def change_signal():

    global signal_color

    if signal_color == RED:
        signal_color = GREEN
    else:
        signal_color = RED


# -------------------------------------------------
# CREATE SPRITE GROUP
# -------------------------------------------------

all_sprites = pygame.sprite.Group()


# -------------------------------------------------
# CREATE EMERGENCY CAR
# -------------------------------------------------

car = Car(WHITE, 80, 40)

car.rect.x = 60
car.rect.y = 280

all_sprites.add(car)


# -------------------------------------------------
# CREATE SCREEN
# -------------------------------------------------

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption(
    "Smart City - Emergency Traffic Control"
)


# -------------------------------------------------
# STARTING TRAFFIC SIGNAL
# -------------------------------------------------

signal_color = RED


# -------------------------------------------------
# FONT
# -------------------------------------------------

font = pygame.font.Font(None, 28)

large_font = pygame.font.Font(None, 45)


# -------------------------------------------------
# CLOCK
# -------------------------------------------------

clock = pygame.time.Clock()


# -------------------------------------------------
# GAME LOOP
# -------------------------------------------------

running = True

while running:

    # ---------------------------------------------
    # HANDLE EVENTS
    # ---------------------------------------------

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:

            running = False


        # Car colour event
        elif event.type == CAR_COLOR_CHANGE_EVENT:

            car.change_color()


        # Traffic signal event
        elif event.type == SIGNAL_CHANGE_EVENT:

            change_signal()


    # ---------------------------------------------
    # UPDATE SPRITES
    # ---------------------------------------------

    all_sprites.update()


    # ---------------------------------------------
    # DRAW BACKGROUND
    # ---------------------------------------------

    screen.fill(GRASS)


    # ---------------------------------------------
    # DRAW ROAD
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        ROAD,
        (0, 220, 600, 160)
    )


    # ---------------------------------------------
    # ROAD BORDERS
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        WHITE,
        (0, 220, 600, 5)
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (0, 375, 600, 5)
    )


    # ---------------------------------------------
    # ROAD DIVIDER
    # ---------------------------------------------

    for x in range(0, 600, 80):

        pygame.draw.rect(
            screen,
            YELLOW,
            (x, 295, 45, 6)
        )


    # ---------------------------------------------
    # SMART CITY BUILDINGS
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        BLUE,
        (30, 80, 70, 120)
    )

    pygame.draw.rect(
        screen,
        PURPLE,
        (130, 100, 80, 100)
    )

    pygame.draw.rect(
        screen,
        ORANGE,
        (470, 90, 80, 110)
    )


    # Building windows
    for wx in [45, 65, 145, 170, 490, 515]:

        for wy in [115, 145, 175]:

            pygame.draw.rect(
                screen,
                YELLOW,
                (wx, wy, 10, 12)
            )


    # ---------------------------------------------
    # TRAFFIC SIGNAL BOX
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        BLACK,
        (270, 35, 60, 150)
    )


    # Traffic signal circles

    pygame.draw.circle(
        screen,
        RED,
        (300, 65),
        18
    )

    pygame.draw.circle(
        screen,
        YELLOW,
        (300, 110),
        18
    )

    pygame.draw.circle(
        screen,
        GREEN,
        (300, 155),
        18
    )


    # ---------------------------------------------
    # ACTIVE SIGNAL
    # ---------------------------------------------

    if signal_color == RED:

        pygame.draw.circle(
            screen,
            RED,
            (300, 65),
            18
        )

    else:

        pygame.draw.circle(
            screen,
            GREEN,
            (300, 155),
            18
        )


    # ---------------------------------------------
    # SMART SENSOR BOXES
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        BLACK,
        (10, 250, 12, 70)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (578, 250, 12, 70)
    )


    # Sensor lights

    pygame.draw.circle(
        screen,
        CYAN,
        (16, 265),
        5
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (16, 285),
        5
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (584, 265),
        5
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (584, 285),
        5
    )


    # ---------------------------------------------
    # DRAW EMERGENCY CAR
    # ---------------------------------------------

    all_sprites.draw(screen)


    # ---------------------------------------------
    # CAR WINDOWS
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        CYAN,
        (
            car.rect.x + 15,
            car.rect.y + 7,
            20,
            15
        )
    )

    pygame.draw.rect(
        screen,
        CYAN,
        (
            car.rect.x + 45,
            car.rect.y + 7,
            20,
            15
        )
    )


    # ---------------------------------------------
    # CAR LIGHT
    # ---------------------------------------------

    pygame.draw.circle(
        screen,
        RED,
        (
            car.rect.x + 40,
            car.rect.y
        ),
        5
    )


    # ---------------------------------------------
    # DASHBOARD
    # ---------------------------------------------

    pygame.draw.rect(
        screen,
        BLACK,
        (10, 10, 210, 55)
    )


    # Signal text

    if signal_color == RED:

        signal_text = "SIGNAL: RED"

    else:

        signal_text = "SIGNAL: GREEN"


    text1 = font.render(
        signal_text,
        True,
        WHITE
    )

    screen.blit(
        text1,
        (20, 18)
    )


    # Sensor counter

    text2 = font.render(
        "Sensors: " + str(car.sensor_count),
        True,
        WHITE
    )

    screen.blit(
        text2,
        (20, 42)
    )


    # ---------------------------------------------
    # TITLE
    # ---------------------------------------------

    title = large_font.render(
        "SMART CITY CONTROL",
        True,
        WHITE
    )

    screen.blit(
        title,
        (170, 5)
    )


    # ---------------------------------------------
    # TRAFFIC STATUS
    # ---------------------------------------------

    if signal_color == RED:

        status = "STOP"

    else:

        status = "GO"


    status_text = font.render(
        "Traffic Status: " + status,
        True,
        WHITE
    )

    screen.blit(
        status_text,
        (430, 20)
    )


    # ---------------------------------------------
    # UPDATE SCREEN
    # ---------------------------------------------

    pygame.display.flip()


    # ---------------------------------------------
    # FRAME RATE
    # ---------------------------------------------

    clock.tick(60)


# -------------------------------------------------
# QUIT PYGAME
# -------------------------------------------------

pygame.quit()