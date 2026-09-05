# 🚀 Space Explorer - Galaxy Mission
# Mini Sprite Adventure Project

import pygame

def main():
    pygame.init()

    # PART 1: Create the game screen
    screen_width, screen_height = 700, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("🚀 Space Explorer - Galaxy Mission")

    # PART 2: Set sprite position and size
    x, y = 60, 60
    sprite_width, sprite_height = 50, 50
    speed = 5

    # PART 3: Define colors
    BLACK = (5, 5, 25)
    WHITE = (255, 255, 255)
    BLUE = (0, 150, 255)
    RED = (255, 60, 60)
    GREEN = (0, 255, 120)
    YELLOW = (255, 220, 0)
    PURPLE = (180, 80, 255)
    ORANGE = (255, 150, 30)
    CYAN = (0, 255, 255)

    current_color = WHITE

    # Font
    font = pygame.font.Font(None, 32)
    big_font = pygame.font.Font(None, 60)

    # PART 4: Game variables
    score = 0
    mission_complete = False

    # Energy crystals
    crystals = [
        pygame.Rect(150, 100, 25, 25),
        pygame.Rect(350, 220, 25, 25),
        pygame.Rect(550, 100, 25, 25),
        pygame.Rect(500, 380, 25, 25)
    ]

    # Portal
    portal_rect = pygame.Rect(620, 400, 50, 60)

    # Clock
    clock = pygame.time.Clock()

    running = True

    # PART 5: Game loop
    while running:

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # PART 6: Check arrow keys
        pressed = pygame.key.get_pressed()

        if not mission_complete:

            if pressed[pygame.K_LEFT]:
                x -= speed

            if pressed[pygame.K_RIGHT]:
                x += speed

            if pressed[pygame.K_UP]:
                y -= speed

            if pressed[pygame.K_DOWN]:
                y += speed

        # PART 7: Keep sprite inside the screen
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Create sprite rectangle
        sprite_rect = pygame.Rect(
            x, y, sprite_width, sprite_height
        )

        # PART 8: Change color according to position

        if x == 0:
            current_color = BLUE

        elif x == screen_width - sprite_width:
            current_color = YELLOW

        elif y == 0:
            current_color = RED

        elif y == screen_height - sprite_height:
            current_color = GREEN

        else:
            current_color = WHITE

        # PART 9: Collect energy crystals

        for crystal in crystals[:]:
            if sprite_rect.colliderect(crystal):
                crystals.remove(crystal)
                score += 10

        # Check portal
        if sprite_rect.colliderect(portal_rect) and len(crystals) == 0:
            mission_complete = True

        # ---------------- DRAWING ----------------

        # Space background
        screen.fill(BLACK)

        # Draw stars
        stars = [
            (50, 40), (120, 300), (210, 70),
            (280, 400), (390, 80), (450, 300),
            (580, 50), (650, 250), (100, 450)
        ]

        for star in stars:
            pygame.draw.circle(screen, WHITE, star, 3)

        # Solid planets
        pygame.draw.circle(
            screen, PURPLE, (100, 180), 35
        )

        pygame.draw.circle(
            screen, ORANGE, (600, 180), 30
        )

        # Outlined planets
        pygame.draw.circle(
            screen, CYAN, (300, 120), 40, 4
        )

        pygame.draw.circle(
            screen, GREEN, (400, 400), 45, 4
        )

        # Draw energy crystals
        for crystal in crystals:
            pygame.draw.circle(
                screen,
                YELLOW,
                crystal.center,
                12
            )

            # Small shine
            pygame.draw.circle(
                screen,
                WHITE,
                (crystal.centerx - 4, crystal.centery - 4),
                3
            )

        # Draw portal
        pygame.draw.rect(
            screen,
            PURPLE,
            portal_rect,
            4
        )

        pygame.draw.rect(
            screen,
            CYAN,
            (portal_rect.x + 10,
             portal_rect.y + 10,
             30,
             40)
        )

        # Draw moving player
        pygame.draw.rect(
            screen,
            current_color,
            sprite_rect
        )

        # Robot window
        pygame.draw.rect(
            screen,
            CYAN,
            (x + 12, y + 10, 26, 15)
        )

        # Robot antenna
        pygame.draw.line(
            screen,
            WHITE,
            (x + 25, y + 10),
            (x + 25, y - 5),
            3
        )

        # Robot antenna light
        pygame.draw.circle(
            screen,
            RED,
            (x + 25, y - 5),
            4
        )

        # Score display
        score_text = font.render(
            "Energy: " + str(score),
            True,
            WHITE
        )

        screen.blit(score_text, (20, 15))

        # Mission information
        info_text = font.render(
            "Collect all crystals and reach the portal!",
            True,
            WHITE
        )

        screen.blit(info_text, (20, 465))

        # Victory message
        if mission_complete:

            victory = big_font.render(
                "MISSION COMPLETE! 🚀",
                True,
                YELLOW
            )

            screen.blit(
                victory,
                (150, 220)
            )

        # Update display
        pygame.display.flip()

        # 60 FPS
        clock.tick(60)

    # Quit pygame
    pygame.quit()


# Start the game
if __name__ == "__main__":
    main()