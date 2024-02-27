import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Game")

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 30
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
