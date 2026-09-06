# ============================================================
# 🐯 WILD QUEST - Wildlife Explorer
# An Interactive Wildlife Information & Quiz Game
# ============================================================

# Import necessary libraries
import pygame
import random

# ------------------------------------------------------------
# PART 1: Initialize Pygame
# ------------------------------------------------------------

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Create display window
display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Window title
pygame.display.set_caption("🐯 WILD QUEST - Wildlife Explorer")


# ------------------------------------------------------------
# PART 2: Load Images
# ------------------------------------------------------------

# Load background image
background_image = pygame.transform.scale(
    pygame.image.load("Wildlife Background Image.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load tiger image
wildlife_image = pygame.transform.scale(
    pygame.image.load("Tiger.png").convert_alpha(),
    (250, 250)
)

# Position tiger in the center
wildlife_rect = wildlife_image.get_rect(
    center=(SCREEN_WIDTH // 2, 300)
)


# ------------------------------------------------------------
# PART 3: Create Fonts
# ------------------------------------------------------------

title_font = pygame.font.Font(None, 52)
heading_font = pygame.font.Font(None, 40)
fact_font = pygame.font.Font(None, 28)
button_font = pygame.font.Font(None, 28)
small_font = pygame.font.Font(None, 23)
score_font = pygame.font.Font(None, 32)


# ------------------------------------------------------------
# PART 4: Wildlife Facts
# ------------------------------------------------------------

facts = [
    "Tigers are powerful wild cats.",
    "Tigers are excellent swimmers.",
    "Every tiger has a unique stripe pattern.",
    "Tigers mainly hunt at night.",
    "A tiger's stripes help it blend into nature.",
    "Tigers are the largest living cat species.",
    "Tigers can live in forests, grasslands and wetlands."
]

current_fact = 0


# ------------------------------------------------------------
# PART 5: Quiz Questions
# ------------------------------------------------------------

questions = [
    {
        "question": "Which animal is known for unique stripe patterns?",
        "options": ["Tiger", "Elephant", "Giraffe"],
        "answer": 0
    },

    {
        "question": "Are tigers good swimmers?",
        "options": ["Yes", "No", "Never"],
        "answer": 0
    },

    {
        "question": "When do tigers mainly hunt?",
        "options": ["At night", "At noon", "Only morning"],
        "answer": 0
    },

    {
        "question": "What helps a tiger camouflage itself?",
        "options": ["Its stripes", "Its wings", "Its horns"],
        "answer": 0
    }
]

current_question = 0
score = 0

# Quiz state
quiz_mode = False
answer_message = ""
message_timer = 0


# ------------------------------------------------------------
# PART 6: Buttons
# ------------------------------------------------------------

next_button = pygame.Rect(
    235, 505, 230, 50
)

quiz_button = pygame.Rect(
    480, 505, 170, 50
)

back_button = pygame.Rect(
    20, 505, 170, 50
)


# Quiz answer buttons
answer_buttons = [
    pygame.Rect(80, 390, 160, 50),
    pygame.Rect(270, 390, 160, 50),
    pygame.Rect(460, 390, 160, 50)
]


# ------------------------------------------------------------
# PART 7: Animated Particles
# ------------------------------------------------------------

particles = []

for i in range(35):
    particles.append({
        "x": random.randint(0, SCREEN_WIDTH),
        "y": random.randint(0, SCREEN_HEIGHT),
        "speed": random.uniform(0.3, 1.2),
        "size": random.randint(2, 5)
    })


# ------------------------------------------------------------
# PART 8: Helper Functions
# ------------------------------------------------------------

def draw_text(text, font, position, color):
    """
    Draw text on the screen.
    """
    text_surface = font.render(
        text,
        True,
        color
    )

    display_surface.blit(
        text_surface,
        position
    )


def draw_center_text(text, font, y, color):
    """
    Draw centered text.
    """

    text_surface = font.render(
        text,
        True,
        color
    )

    text_rect = text_surface.get_rect(
        center=(SCREEN_WIDTH // 2, y)
    )

    display_surface.blit(
        text_surface,
        text_rect
    )


def draw_button(rect, text):
    """
    Draw a button.
    """

    mouse_position = pygame.mouse.get_pos()

    # Change appearance when mouse is over button
    if rect.collidepoint(mouse_position):
        button_color = pygame.Color("orange")
    else:
        button_color = pygame.Color("darkgreen")

    pygame.draw.rect(
        display_surface,
        button_color,
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        display_surface,
        pygame.Color("white"),
        rect,
        2,
        border_radius=12
    )

    text_surface = button_font.render(
        text,
        True,
        pygame.Color("white")
    )

    text_rect = text_surface.get_rect(
        center=rect.center
    )

    display_surface.blit(
        text_surface,
        text_rect
    )


def draw_particles():
    """
    Draw and animate jungle particles.
    """

    for particle in particles:

        pygame.draw.circle(
            display_surface,
            pygame.Color("lightgreen"),
            (
                int(particle["x"]),
                int(particle["y"])
            ),
            particle["size"]
        )

        particle["y"] += particle["speed"]

        # Move particle back to top
        if particle["y"] > SCREEN_HEIGHT:
            particle["y"] = 0
            particle["x"] = random.randint(
                0,
                SCREEN_WIDTH
            )


# ------------------------------------------------------------
# PART 9: Main Game Loop
# ------------------------------------------------------------

def game_loop():

    global current_fact
    global quiz_mode
    global current_question
    global score
    global answer_message
    global message_timer

    # Clock
    clock = pygame.time.Clock()

    running = True

    while running:

        # ----------------------------------------------------
        # EVENT HANDLING
        # ----------------------------------------------------

        for event in pygame.event.get():

            # Window close button
            if event.type == pygame.QUIT:
                running = False

            # Keyboard controls
            if event.type == pygame.KEYDOWN:

                # ESCAPE = QUIT
                if event.key == pygame.K_ESCAPE:
                    running = False

                # SPACE = Next fact
                if event.key == pygame.K_SPACE:

                    if not quiz_mode:

                        current_fact += 1

                        if current_fact >= len(facts):
                            current_fact = 0

                # Q = Start quiz
                if event.key == pygame.K_q:
                    quiz_mode = True
                    current_question = 0
                    score = 0
                    answer_message = ""

                # B = Back to information
                if event.key == pygame.K_b:
                    quiz_mode = False
                    answer_message = ""

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_position = event.pos

                # --------------------------------------------
                # NORMAL WILDLIFE INFORMATION MODE
                # --------------------------------------------

                if not quiz_mode:

                    # Next Fact button
                    if next_button.collidepoint(mouse_position):

                        current_fact += 1

                        if current_fact >= len(facts):
                            current_fact = 0

                    # Quiz button
                    if quiz_button.collidepoint(mouse_position):

                        quiz_mode = True
                        current_question = 0
                        score = 0
                        answer_message = ""

                # --------------------------------------------
                # QUIZ MODE
                # --------------------------------------------

                else:

                    # Answer buttons
                    for index, button in enumerate(
                        answer_buttons
                    ):

                        if button.collidepoint(
                            mouse_position
                        ):

                            correct_answer = questions[
                                current_question
                            ]["answer"]

                            if index == correct_answer:

                                score += 1

                                answer_message = (
                                    "CORRECT! 🎉 +1 point"
                                )

                            else:

                                answer_message = (
                                    "Oops! Try the next one! 🐾"
                                )

                            message_timer = 60

                            # Move to next question
                            current_question += 1

                            # Restart quiz after last question
                            if current_question >= len(
                                questions
                            ):

                                current_question = 0

                    # Back button
                    if back_button.collidepoint(
                        mouse_position
                    ):

                        quiz_mode = False
                        answer_message = ""


        # ----------------------------------------------------
        # DRAW BACKGROUND
        # ----------------------------------------------------

        display_surface.blit(
            background_image,
            (0, 0)
        )


        # Dark transparent overlay
        overlay = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 55)
        )

        display_surface.blit(
            overlay,
            (0, 0)
        )


        # Animated particles
        draw_particles()


        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        draw_center_text(
            "🐯 WILD QUEST",
            title_font,
            35,
            pygame.Color("white")
        )


        # ----------------------------------------------------
        # WILDLIFE INFORMATION MODE
        # ----------------------------------------------------

        if not quiz_mode:

            # Subtitle
            draw_center_text(
                "Wildlife Explorer: TIGER",
                heading_font,
                80,
                pygame.Color("yellow")
            )

            # Tiger image
            display_surface.blit(
                wildlife_image,
                wildlife_rect
            )

            # Fact box
            fact_box = pygame.Rect(
                70,
                370,
                560,
                90
            )

            pygame.draw.rect(
                display_surface,
                pygame.Color("white"),
                fact_box,
                border_radius=15
            )

            pygame.draw.rect(
                display_surface,
                pygame.Color("darkgreen"),
                fact_box,
                3,
                border_radius=15
            )

            # Fact number
            draw_center_text(
                "FACT " + str(current_fact + 1),
                small_font,
                390,
                pygame.Color("darkgreen")
            )

            # Current fact
            draw_center_text(
                facts[current_fact],
                fact_font,
                425,
                pygame.Color("black")
            )


            # Buttons
            draw_button(
                next_button,
                "NEXT FACT ➜"
            )

            draw_button(
                quiz_button,
                "QUIZ 🎯"
            )


            # Controls
            draw_text(
                "SPACE = Next Fact",
                small_font,
                (20, 565),
                pygame.Color("white")
            )

            draw_text(
                "Q = Quiz",
                small_font,
                (280, 565),
                pygame.Color("white")
            )

            draw_text(
                "ESC = Quit",
                small_font,
                (500, 565),
                pygame.Color("white")
            )


        # ----------------------------------------------------
        # QUIZ MODE
        # ----------------------------------------------------

        else:

            draw_center_text(
                "🐾 WILDLIFE QUIZ",
                heading_font,
                85,
                pygame.Color("yellow")
            )

            # Score
            draw_text(
                "Score: " + str(score),
                score_font,
                (25, 110),
                pygame.Color("white")
            )

            # Question
            question = questions[
                current_question
            ]["question"]

            question_box = pygame.Rect(
                40,
                145,
                620,
                180
            )

            pygame.draw.rect(
                display_surface,
                pygame.Color("white"),
                question_box,
                border_radius=15
            )

            pygame.draw.rect(
                display_surface,
                pygame.Color("darkgreen"),
                question_box,
                3,
                border_radius=15
            )

            draw_center_text(
                "Question " +
                str(current_question + 1),
                small_font,
                170,
                pygame.Color("darkgreen")
            )

            draw_center_text(
                question,
                fact_font,
                230,
                pygame.Color("black")
            )

            draw_center_text(
                "Choose the correct answer:",
                small_font,
                280,
                pygame.Color("black")
            )


            # Answer buttons
            options = questions[
                current_question
            ]["options"]

            for index, button in enumerate(
                answer_buttons
            ):

                draw_button(
                    button,
                    options[index]
                )


            # Answer message
            if answer_message:

                draw_center_text(
                    answer_message,
                    fact_font,
                    470,
                    pygame.Color("yellow")
                )


            # Back button
            draw_button(
                back_button,
                "← BACK"
            )

            draw_text(
                "ESC = Quit",
                small_font,
                (540, 565),
                pygame.Color("white")
            )


        # ----------------------------------------------------
        # UPDATE DISPLAY
        # ----------------------------------------------------

        pygame.display.flip()


        # Message timer
        if message_timer > 0:
            message_timer -= 1


        # 30 FPS
        clock.tick(30)


    # --------------------------------------------------------
    # QUIT PYGAME
    # --------------------------------------------------------

    pygame.quit()


# ------------------------------------------------------------
# PART 10: Run the Application
# ------------------------------------------------------------

if __name__ == "__main__":
    game_loop()