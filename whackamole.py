import pygame
import random


def main():
    try:
        pygame.init()

        # Mole image
        mole_image = pygame.image.load("mole.png")

        # Screen setup
        screen_width, screen_height = 650, 512
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        # Grid setup
        cell_size = 32
        rows, cols = screen_height // cell_size, screen_width // cell_size

        # Setting the initial mole position (0, 0)
        mole_x, mole_y = 0, 0

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mole is clicked
                    if (
                        mole_x <= event.pos[0] < mole_x + cell_size
                        and mole_y <= event.pos[1] < mole_y + cell_size
                    ):
                        # Move mole to a random position
                        mole_x = random.randrange(0, cols) * cell_size
                        mole_y = random.randrange(0, rows) * cell_size

            # Filling the background
            screen.fill("light green")

            # Draw grid
            for x in range(0, screen_width, cell_size):
                pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, screen_height))
            for y in range(0, screen_height, cell_size):
                pygame.draw.line(screen, (200, 200, 200), (0, y), (screen_width, y))

            # Draw mole
            screen.blit(mole_image, (mole_x, mole_y))

            # Update the display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
