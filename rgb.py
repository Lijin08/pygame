import pygame
import sys

# Initialize Pygame
pygame.init()

# Setup the window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Color Changer: R, G, B")

# Initial color (White)
object_color = (255, 255, 255)

# Main Loop
while True:
    screen.fill((30, 30, 30))  # Dark grey background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                object_color = (255, 0, 0)   # Red
            elif event.key == pygame.K_g:
                object_color = (0, 255, 0)   # Green
            elif event.key == pygame.K_b:
                object_color = (0, 0, 255)   # Blue

    # Draw the object (a rectangle in the center)
    pygame.draw.rect(screen, object_color, (150, 100, 100, 100))

    # Update the display
    pygame.display.flip()
